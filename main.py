import os.path
import sys
from functions.files import import_from_dir
from functions.projlog import log
import click_log
import click
import pandas as pd

logger = log("logs")
pd.set_option("display.max_columns", None)


@click.command()
@click.argument("directory")
@click.argument("output")
@click_log.simple_verbosity_option(logger)
def main(directory: "input", output: "output"):
    fullpath = os.path.abspath(directory)
    logger.debug(f"Reading files in {fullpath}")
    input_files = import_from_dir(directory)
    input_files = input_files.sort_values(["timestamp"], ascending=False)
    input_files = input_files.groupby(["id"]).first()
    input_files.to_csv(f"{output}/id_descriptions.csv")
    print(input_files)
    return input_files


if __name__ == "__main__":
    main()
