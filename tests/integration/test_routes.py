import pytest
from app.models.tb_concessionaria import Concessionaria
from flask import json

class TestRoutes:

    def login_and_get_token(self, client):
        # Realiza login para obter o token de autenticação
        response = client.post('/login', json={
            'email': 'admin@example.com',
            'senha': 'admin123'
        })
        assert response.status_code == 200, f"Login falhou: {response.data}"
        json_data = response.get_json()
        assert 'access_token' in json_data, "Token de acesso não retornado"
        return json_data['access_token']

    def test_get_all_veiculos(self, client, init_db):
        token = self.login_and_get_token(client)
        response = client.get('/concessionaria/', headers={
            'Authorization': f'Bearer {token}'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert 'veiculos' in data
        assert 'total_itens' in data
        assert len(data['veiculos']) == 3
        assert data['total_itens'] == 3

    def test_get_veiculo_by_id(self, client, init_db):
        token = self.login_and_get_token(client)
        with client.application.app_context():
            veiculo = Concessionaria.query.first()
            assert veiculo is not None, "Nenhum veículo encontrado no banco de dados"
            response = client.get(
                f'/concessionaria/{veiculo.id}',
                headers={'Authorization': f'Bearer {token}'}
            )
            assert response.status_code == 200
            data = response.get_json()
            assert data['id'] == veiculo.id

    def test_create_veiculo(self, client, init_db):
        token = self.login_and_get_token(client)
        novo_veiculo = {
            'nome': 'Argo',
            'marca': 'Fiat',
            'ano': 2022,
            'cor': 'Vermelho'
        }
        response = client.post('/concessionaria/', json=novo_veiculo, headers={
            'Authorization': f'Bearer {token}'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['nome'] == novo_veiculo['nome']
        assert data['marca'] == novo_veiculo['marca']
        assert data['ano'] == novo_veiculo['ano']
        assert data['cor'] == novo_veiculo['cor']

    def test_update_veiculo(self, client, init_db):
        token = self.login_and_get_token(client)
        with client.application.app_context():
            veiculo = Concessionaria.query.first()
            assert veiculo is not None, "Nenhum veículo encontrado para atualizar"
            update_data = {'cor': 'Azul'}
            response = client.put(
                f'/concessionaria/{veiculo.id}',
                json=update_data,
                headers={'Authorization': f'Bearer {token}'}
            )
            assert response.status_code == 200
            updated = Concessionaria.query.get(veiculo.id)
            assert updated.cor == 'Azul'

    def test_delete_veiculo(self, client, init_db):
        token = self.login_and_get_token(client)
        with client.application.app_context():
            veiculo = Concessionaria.query.first()
            assert veiculo is not None, "Nenhum veículo encontrado para deletar"
            response = client.delete(
                f'/concessionaria/{veiculo.id}',
                headers={'Authorization': f'Bearer {token}'}
            )
            assert response.status_code == 200
            assert Concessionaria.query.get(veiculo.id) is None
