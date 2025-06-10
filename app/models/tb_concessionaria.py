from app import db

class Concessionaria(db.Model):
    __tablename__ = 'tb_concessionaria'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    cor = db.Column(db.String(30), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'marca': self.marca,
            'ano': self.ano,
            'cor': self.cor
        }