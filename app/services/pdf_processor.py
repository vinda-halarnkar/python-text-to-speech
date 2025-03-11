import os
import PyPDF2
from PyPDF2.errors import PdfReadError

class PDFProcessor:
    def extract_text(self, file_path, ):
        """Extracts text from a PDF file and saves it."""
        try:
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())

            return text

        except PdfReadError:
            raise ValueError("Invalid PDF file")
