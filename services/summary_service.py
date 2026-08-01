from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(current, previous, ratios, growth):

    prompt = f"""
You are a senior financial analyst.

Based on the following financial information, write a professional executive summary.

Current Year Financials:
{current}

Previous Year Financials:
{previous}

Financial Ratios:
{ratios}

Year-over-Year Growth:
{growth}

Write the summary in 6-8 professional sentences.

Focus on:
- Revenue trend
- Profitability
- Liquidity
- Debt position
- Overall financial health

Do not use bullet points.
"""

    response = model.generate_content(prompt)

    return response.text