from flask import Blueprint, request, jsonify
from app.services.db_concessionaria_post import create_veiculo
from flask_jwt_extended import jwt_required, get_jwt_identity


# Criação do Blueprint para POST
concessionaria_post_bp = Blueprint('concessionaria_post', __name__, url_prefix='/concessionaria')


# POST: Criar novo veículo
@concessionaria_post_bp.route('/', methods=['POST'])
@jwt_required()
def adicionar_veiculo():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"erro": "Dados ausentes ou mal formatados"}), 400

        novo_veiculo = create_veiculo(data)
        return jsonify(novo_veiculo), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
