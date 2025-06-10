from flask import Blueprint, jsonify
from app.services.db_concessionaria_delete import delete_veiculo

concessionaria_delete_bp = Blueprint('concessionaria_delete', __name__, url_prefix='/concessionaria')

@concessionaria_delete_bp.route('/<int:veiculo_id>', methods=['DELETE'])
def remover_veiculo(veiculo_id):
    try:
        sucesso = delete_veiculo(veiculo_id)
        if sucesso:
            return jsonify({"mensagem": "Veículo removido com sucesso"}), 200
        else:
            return jsonify({"erro": "Veículo não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

