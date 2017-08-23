import mongoengine as me
from werkzeug.security import generate_password_hash, check_password_hash


class Users(me.Document):
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)

    firstName = me.StringField()
    lastName = me .StringField()

    city = me.StringField()
    country = me.StringField()
    phone = me.IntField()

    isBusiness = me.BooleanField(default=False)
    businessTypePicked = me.StringField()
    isApproved = me.BooleanField(default=False)

    def hash_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
