import pytest
from app.services.db_concessionaria_update import update_veiculo
from app.models.tb_concessionaria import Concessionaria

class TestUpdateServices:
    def test_update_veiculo(self, app, init_db):
        with app.app_context():
            veiculo = Concessionaria.query.first()
            updated = update_veiculo(veiculo.id, {'cor': 'Verde'})
            assert updated is True
            assert Concessionaria.query.get(veiculo.id).cor == 'Verde'

    def test_update_nonexistent_veiculo(self, app, init_db):
        with app.app_context():
            updated = update_veiculo(9999, {'cor': 'Azul'})
            assert updated is False