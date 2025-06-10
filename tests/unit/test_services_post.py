import pytest
from app.services.db_concessionaria_post import create_veiculo
from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import IntegrityError

class TestPostServices:

    def test_create_veiculo(self, app, init_db):
        """Testa a criação de um veículo válido"""
        with app.app_context():
            data = {
                'nome': 'City',
                'marca': 'Honda',
                'ano': 2021,
                'cor': 'Branco'
            }
            result = create_veiculo(data)
            assert 'id' in result
            assert result['nome'] == 'City'

            # Confirma que o veículo está no banco
            veiculo_db = Concessionaria.query.get(result['id'])
            assert veiculo_db is not None
            assert veiculo_db.nome == 'City'

    def test_create_veiculo_missing_fields(self, app):
        """Testa a criação com campos faltando"""
        with app.app_context():
            # Ajuste conforme a exceção específica lançada pelo seu serviço
            with pytest.raises(Exception):
                create_veiculo({'nome': 'Incompleto'})
