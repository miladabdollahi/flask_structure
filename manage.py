import os.path
from importlib import import_module

import typer

from alembic import command
from alembic.config import Config

from apps import app, balerin

config = Config('alembic.ini')

manager = typer.Typer()


@manager.command(name='make-migrations')
def make_migrations(revision_id: str = None):
    config.balerin = balerin
    if not os.path.exists('migrations'):
        command.init(config, 'migrations')

    packages = config.balerin.get_loaded_packages()
    for package in packages:
        try:
            import_module('{package}.models'.format(package=package))
        except ImportError:
            pass

    command.revision(config, autogenerate=True, rev_id=revision_id)


@manager.command()
def upgrade(revision: str = 'head'):
    command.upgrade(config, revision)


@manager.command()
def downgrade(revision: str = 'head'):
    command.downgrade(config, revision)


@manager.command(name='runserver')
def runserver(uri: str):
    host, port = uri.split(':')
    app.run(host, port)


if __name__ == '__main__':
    import configs

    app.config.from_mapping(configs.DATABASES)
    balerin.load_components()
    manager()
