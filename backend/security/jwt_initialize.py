from flask_jwt import JWT, jwt_required, JWTError
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)

jwt = JWTManager()

def initialize_jwt(app):
    jwt.init_app(app)