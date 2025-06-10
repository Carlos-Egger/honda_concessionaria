import pytest
from app.services.db_concessionaria_get import get_all_veiculos, get_veiculo_by_id
from app.models.tb_concessionaria import Concessionaria

class TestGetServices:
    
    def get_all_veiculos(page=1, per_page=10):
        pagination = Concessionaria.query.paginate(page=page, per_page=per_page, error_out=False)
        
        veiculos = []
        for v in pagination.items:
            veiculos.append({
                "id": v.id,
                "nome": v.nome,
                # Inclua outros campos que achar relevante
            })
        
        return {
            "veiculos": veiculos,
            "pagina_atual": pagination.page,
            "total": pagination.total
        }
    

    def get_veiculo_by_id(veiculo_id):
        veiculo = Concessionaria.query.get(veiculo_id)
        if veiculo:
            return {
                "id": veiculo.id,
                "nome": veiculo.nome,
                # outros campos aqui
            }
        return None

    def test_get_nonexistent_veiculo(self, app, init_db):
        with app.app_context():
            # Busca um veículo que não existe
            result = get_veiculo_by_id(9999)
            # Espera None, pois não deve existir
            assert result is None
