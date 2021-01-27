#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import timedelta

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWTError
from flask_cors import CORS

from security.jwt_initialize import initialize_jwt
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': 'example'
}

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token_cookie'
app.config['JWT_REFRESH_COOKIE_NAME'] = 'refresh_token_cookie'
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=5)
app.config['JWT_ALGORITHM'] = 'HS512'
app.config['JWT_DECODE_ALGORITHMS'] = ['HS512', 'HS256']
app.secret_key = os.environ['JWT_SECRET_KEY']
CORS(app, supports_credentials=True)

initialize_jwt(app)
initialize_db(app)
initialize_routes(api)

@app.errorhandler(JWTError)
def auth_error_handler(err):
    return jsonify({'message': 'Usuário não autorizado.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
