import pytest
from app.services.db_concessionaria_get import get_all_veiculos, get_veiculo_by_id
from app.models.tb_concessionaria import Concessionaria

class TestGetServices:
    
    def test_get_all_veiculos(self, app, init_db):
        with app.app_context():
            result = get_all_veiculos(page=1, per_page=2)
            # Verifica se trouxe 2 veículos conforme per_page
            assert len(result['veiculos']) == 2
            # Verifica a página atual
            assert result['pagina_atual'] == 1
            # Verifica o total de veículos no banco (populado no init_db)
            assert result['total'] == 3

    def test_get_veiculo_by_id(self, app, init_db):
        with app.app_context():
            # Busca o primeiro veículo cadastrado na base de teste
            veiculo = Concessionaria.query.first()
            result = get_veiculo_by_id(veiculo.id)
            # Verifica se os dados retornados batem com o objeto do banco
            assert result is not None
            assert result['id'] == veiculo.id
            assert result['nome'] == veiculo.nome

    def test_get_nonexistent_veiculo(self, app, init_db):
        with app.app_context():
            # Busca um veículo que não existe
            result = get_veiculo_by_id(9999)
            # Espera None, pois não deve existir
            assert result is None
