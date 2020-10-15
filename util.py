import pathlib


def get_top_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent.parent.absolute()


def get_local_db_path() -> pathlib.PurePath:
    top_path = get_top_dir()
    db_file_path = top_path.joinpath("data/sqlite.db")
    return db_file_path

# END OF FILE
