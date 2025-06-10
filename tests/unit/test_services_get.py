import pytest
from app.services.db_concessionaria_get import get_all_veiculos, get_veiculo_by_id
from app.models.tb_concessionaria import Concessionaria

class TestGetServices:

    def test_get_all_veiculos(self, app, init_db):
        with app.app_context():
            result = get_all_veiculos(page=1, per_page=2)
            assert len(result['veiculos']) == 2
            assert result['pagina_atual'] == 1
            assert result['total_itens'] == 3

    def test_get_veiculo_by_id(self, app, init_db):
        with app.app_context():
            veiculo = Concessionaria.query.first()
            result = get_veiculo_by_id(veiculo.id)
            assert result is not None
            assert result['id'] == veiculo.id
            assert result['nome'] == veiculo.nome

    def test_get_nonexistent_veiculo(self, app, init_db):
        with app.app_context():
            result = get_veiculo_by_id(9999)
            assert result is None
