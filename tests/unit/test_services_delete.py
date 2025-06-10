import pytest
from app.services.db_concessionaria_delete import delete_veiculo
from app.models.tb_concessionaria import Concessionaria

class TestDeleteServices:
    def test_delete_veiculo(self, app, init_db):
        with app.app_context():
            veiculo = Concessionaria.query.first()
            deleted = delete_veiculo(veiculo.id)
            assert deleted is True
            assert Concessionaria.query.get(veiculo.id) is None

    def test_delete_nonexistent_veiculo(self, app, init_db):
        with app.app_context():
            deleted = delete_veiculo(9999)
            assert deleted is False