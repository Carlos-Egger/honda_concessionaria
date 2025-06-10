import pytest
import sys
import os
from pathlib import Path

# Adiciona o diretório raiz do projeto ao PATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app, db
from app.models.tb_concessionaria import Concessionaria

@pytest.fixture(scope='module')
def app():
    """Cria e configura uma nova aplicação para cada teste"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/concessionaria_test'
    
    with app.app_context():
        db.create_all()
    
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """Um cliente de teste para a aplicação"""
    return app.test_client()

@pytest.fixture
def init_db(app):
    """Preenche o banco de dados com dados de teste"""
    with app.app_context():
        # Limpa dados existentes
        db.session.rollback()
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

        # Adiciona dados de teste
        veiculos = [
            Concessionaria(nome='Gol', marca='Volkswagen', ano=2020, cor='Preto'),
            Concessionaria(nome='Onix', marca='Chevrolet', ano=2021, cor='Branco'),
            Concessionaria(nome='HB20', marca='Hyundai', ano=2019, cor='Prata')
        ]
        db.session.bulk_save_objects(veiculos)
        db.session.commit()
    
    yield
    
    with app.app_context():
        db.session.rollback()