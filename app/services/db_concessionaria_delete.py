from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError
from app import db  # Certifique-se de importar a instância do banco corretamente

# Deletar veículo por ID
def delete_veiculo(veiculo_id):
    try:
        veiculo = Concessionaria.query.get(veiculo_id)
        if not veiculo:
            return {"message": "Veículo não encontrado"}, 404

        db.session.delete(veiculo)
        db.session.commit()
        return {"message": "Veículo deletado com sucesso"}, 200
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Erro ao deletar veículo: {str(e)}")
