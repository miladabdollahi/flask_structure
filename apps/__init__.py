import os

from flask import Flask
from balerin import PackagingManager


app = Flask('flaskProject')
working_directory = os.path.abspath(os.getcwd())
root_package = os.path.join(working_directory, __name__)
balerin = PackagingManager(
    root_package, context=dict(important=True, app=app), ignored_packages='apps.core'
)
