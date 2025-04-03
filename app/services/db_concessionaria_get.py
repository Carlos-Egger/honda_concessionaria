from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError


# Buscar todos os veículos
# Buscar todos os veículos com paginação
def get_all_veiculos(page=1, per_page=10):
    """
    Retorna uma lista paginada de veículos.

    :param page: Página atual (padrão: 1)
    :param per_page: Itens por página (padrão: 10)
    :return: Dicionário com dados da página
    """
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


# Buscar veículo por ID
def get_veiculo_by_id(veiculo_id):
    try:
        veiculo = Concessionaria.query.get(veiculo_id)
        if veiculo:
            return veiculo.to_dict()
        return None
    except SQLAlchemyError as e:
        raise Exception(f"Erro ao buscar veículo por ID: {str(e)}")
