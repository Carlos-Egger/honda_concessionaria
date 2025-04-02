from flask import Blueprint, jsonify, request
from app.services.db_concessionaria_get import get_all_veiculos, get_veiculo_by_id

# Criação do Blueprint para os endpoints de GET
concessionaria_get_bp = Blueprint('concessionaria_get', __name__, url_prefix='/concessionaria')


# GET: Buscar todos os veículos
@concessionaria_get_bp.route('/', methods=['GET'])
def listar_veiculos():
    try:
        veiculos = get_all_veiculos()
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
