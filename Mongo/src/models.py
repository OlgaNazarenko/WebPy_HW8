from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField


class Authors(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=100)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors, reverse_delete_rule='DENY')
    quote = StringField()
    meta = {'allow_inheritance': True}
