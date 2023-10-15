import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
SECRET_KEY = os.environ.get('SECRET_KEY')
DB_ENGINE = os.environ.get('DB_ENGINE')
DB_PORT = os.environ.get('DB_PORT')
VK_API_CLIENT_ID = os.environ.get('VK_API_CLIENT_ID')
VK_APP_KEY = os.environ.get('VK_API_KEY')