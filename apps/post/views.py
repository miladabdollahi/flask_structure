from flask import Blueprint

from apps import app


user = Blueprint(
    'user', __name__, url_prefix='/users'
)


@user.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(user)
