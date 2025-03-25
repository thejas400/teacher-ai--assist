# Teachr Assist

Teachr Assist is a web application that helps teachers grade student submissions using AI. It features OCR for text extraction, AI-powered grading using Google's Gemini model, analytics dashboard, and real-time notifications.

## Features

- **OCR Processing**: Extract text from images and PDFs using Google Cloud Vision API
- **AI-Powered Grading**: Grade student submissions against teacher solutions using Google's Gemini model
- **Analytics Dashboard**: Visualize grading trends and statistics using Chart.js
- **Real-time Notifications**: Get notified about new submissions and grading results using Firebase Cloud Messaging
- **User Authentication**: Secure login using Google OAuth
- **File Management**: Upload and manage teacher solutions and student submissions

## Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account with the following APIs enabled:
  - Cloud Vision API
  - Cloud Storage API
  - Vertex AI API
- Firebase project for notifications
- MongoDB database

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/teachr-assist.git
cd teachr-assist
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
MONGODB_URI=your-mongodb-uri
GOOGLE_OAUTH_CLIENT_ID=your-client-id
GOOGLE_OAUTH_CLIENT_SECRET=your-client-secret
FIREBASE_CREDENTIALS=path/to/your/firebase-credentials.json
FIREBASE_VAPID_KEY=your-vapid-key
```

5. Set up Google Cloud:
   - Create a project in Google Cloud Console
   - Enable required APIs
   - Create a service account and download credentials
   - Set up Cloud Storage bucket for file uploads

6. Set up Firebase:
   - Create a new Firebase project
   - Download service account credentials
   - Generate VAPID key for web push notifications

7. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

8. Run the application:
```bash
flask run
```

## Project Structure

```
teachr-assist/
├── app/
│   ├── models/
│   │   ├── file.py
│   │   ├── grading.py
│   │   └── fcm_token.py
│   ├── routes/
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── upload.py
│   │   ├── grade.py
│   │   ├── analytics.py
│   │   └── notifications.py
│   ├── services/
│   │   ├── ocr_service.py
│   │   ├── grading_service.py
│   │   ├── analytics_service.py
│   │   └── notification_service.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── firebase-messaging-sw.js
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── dashboard.html
│       ├── upload.html
│       ├── grade.html
│       └── analytics.html
├── config.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 