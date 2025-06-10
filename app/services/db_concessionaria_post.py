from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError

def create_veiculo(data):
    try:
        novo_veiculo = Concessionaria(
            nome=data['nome'],
            marca=data['marca'],
            ano=data['ano'],
            cor=data['cor']
        )
        db.session.add(novo_veiculo)
        db.session.commit()
        return novo_veiculo.to_dict()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Erro ao criar veículo: {str(e)}")
    except KeyError as e:
        raise Exception(f"Campo obrigatório faltando: {str(e)}")