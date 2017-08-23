from http import HTTPStatus

from flask import request
from flask.views import MethodView

from app.middlewares.responses import json_response
from .serializers import UserBusinessSchema

from app.middlewares.user_auth import login_jwt_required


USER_BUSINESS_MODEL = UserBusinessSchema.Meta.model


class BusinessListView(MethodView):
    """

    """
    decorators = [login_jwt_required]

    def get(self, user):
        return UserBusinessSchema().dump(USER_BUSINESS_MODEL.objects.get(user=user.id))

    def post(self, user):
        business, error = UserBusinessSchema().load({'user': user, **request.json})
        if error:
            return json_response(error, HTTPStatus.BadRequest, HTTPStatus.BadRequest)

