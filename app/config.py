import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER")
    ALLOWED_EXTENSIONS = "pdf"
    AWS_ACCESS_KEY = os.getenv("AWS_AK")
    AWS_SECRET_KEY = os.getenv("AWS_SAK")
    SECRET_KEY = os.getenv("SECRET_KEY")


