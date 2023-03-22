from apps.core import database
from apps.core.models import Model


class User(Model):
    first_name = database.Column(database.String)
    last_name = database.Column(database.String)

