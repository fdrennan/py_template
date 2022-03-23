import os.path
import sys
from functions.files import import_from_dir
from functions.projlog import mylog
import click_log
import click

logger = mylog("logs")


@click.command()
@click.argument("directory")
@click_log.simple_verbosity_option(logger)
def main(directory: "input"):
    fullpath = os.path.abspath(directory)
    logger.debug(f"Reading files in {fullpath}")
    input_files = import_from_dir(directory)
    if input_files is None:
        logger.warning(f"No files in {directory}")
        sys.exit()


if __name__ == "__main__":
    main()
