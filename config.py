import os

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    
    # Google OAuth settings
    GOOGLE_OAUTH_CLIENT_ID = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
    
    # MongoDB settings
    MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
    
    # Firebase settings
    FIREBASE_CREDENTIALS_PATH = os.environ.get('FIREBASE_CREDENTIALS_PATH')
    FIREBASE_API_KEY = os.environ.get('FIREBASE_API_KEY')
    FIREBASE_AUTH_DOMAIN = os.environ.get('FIREBASE_AUTH_DOMAIN')
    FIREBASE_PROJECT_ID = os.environ.get('FIREBASE_PROJECT_ID')
    FIREBASE_STORAGE_BUCKET = os.environ.get('FIREBASE_STORAGE_BUCKET')
    FIREBASE_MESSAGING_SENDER_ID = os.environ.get('FIREBASE_MESSAGING_SENDER_ID')
    FIREBASE_APP_ID = os.environ.get('FIREBASE_APP_ID')
    FIREBASE_VAPID_KEY = os.environ.get('FIREBASE_VAPID_KEY') 