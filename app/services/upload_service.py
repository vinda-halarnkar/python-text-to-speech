from werkzeug.datastructures import FileStorage
from app.config import Config as app_config
import os

class UploadService(object):
    def __init__(self, file: FileStorage, upload_folder: str = None, allowed_ext: list = None, max_file_size: int = 10 * 1024 * 1024):
        self.upload_folder = upload_folder or app_config.UPLOAD_FOLDER
        self.allowed_extensions = allowed_ext
        self.max_file_size = max_file_size
        self.file = file

    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in self.allowed_extensions

    def validate_file_size(self, file):
        return file.content_length <= self.max_file_size * 1024 * 1024  # in bytes

    def save_file(self):
        filename = self.file.filename
        if self.validate_file_size(self.file):
            file_path = os.path.join(self.upload_folder, filename)
            self.file.save(file_path)
            return file_path
        else:
            return None
