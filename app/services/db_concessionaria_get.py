from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError


# Buscar todos os veículos
def get_all_veiculos():
    try:
        veiculos = Concessionaria.query.all()
        return [v.to_dict() for v in veiculos]
    except SQLAlchemyError as e:
        raise Exception(f"Erro ao buscar todos os veículos: {str(e)}")


# Buscar veículo por ID
def get_veiculo_by_id(veiculo_id):
    try:
        veiculo = Concessionaria.query.get(veiculo_id)
        if veiculo:
            return veiculo.to_dict()
        return None
    except SQLAlchemyError as e:
        raise Exception(f"Erro ao buscar veículo por ID: {str(e)}")
