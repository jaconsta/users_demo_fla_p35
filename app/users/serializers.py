from marshmallow_mongoengine import ModelSchema

from .model import Users


class UserSchema(ModelSchema):
    class Meta:
        model = Users
        model_fields_kwargs = {'password': {'load_only': True}}


class LoginSchema(ModelSchema):
    class Meta:
        model = Users
        fields = ('email', 'password')
