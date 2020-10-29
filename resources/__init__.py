from functools import wraps
from flask_jwt import jwt_required ,current_identity

def checkuser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_identity.username == args[1]:
            return func(*args, **kwargs)
        return {'message': "user not allowed "}, 401
    return wrapper