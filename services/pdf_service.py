import fitz
import os


def convert_pdf_to_images(pdf_path, prefix):

    image_paths = []

    pdf = fitz.open(pdf_path)

    for page_number in range(len(pdf)):

        page = pdf.load_page(page_number)

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        image_path = f"uploads/{prefix}_page_{page_number + 1}.png"

        pix.save(image_path)

        image_paths.append(image_path)

    pdf.close()

    return image_paths