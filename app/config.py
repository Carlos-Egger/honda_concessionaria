import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Constrói a URI de conexão usando as variáveis de ambiente de forma segura
    # Importante: usamos postgresql+psycopg2 para garantir compatibilidade
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('PASSWORD')}"
        f"@{os.getenv('HOST')}:{os.getenv("DB_PORT")}/{os.getenv('DATABASE')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
