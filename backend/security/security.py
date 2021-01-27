#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from werkzeug.security import safe_str_cmp
from services.user import UserService
from flask_mongoengine import DoesNotExist

import json

def authenticate(username, password):
    try:
        user_json = UserService.buscar_por_username(username)
        user = json.loads(user_json)
        if user and safe_str_cmp(user['password'], password):
            return user
        else:
            return None
    except DoesNotExist:
        return None