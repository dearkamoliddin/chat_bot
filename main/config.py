import os
from dotenv import load_dotenv
load_dotenv()

ADMIN = os.getenv("ADMIN")
TOKEN = os.getenv("TOKEN")

DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
