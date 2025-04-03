from sqlalchemy import Column, Integer, String, Float
from app import db

class Concessionaria(db.Model):
    __tablename__ = 'tb_concessionaria'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    versao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<Concessionaria(id={self.id}, marca='{self.marca}', modelo='{self.modelo}', "
                f"versao='{self.versao}', preco={self.preco}, estoque={self.estoque})>")

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "versao": self.versao,
            "preco": self.preco,
            "estoque": self.estoque
        }
