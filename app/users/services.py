from .model import Users


def get_user_from_id(user_id):
    return Users.objects().get(id=user_id)
