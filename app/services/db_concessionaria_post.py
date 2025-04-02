from app.models.tb_concessionaria import Concessionaria, db
from sqlalchemy.exc import SQLAlchemyError


def create_veiculo(data):
    try:
        novo_veiculo = Concessionaria(
            marca=data.get('marca'),
            modelo=data.get('modelo'),
            versao=data.get('versao'),
            preco=data.get('preco'),
            estoque=data.get('estoque')
        )
        db.session.add(novo_veiculo)
        db.session.commit()
        return novo_veiculo.to_dict()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Erro ao inserir veículo: {str(e)}")
