import logging
import pathlib
import sys

LOG_MSG_FMT = "%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(lineno)d: %(message)s"
LOG_DATE_FMT = "%Y%b%d:%H:%M:%S"
DFLT_LOG_FILE = "prism_tank.log"


def get_logger(logger_name="prism_tank",
               log_msg_fmt=LOG_MSG_FMT,
               log_date_fmt=LOG_DATE_FMT,
               level=logging.DEBUG,
               log_file=DFLT_LOG_FILE) -> logging.Logger:
    log = logging.getLogger(logger_name)
    fmt = logging.Formatter(log_msg_fmt,
                            datefmt=log_date_fmt)
    add_sh = True
    add_fh = True

    for h in log.handlers:
        if isinstance(h, logging.StreamHandler):
            add_sh = False
        elif isinstance(h, logging.FileHandler):
            add_fh = False
    if add_sh is True and add_fh is True:
        log.setLevel(level)

    if add_sh is True:
        fh = logging.StreamHandler(stream=sys.stdout)
        fh.setLevel(level)
        fh.setFormatter(fmt)
        log.addHandler(fh)

    if add_fh is True:
        if log_file == DFLT_LOG_FILE:
            top_dir = pathlib.Path(__file__).parent.parent.parent.absolute()
            logs_file = pathlib.Path(top_dir).joinpath(f"logs/{DFLT_LOG_FILE}")
        else:
            logs_file = log_file
        fh = logging.FileHandler(filename=logs_file)
        fh.setFormatter(fmt)
        fh.setLevel(level)
        log.addHandler(fh)

    return log

