from app.models.tb_concessionaria import Concessionaria
from sqlalchemy.exc import SQLAlchemyError
from app import db  # Certifique-se de importar a instância do banco corretamente

# Atualizar veículo por ID
def update_veiculo(veiculo_id, data):
    try:
        veiculo = Concessionaria.query.get(veiculo_id)
        if not veiculo:
            return {"message": "Veículo não encontrado"}, 404

        for key, value in data.items():
            if hasattr(veiculo, key):
                setattr(veiculo, key, value)

        db.session.commit()
        return {"message": "Veículo atualizado com sucesso"}, 200
    except SQLAlchemyError as e:
        db.session.rollback()
        raise Exception(f"Erro ao atualizar veículo: {str(e)}")
