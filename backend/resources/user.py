from models.user import User
from flask import Response
from flask_restful import Resource, reqparse, request
from security.jwt_initialize import jwt_required, get_jwt_identity
from services.user import UserService
from flask_mongoengine import DoesNotExist

class UserController(Resource):

    @jwt_required
    def get(self):
        args = request.args
        print(args)
        username = request.args.get('username')
        try:
            if username:
                users = UserService.buscar_por_username(username)
            else:
                users = UserService.buscar_todos()
            return Response(users, mimetype="application/json", status=200)
        except DoesNotExist:
            return {'message': 'Usuário não encontrado'}, 404