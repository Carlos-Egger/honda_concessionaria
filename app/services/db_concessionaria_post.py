from app.models.tb_concessionaria import Concessionaria
from app import db
from sqlalchemy.exc import SQLAlchemyError

def create_veiculo(data):
    try:
        # Verifica campos obrigatórios
        required_fields = ['nome', 'marca', 'ano', 'cor']
        if not all(field in data for field in required_fields):
            raise ValueError("Campos obrigatórios faltando")
        
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
    except Exception as e:
        db.session.rollback()
        raise e