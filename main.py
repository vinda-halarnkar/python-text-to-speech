import os

from flask import render_template
from app import create_app

from app.config import Config

app = create_app()

app_config = Config()

app.secret_key = app_config.SECRET_KEY

#Root route
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=os.environ.get('PORT'))