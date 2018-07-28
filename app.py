import os
import connexion

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver

def configure(binder: Binder) -> Binder:
    binder.bind(

    )

    return binder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('rest.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=9090)
