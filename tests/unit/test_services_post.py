import pytest
from app.services.db_concessionaria_post import create_veiculo
from app.models.tb_concessionaria import Concessionaria

class TestPostServices:
    def test_create_veiculo(self, app):
        with app.app_context():
            data = {
                'nome': 'Toro',
                'marca': 'Fiat',
                'ano': 2021,
                'cor': 'Branco'
            }
            result = create_veiculo(data)
            assert result['id'] is not None
            assert Concessionaria.query.get(result['id']) is not None

    def test_create_veiculo_invalid_data(self, app):
        with app.app_context(), pytest.raises(Exception):
            create_veiculo({'nome': 'Incompleto'})