import os
from fastapi import APIRouter, UploadFile, File
from services.pdf_service import convert_pdf_to_images
from services.gemini_service import extract_financial_data
from services.ratio_service import calculate_ratios
from services.growth_service import calculate_growth
from services.summary_service import generate_summary
from services.health_score import calculate_health_score

router = APIRouter()


@router.post("/analyze")
async def analyze_reports(
    current_report: UploadFile = File(...),
    previous_report: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    current_path = f"uploads/{current_report.filename}"
    previous_path = f"uploads/{previous_report.filename}"

    with open(current_path, "wb") as f:
        f.write(await current_report.read())

    with open(previous_path, "wb") as f:
        f.write(await previous_report.read())

    current_images = convert_pdf_to_images(current_path, "current")
    previous_images = convert_pdf_to_images(previous_path, "previous")

    current_financials = extract_financial_data(current_images)
    previous_financials = extract_financial_data(previous_images)

    current_ratios = calculate_ratios(current_financials)
    previous_ratios = calculate_ratios(previous_financials)

    current_health = calculate_health_score(current_ratios)
    previous_health = calculate_health_score(previous_ratios)

    growth = calculate_growth(
    current_financials,
    previous_financials
)
    summary = generate_summary(
    current_financials,
    previous_financials,
    current_ratios,
    growth
)

    return {

    "financial_data": {

        "current_year": current_financials,

        "previous_year": previous_financials

    },

    "financial_ratios": {

        "current_year": current_ratios,

        "previous_year": previous_ratios

    },

    "growth_analysis": growth,

    "financial_health": {

        "current_year": current_health,

        "previous_year": previous_health

    },

    "executive_summary": summary

}