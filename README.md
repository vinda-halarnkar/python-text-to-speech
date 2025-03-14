# python

# Text to Audio Project

## Features

- Simple Text to Speech converter
- Upload your PDF file and receive an audio file generated using Amazon Polly Service

## Technologies Used

- **Flask** - Web framework

## Prerequisites

- Python (version 3.6+ recommended)
- pip
- Virtual environment

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:vinda-halarnkar/python-text-to-speech.git
```

### If you have virtualenv installed
```bash
virtualenv venv
```

# Activate your virtual environment
```bash
source venv/bin/activate
```

# Install Dependencies
```bash
pip install -r requirements.txt
```

# Setup environment variables
```bash
AWS_AK=your-aws-access-key
AWS_SAK=your-aws-secret-key
SECRET_KEY=your-flask-secret-key

DOWNLOAD_FOLDER=app/static/downloads
UPLOAD_FOLDER=app/static/uploads
ALLOWED_EXTENSIONS=pdf

PORT=5005
```




# Run the Development Server
```bash
python main.py
```




