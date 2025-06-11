import os
import pytest
import sys
from pathlib import Path
from app.models.user import User
from app import create_app, db

sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture(scope='module')
def app():
    """Fixture para criar e configurar a aplicação Flask"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'TEST_DATABASE_URL',
        'postgresql://postgres:postgres@localhost:5432/concessionaria_test'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
    
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db(app):
    with app.app_context():
        # Limpa todas as tabelas
        db.session.rollback()
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

        # Cria dados de teste
        veiculos = [
            Concessionaria(nome='Fit', marca='Honda', ano=2020, cor='Preto'),
            Concessionaria(nome='Civic', marca='Honda', ano=2021, cor='Branco'),
            Concessionaria(nome='City', marca='Honda', ano=2019, cor='Prata')
        ]
        db.session.bulk_save_objects(veiculos)

        # Usuário admin
        admin = User(email='admin@example.com')
        admin.set_password('admin123')
        db.session.add(admin)

        db.session.commit()
    yield