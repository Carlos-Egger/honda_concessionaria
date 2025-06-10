import pytest
from app.models.tb_concessionaria import Concessionaria

class TestRoutes:
    def test_get_all_veiculos(self, client, init_db):
        response = client.get('/concessionaria/')
        assert response.status_code == 200
        data = response.get_json()
        assert len(data['veiculos']) == 3
        assert data['total_itens'] == 3

    def test_get_veiculo_by_id(self, client, init_db):
        with client.application.app_context():
            veiculo = Concessionaria.query.first()
            response = client.get(f'/concessionaria/{veiculo.id}')
            assert response.status_code == 200
            assert response.get_json()['id'] == veiculo.id

    def test_create_veiculo(self, client, init_db):
        novo_veiculo = {
            'nome': 'Argo',
            'marca': 'Fiat',
            'ano': 2022,
            'cor': 'Vermelho'
        }
        response = client.post('/concessionaria/', json=novo_veiculo)
        assert response.status_code == 201
        data = response.get_json()
        assert data['nome'] == 'Argo'

    def test_update_veiculo(self, client, init_db):
        with client.application.app_context():
            veiculo = Concessionaria.query.first()
            update_data = {'cor': 'Azul'}
            response = client.put(
                f'/concessionaria/{veiculo.id}',
                json=update_data
            )
            assert response.status_code == 200
            updated = Concessionaria.query.get(veiculo.id)
            assert updated.cor == 'Azul'

    def test_delete_veiculo(self, client, init_db):
        with client.application.app_context():
            veiculo = Concessionaria.query.first()
            response = client.delete(f'/concessionaria/{veiculo.id}')
            assert response.status_code == 200
            assert Concessionaria.query.get(veiculo.id) is None