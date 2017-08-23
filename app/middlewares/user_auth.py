from functools import wraps

from flask import jsonify, request
import jwt

from app.users.services import get_user_from_id


def login_jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        jwtBody = jwt.decode(request.headers.get('Authorization'), 'secret', algorithms=['HS256'])
        return f(user=get_user_from_id(jwtBody['user_id']), *args, **kwargs)
    return decorated_function
