from util import get_local_db_path

DB_DIALECT = "sqlite"
SQLALCHEMY_DATABASE_URI = f"sqlite:////{get_local_db_path()}"
