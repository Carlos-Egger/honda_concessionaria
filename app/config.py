import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}"
        f"@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
