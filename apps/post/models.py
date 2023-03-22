from apps.core import database
from apps.core.models import Model


class Post(Model):
    title = database.Column(database.String)
    name = database.Column(database.CHAR)
