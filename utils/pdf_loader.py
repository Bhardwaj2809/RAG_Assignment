import os
import fitz


def load_pdfs(pdf_folder: str):
    """
    Reads all PDFs inside pdf_folder.

    Returns:
        [
            {
                "document": "...",
                "page": 1,
                "text": "..."
            }
        ]
    """

    documents = []

    if not os.path.exists(pdf_folder):
        raise FileNotFoundError(f"Folder '{pdf_folder}' does not exist.")

    pdf_files = [
        file for file in os.listdir(pdf_folder)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise Exception("No PDF files found inside the pdfs folder.")

    for pdf_file in pdf_files:

        pdf_path = os.path.join(pdf_folder, pdf_file)

        pdf = fitz.open(pdf_path)

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text("text")

            # Clean unnecessary whitespace
            text = " ".join(text.split())

            if text.strip():

                documents.append(
                    {
                        "document": pdf_file,
                        "page": page_number,
                        "text": text,
                    }
                )

        pdf.close()

    return documents