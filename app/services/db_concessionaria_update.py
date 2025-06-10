from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError
from app import db

def update_veiculo(veiculo_id, data):
    veiculo = Concessionaria.query.get(veiculo_id)
    if not veiculo:
        return False
    try:
        for key, value in data.items():
            if hasattr(veiculo, key):
                setattr(veiculo, key, value)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False
