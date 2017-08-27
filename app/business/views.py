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
        return json_response(UserBusinessSchema().dump(USER_BUSINESS_MODEL.objects(user=user.id), many=True))

    def post(self, user):
        business, error = UserBusinessSchema().load({'user': user.id, **request.json})
        if error:
            return json_response(error, HTTPStatus.BadRequest, HTTPStatus.BadRequest)
        business.save()
        return json_response(UserBusinessSchema().dump(business))


class BusinessApiView(MethodView):
    decorators = [login_jwt_required]

    def get(self, user, id):
        return json_response(UserBusinessSchema().dump(USER_BUSINESS_MODEL.objects.get(id=id, user=user.id)).data)

    def put(self, user, id):
        business_data, error = UserBusinessSchema().load(request.json, partial=True)
        if error:
            return json_response(error, HTTPStatus.BadRequest, HTTPStatus.BadRequest)
        business = USER_BUSINESS_MODEL.objects.get(id=id, user=user.id).update(**business_data)
        return json_response(UserBusinessSchema().dump(business.reload()))
