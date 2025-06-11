import pytest
import sys
from pathlib import Path
from app.models.user import User  # ajuste conforme seu projeto

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app, db
from app.models.tb_concessionaria import Concessionaria

@pytest.fixture(scope='module')
def app():
    """Fixture para criar e configurar a aplicação Flask"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/concessionaria_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Cria todas as tabelas
    with app.app_context():
        db.create_all()
    
    yield app
    
    # Limpa o banco de dados após os testes
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """Fixture para criar um cliente de teste"""
    return app.test_client()


@pytest.fixture
def init_db(app):
    with app.app_context():
        db.session.rollback()
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

        # Veículos existentes
        veiculos = [
            Concessionaria(nome='Gol', marca='Volkswagen', ano=2020, cor='Preto'),
            Concessionaria(nome='Onix', marca='Chevrolet', ano=2021, cor='Branco'),
            Concessionaria(nome='HB20', marca='Hyundai', ano=2019, cor='Prata')
        ]
        db.session.bulk_save_objects(veiculos)

        # Usuário admin para autenticação
        admin = User(email='admin@example.com')
        admin.set_password('admin123')
        db.session.add(admin)

        db.session.commit()
    yield
    with app.app_context():
        db.session.rollback()