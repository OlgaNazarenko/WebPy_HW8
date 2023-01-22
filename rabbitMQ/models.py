from mongoengine import Document, StringField, BooleanField


class Contacts(Document):
    fullname = StringField(max_length=50, required=True)
    email = StringField()
    status = BooleanField(default=False)
