from fastapi import FastAPI, UploadFile, File
from app.vision_extractor import pdf_to_base64_images, extract_financials
from app.summary import generate_summary
from app.analytics import calculate_ratios, yoy_growth

app = FastAPI()

@app.post("/extract")
async def extract_data(
    file_current: UploadFile = File(...),
    file_previous: UploadFile = File(...),
    current_date: str = "June 30, 2024",
    previous_date: str = "June 30, 2023"
):
    
    # Convert PDFs to images
    images_current = pdf_to_base64_images(file_current.file)
    images_previous = pdf_to_base64_images(file_previous.file)

    # Extract financial data using GPT
    current_data = extract_financials(images_current, current_date)
    previous_data = extract_financials(images_previous, previous_date)

    
    current_ratios = calculate_ratios(current_data)
    previous_ratios = calculate_ratios(previous_data)

    growth = yoy_growth(current_data, previous_data)

    summary = generate_summary(
    current_data,
    previous_data,
    current_ratios,
    previous_ratios,
    growth
)

    return {
    "current_data": current_data,
    "previous_data": previous_data,
    "current_ratios": current_ratios,
    "previous_ratios": previous_ratios,
    "yoy_growth": growth,
    "executive_summary": summary
}
    

