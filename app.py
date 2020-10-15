from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from log import get_logger

LOG = get_logger()
DIALECT = "sqlite"

db = SQLAlchemy()


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_path=True)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

