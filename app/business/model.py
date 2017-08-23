from bson import ObjectId

import mongoengine as me

from app.users.model import Users


class LaundryBranchesEmbedded(me.EmbeddedDocument):
    identifier = me.ObjectIdField(default=ObjectId)

    branch_name = me.StringField()
    address = me.StringField(required=True)
    phone = me.StringField()

    services_choices = ['laundry', 'pounds_laundry', 'tint', 'shoes']
    services = me.ListField(me.StringField(choices=services_choices))

    branch_pictures = me.ListField(me.URLField())


class SelfMachinesEmbedded(me.EmbeddedDocument):
    identifier = me.ObjectIdField(default=ObjectId)

    description = me.StringField()
    pictures = me.ListField(me.URLField())


class UserBusinessModel(me.Document):
    # Owner
    user = me.ReferenceField(Users)

    business_type_choices = ['laundries', 'self_machines']
    business_type = me.StringField(choices=business_type_choices)

    # laundries: Branches information.
    branches = me.ListField(me.EmbeddedDocumentField(LaundryBranchesEmbedded))
    # self_machines: Washing machine information
    self_machines = me.ListField(me.EmbeddedDocumentField(SelfMachinesEmbedded))
