from flask import Blueprint, request, jsonify
from app.models.user import User
from flask_jwt_extended import create_access_token
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()
    
    if user and user.check_password(data.get('senha')):  # Changed from 'password' to 'senha'
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Credenciais inválidas"}), 401