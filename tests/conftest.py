import pytest
import os
import sys
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app, db
from app.models.tb_concessionaria import Concessionaria

@pytest.fixture(scope='module')
def app():
    """Configuração da aplicação para testes"""
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'TEST_DATABASE_URL',
        'postgresql://postgres:postgres@localhost:5432/concessionaria_test'
    )
    
    with app.app_context():
        db.create_all()
    
    yield app
    
    with app.app_context():
        db.drop_all()