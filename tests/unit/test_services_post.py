import pytest
from app.services.db_concessionaria_post import create_veiculo
from app.models.tb_concessionaria import Concessionaria

class TestPostServices:
    def test_create_veiculo(self, app):
        """Testa a criação de um veículo válido"""
        with app.app_context():
            data = {
                'nome': 'Toro',
                'marca': 'Fiat',
                'ano': 2021,
                'cor': 'Branco'
            }
            result = create_veiculo(data)
            assert 'id' in result
            assert result['nome'] == 'Toro'

    def test_create_veiculo_missing_fields(self, app):
        """Testa a criação com campos faltando"""
        with app.app_context(), pytest.raises(Exception):
            create_veiculo({'nome': 'Incompleto'})