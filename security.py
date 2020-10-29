
from werkzeug.security import safe_str_cmp
from functools import wraps
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

def checkuser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_identity.username == 'user1':
            return func(*args, **kwargs)
        return {'message': "user not allowed "}, 401
    return wrapper