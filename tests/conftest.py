import pytest
from app import create_app, db
from app.models.tb_concessionaria import Concessionaria

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('config.TestConfig')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/concessionaria_test'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_veiculo(app):
    with app.app_context():
        veiculo = Concessionaria(
            nome='Gol',
            marca='Volkswagen',
            ano=2020,
            cor='Preto'
        )
        db.session.add(veiculo)
        db.session.commit()
        return veiculo