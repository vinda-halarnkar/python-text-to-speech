from flask import Blueprint, request, redirect, url_for, render_template, flash
from app.services.pdf_processor import PDFProcessor
from app.services.polly_service import PollyService

from app.services.upload_service import UploadService

audio_file_name = "audio"
text_to_speech_bp = Blueprint("text_to_speech", __name__)

@text_to_speech_bp.route('/text_to_speech')
def text_to_speech():
    url = request.url
    page = url.rsplit('/', 1).pop()
    return render_template('index.html', page=page)


@text_to_speech_bp.route('/text-to-speech', methods=['POST'])
def text_to_speech_submit(audio_file_path=None):
    if 'file' in request.files and request.files['file']:
        flash('File not found', "error")
        response = upload(request)
        return response
    return redirect(url_for('text_to_speech.text_to_speech'))

def upload(request):
    try:
        if 'file' not in request.files:
            flash("No file part", "error")
            return redirect(url_for('text_to_speech.text_to_speech'))

        # Validate and save uploaded file
        file = request.files['file']
        upload_file = UploadService(file=file)
        file_path = upload_file.save_file()

        # Process PDF
        pdf_processor = PDFProcessor()
        text = pdf_processor.extract_text(file_path)

        if not text.strip():
            flash("No readable text found in PDF", "error")
            return redirect(url_for('home'))

        audio_file_path = convert_text_to_audio(text)
        return render_template('index.html', file_url=audio_file_path, page='text_to_speech')

    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('text_to_speech.text_to_speech'))

def convert_text_to_audio(text):
    # Convert text to speech
    polly_service = PollyService()
    audio_file_path = polly_service.convert_text_to_speech(text, audio_file_name)

    return audio_file_path
