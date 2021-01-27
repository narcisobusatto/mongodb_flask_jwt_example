from resources.login import LoginAuth, LoginRefresh, LoginRemove
from resources.user import UserController


def initialize_routes(api):
    api.add_resource(UserController, '/api/users')

    api.add_resource(LoginAuth, '/api/token/auth')
    api.add_resource(LoginRefresh, '/api/token/refresh')
    api.add_resource(LoginRemove, '/api/token/remove')