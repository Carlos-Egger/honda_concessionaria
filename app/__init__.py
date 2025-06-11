import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

# Instâncias globais
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)
    
    # Carregar variáveis de ambiente do .env PRIMEIRO
    load_dotenv()
    
    # Configurações do arquivo de config
    app.config.from_object('app.config.Config')
    
    # Configuração JWT (pode sobrescrever se necessário)
    app.config["JWT_SECRET_KEY"] = "supersecret123"
    
    # Inicializar extensões
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