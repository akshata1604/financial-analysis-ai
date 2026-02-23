from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(current_data, previous_data, current_ratios, previous_ratios, growth):

    prompt = f"""
You are a senior financial analyst.

Analyze the financial performance comparing two quarters.

Current Year Data:
{current_data}

Previous Year Data:
{previous_data}

Current Ratios:
{current_ratios}

Previous Ratios:
{previous_ratios}

Growth Metrics:
{growth}

Write a concise executive-level financial summary.
Focus on:
- Profitability trend
- Liquidity
- Leverage
- Efficiency
- Growth interpretation

Keep it professional and under 200 words.
No bullet points.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content