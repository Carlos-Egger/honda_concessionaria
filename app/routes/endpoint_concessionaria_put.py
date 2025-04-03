from flask import Blueprint, request, jsonify
from app.services.db_concessionaria_update import update_veiculo

# Criação do Blueprint para PUT
concessionaria_put_bp = Blueprint('concessionaria_put', __name__, url_prefix='/concessionaria')

# PUT: Atualizar veículo por ID
@concessionaria_put_bp.route('/<int:veiculo_id>', methods=['PUT'])
def atualizar_veiculo(veiculo_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"erro": "Dados ausentes ou mal formatados"}), 400

        sucesso = update_veiculo(veiculo_id, data)
        if sucesso:
            return jsonify({"mensagem": "Veículo atualizado com sucesso"}), 200
        else:
            return jsonify({"erro": "Veículo não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
