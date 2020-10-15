from pathlib import PurePath

from flask import g, current_app
from flask_sqlalchemy import SQLAlchemy

from util import get_top_dir





def get_db():
    if 'db' not in g:
        dialect = current_app.config["DB_DIALECT"]
        if dialect == "sqlite":
            engine = SQLAlchemy.create_engine(f'sqlite:////{get_local_db_path()}')
            g.db = engine
        else:
            raise ValueError(f"invalid db dialect in config: {dialect}")

