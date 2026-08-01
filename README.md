# AI Financial Statement Analysis System

An AI-powered financial analysis application that automates financial statement analysis using Gemini Vision, FastAPI, and Python. The system extracts financial information from uploaded financial statement PDFs, calculates financial ratios, performs year-over-year growth analysis, generates a financial health score, and produces an AI-powered executive summary.

##  Features

- Upload two financial statement PDFs
- Convert PDF pages into images using PyMuPDF
- Extract financial information using Gemini Vision
- Calculate key financial ratios
- Perform Year-over-Year (YoY) growth analysis
- Generate Financial Health Score
- Generate AI-powered Executive Summary
- REST API built with FastAPI
- Interactive API documentation using Swagger UI

## Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| AI Model | Gemini 2.5 Flash |
| Language | Python |
| PDF Processing | PyMuPDF |
| Image Processing | Pillow |
| API Testing | Swagger UI |

## Project Structure

```
financial-analysis-ai/
│
├── services/
│   ├── pdf_service.py
│   ├── gemini_service.py
│   ├── ratio_service.py
│   ├── growth_service.py
│   ├── health_score.py
│   └── summary_service.py
│
├── routes/
│   └── analysis.py
│
├── uploads/
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## Project Workflow

1. User uploads two financial statement PDFs.
2. PDFs are converted into images using PyMuPDF.
3. Gemini Vision extracts financial data from the images.
4. Python calculates financial ratios.
5. Year-over-Year growth is calculated.
6. Financial Health Score is generated.
7. Gemini generates an executive summary.
8. API returns a structured JSON response.

## Financial Ratios Calculated

- Profit Margin
- Current Ratio
- Debt-to-Equity Ratio
- Return on Assets (ROA)
- Return on Equity (ROE)

## API Endpoint

### Analyze Financial Statements

```
POST /analyze
```

Upload:

- Current Year Financial Statement PDF
- Previous Year Financial Statement PDF

Returns:

- Financial Data
- Financial Ratios
- Year-over-Year Growth
- Financial Health Score
- Executive Summary

## Sample Response

```json
{
  "financial_data": {
    "current_year": {},
    "previous_year": {}
  },
  "financial_ratios": {
    "current_year": {},
    "previous_year": {}
  },
  "growth_analysis": {},
  "financial_health": {
    "current_year": {},
    "previous_year": {}
  },
  "executive_summary": "..."
}
```

## Future Improvements

- Support additional financial ratios
- Multi-company comparison
- Interactive dashboard
- Historical trend visualization
- Export analysis as PDF
- Cloud deployment

## Author

Akshata Kelkar

MBA – Data Science & Analytics

AI | Data Analytics | Financial Analytics
