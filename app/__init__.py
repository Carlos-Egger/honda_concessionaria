from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv

db = SQLAlchemy()


def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__, static_folder="static")

    # Carregar variáveis de ambiente do .env
    load_dotenv()

    # Configuração do Flask a partir de um objeto de configuração
    app.config.from_object("app.config.Config")

    # Inicialização da extensão SQLAlchemy
    db.init_app(app)

    # Habilitar CORS
    CORS(app)

    # Inicialização do Flask-RESTX
    api = Api(
        app,
        version="1.0",
        title="API Concessionária",
        description="API para gerenciamento de veículos da concessionária",
    )

    # Registrar os Blueprints das rotas
    from app.routes.endpoint_concessionaria_get import concessionaria_get_bp
    from app.routes.endpoint_concessionaria_post import concessionaria_post_bp

    app.register_blueprint(concessionaria_get_bp)
    app.register_blueprint(concessionaria_post_bp)

    # Criar as tabelas no banco de dados (se não existirem)
    with app.app_context():
        db.create_all()

    # Configuração do Swagger UI
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "API Concessionária"},
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    # Servindo arquivos estáticos corretamente, incluindo swagger.json
    @app.route("/static/<path:filename>")
    def static_files(filename):
        return send_from_directory(app.static_folder, filename)

    return app
