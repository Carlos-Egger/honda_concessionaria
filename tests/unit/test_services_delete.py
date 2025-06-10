import pytest
from app.services.db_concessionaria_delete import delete_veiculo
from app.models.tb_concessionaria import Concessionaria

class TestDeleteServices:
    def delete_veiculo(veiculo_id):
        veiculo = Concessionaria.query.get(veiculo_id)
        if not veiculo:
            return False
        db.session.delete(veiculo)
        db.session.commit()
        return True

    def test_delete_nonexistent_veiculo(self, app, init_db):
        with app.app_context():
            deleted = delete_veiculo(9999)
            assert deleted is False