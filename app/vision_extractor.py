from pdf2image import convert_from_bytes
import base64
import io

def pdf_to_base64_images(file):
    pdf_bytes = file.read()
    images = convert_from_bytes(pdf_bytes)

    encoded_images = []

    for img in images:
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        encoded_images.append(base64.b64encode(buffer.getvalue()).decode())

    return encoded_images

from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_financials(base64_images, target_date):

    prompt = f"""
You are a financial analyst.

Extract financial metrics strictly for {target_date} only.

If multiple dates exist, ignore all other dates.

Return STRICT JSON with the following keys:

revenue
net_income
total_assets
total_liabilities
equity
current_assets
current_liabilities

Rules:
- Return numbers only
- No commas
- No currency symbols
- No explanation
- Only JSON
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ] + [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{img}"
                        }
                    }
                    for img in base64_images
                ]
            }
        ]
    )

    raw_output= response.choices[0].message.content
     # Remove markdown if exists
    cleaned = raw_output.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned)