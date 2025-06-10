from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError
from app import db  # Certifique-se de importar sua instância do SQLAlchemy

def get_all_veiculos(page=1, per_page=10):
    try:
        pagination = Concessionaria.query.paginate(page=page, per_page=per_page, error_out=False)
        return {
            "veiculos": [v.to_dict() for v in pagination.items],
            "pagina_atual": pagination.page,
            "total_paginas": pagination.pages,
            "total_itens": pagination.total,
            "tem_proxima": pagination.has_next,
            "tem_anterior": pagination.has_prev
        }
    except SQLAlchemyError as e:
        raise Exception(f"Erro ao buscar veículos com paginação: {str(e)}")

def get_veiculo_by_id(veiculo_id):
    try:
        veiculo = db.session.get(Concessionaria, veiculo_id)
        if veiculo:
            return veiculo.to_dict()
        return None
    except SQLAlchemyError as e:
        raise Exception(f"Erro ao buscar veículo por ID: {str(e)}")
