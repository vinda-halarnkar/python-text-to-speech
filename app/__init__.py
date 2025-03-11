from flask import Flask
from app.routes.text_to_speech import text_to_speech_bp

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")

    # Register Blueprints (routes)
    app.register_blueprint(text_to_speech_bp)

    return app