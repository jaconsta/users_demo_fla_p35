from http import HTTPStatus

from flask import request, jsonify
from flask.views import MethodView
import jwt
from mongoengine import NotUniqueError

from .serializers import UserSchema, LoginSchema


class UserApiView(MethodView):
    """
    Manage todo's based on their _id.
    """

    def get(self, id):
        """
        Find and return the User item.
        :param id: UUID of the database.
        :return: TODO object
        """
        user = UserSchema.Meta.model.objects().get(pk=id)
        return jsonify(UserSchema().dump(user))


class UserApiListView(MethodView):
    """
    Manage the creation and listing of users.
    """
    def get(self):
        """
        Get all users.
        Not implemented due to access rights.
        :return: (List) users.
        ---
        """
        return jsonify(UserSchema().dump(UserSchema.Meta.model.objects(), many=True))

    def post(self):
        """
        Create a new user.
        :return: User object.
        ---
        """
        user_data, errors = UserSchema().load(request.json)
        if errors:
            return jsonify(errors)
        user_data.hash_password()
        try:
            user_data.save()
        except NotUniqueError as e:
            return jsonify({'message': ['User already exists.']}), HTTPStatus.BAD_REQUEST

        return jsonify(UserSchema().dump(user_data))


class LoginApiView(MethodView):
    """
    Login the user.
    """
    def post(self):
        """
        Authenticate the user.
        Currently return users _id as access_token, though an access_token is required.
        """
        if not request.json:
            return jsonify({'errors': ['Data is not JSON']}), HTTPStatus.BAD_GATEWAY
        try:
            login_data, errors = LoginSchema().load(request.json)
        except Exception as e:
            return jsonify({'errors': [str(e)]}), HTTPStatus.BAD_REQUEST
        if errors:
            return jsonify(errors), HTTPStatus.BAD_REQUEST
        # Find and validate user credentials.
        user = LoginSchema.Meta.model.objects(email=login_data['email']).first()
        if not user or not user.check_password(login_data['password']):
            return jsonify({'error': 'Invalid credentials'}), HTTPStatus.BAD_REQUEST

        token = jwt.encode({'user_id': str(user.pk)}, 'secret', algorithm='HS256').decode('UTF-8')
        return jsonify({'token': token})  # {'token': str(user.pk)}
