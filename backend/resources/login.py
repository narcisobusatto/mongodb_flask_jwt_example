from flask_restful import Resource
from flask import jsonify, request
from security.jwt_initialize import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
from security.security import authenticate


class LoginAuth(Resource):

    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user = authenticate(username, password)
        if user is None:
            resp = jsonify({'login': False})
            resp.status_code = 200
            unset_jwt_cookies(resp)
            return resp

        access_token = create_access_token(identity=user['username'])
        refresh_token = create_refresh_token(identity=user['username'])

        resp = jsonify({'login': True})
        resp.status_code = 200
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        return resp

class LoginRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        resp = jsonify({'refresh': True})
        resp.status_code = 200
        set_access_cookies(resp, access_token)
        return resp

class LoginRemove(Resource):

    def post(self):
        resp = jsonify({'logout': True})
        resp.status_code = 200
        unset_jwt_cookies(resp)
        return resp