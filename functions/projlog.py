import logging
import datetime


def log(logdir: str):
    # Create custom logger logging all five levels
    logger = logging.getLogger(logdir)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Define format for logs
    fmt = "%(asctime)s | %(levelname)8s | %(message)s"

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)

    # Create file handler for logging to a file (logs all five levels)
    today = datetime.date.today()
    log_path = "{}/my_app_{}.log".format(logdir, today.strftime("%Y_%m_%d"))
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(fmt))

    # Add both handlers to the logger
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger
