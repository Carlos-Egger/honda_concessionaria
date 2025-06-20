from flask import Blueprint, jsonify, request
from app.services.db_concessionaria_get import get_all_veiculos, get_veiculo_by_id
from flask_jwt_extended import jwt_required, get_jwt_identity


# Criação do Blueprint para os endpoints de GET
concessionaria_get_bp = Blueprint('concessionaria_get', __name__, url_prefix='/concessionaria')


# GET: Buscar todos os veículos
@concessionaria_get_bp.route('/', methods=['GET'])
@jwt_required()
def listar_veiculos():
    try:
        # Captura os parâmetros da query string (ex: ?page=2&per_page=20)
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        # Chamada da função com paginação
        veiculos = get_all_veiculos(page=page, per_page=per_page)

        return jsonify(veiculos), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# GET: Buscar veículo por ID
@concessionaria_get_bp.route('/<int:veiculo_id>', methods=['GET'])
def buscar_veiculo_por_id(veiculo_id):
    try:
        veiculo = get_veiculo_by_id(veiculo_id)
        if veiculo:
            return jsonify(veiculo), 200
        return jsonify({"mensagem": "Veículo não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
