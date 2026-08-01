from dotenv import load_dotenv
import os
import json
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_financial_data(image_paths):

    images = []

    for image_path in image_paths:
        images.append(Image.open(image_path))

    prompt = """
You are an expert financial analyst.

Analyze these financial statement images.

Extract ONLY these values.

Return ONLY valid JSON.

{
    "revenue": null,
    "net_income": null,
    "total_assets": null,
    "total_liabilities": null,
    "total_equity": null,
    "current_assets": null,
    "current_liabilities": null
}
"""

    response = model.generate_content(
        [prompt] + images
    )

    response_text = response.text

    response_text = response_text.replace("```json", "")
    response_text = response_text.replace("```", "")
    response_text = response_text.strip()

    return json.loads(response_text)

