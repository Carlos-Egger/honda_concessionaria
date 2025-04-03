import os
from dotenv import load_dotenv

load_dotenv()

print("Variáveis de ambiente carregadas:")
print(f"USER: {os.getenv('USER')}")
print(f"PASSWORD: {os.getenv('PASSWORD')}")
print(f"HOST: {os.getenv('HOST')}")
print(f"PORT: {os.getenv('PORT')}")
print(f"DATABASE: {os.getenv('DATABASE')}")

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
