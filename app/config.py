import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'segredo-muito-secreto')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:postgres@localhost:5432/concessionaria'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False