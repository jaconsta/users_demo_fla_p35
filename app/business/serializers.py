from marshmallow_mongoengine import ModelSchema

from .model import UserBusinessModel


class UserBusinessSchema(ModelSchema):
    class Meta:
        model = UserBusinessModel


