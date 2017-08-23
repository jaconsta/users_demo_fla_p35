from http import HTTPStatus

from flask import jsonify


def json_response(message, code=HTTPStatus.OK, status=HTTPStatus.OK):
    response = {
        'message': message,
        'code': code}
    return jsonify(response), status
