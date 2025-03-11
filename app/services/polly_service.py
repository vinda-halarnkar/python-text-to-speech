import os
import boto3
from flask import current_app, url_for
from botocore.exceptions import BotoCoreError, NoCredentialsError
from app.config import Config as app_config

class PollyService:
    def __init__(self):
        self.client = boto3.client(
            'polly',
            aws_access_key_id=app_config.AWS_ACCESS_KEY,
            aws_secret_access_key=app_config.AWS_SECRET_KEY,
            region_name='us-east-1'
        )

    def convert_text_to_speech(self, text, filename):
        """Converts extracted text to speech using AWS Polly."""
        try:
            result = self.client.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId='Aditi')
            audio = result['AudioStream'].read()

            download_folder = os.environ.get("DOWNLOAD_FOLDER")
            audio_file_path = os.path.join(download_folder, f"{filename}.mp3")

            with open(audio_file_path, "wb") as audio_file:
                audio_file.write(audio)

            audio_file_path = url_for('static', filename=f"downloads/{filename}.mp3")

            return audio_file_path

        except NoCredentialsError:
            raise RuntimeError("AWS credentials missing or incorrect")
        except BotoCoreError as e:
            raise RuntimeError(f"AWS Polly error: {str(e)}")
