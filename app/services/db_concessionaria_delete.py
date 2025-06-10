from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError
from app import db  # Importar instância do banco corretamente

def delete_veiculo(veiculo_id):
    try:
        veiculo = Concessionaria.query.get(veiculo_id)
        if not veiculo:
            return False

        db.session.delete(veiculo)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        raise  # relança a exceção para o controlador tratar
