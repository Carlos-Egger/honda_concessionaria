import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv\
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "sua_chave_secreta_super_segura"
    jwt = JWTManager(app)
        
    # Carregar variáveis de ambiente do .env
    load_dotenv()
    
    # Configurações
    app.config.from_object('app.config.Config')
    
    # Inicializa o banco de dados
    db.init_app(app)
    jwt.init_app(app)
    
    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.endpoint_concessionaria_get import concessionaria_get_bp
    from app.routes.endpoint_concessionaria_post import concessionaria_post_bp
    from app.routes.endpoint_concessionaria_put import concessionaria_put_bp
    from app.routes.endpoint_concessionaria_delete import concessionaria_delete_bp
    app.register_blueprint(auth_bp)    
    app.register_blueprint(concessionaria_get_bp)
    app.register_blueprint(concessionaria_post_bp)
    app.register_blueprint(concessionaria_put_bp)
    app.register_blueprint(concessionaria_delete_bp)
    
    return app