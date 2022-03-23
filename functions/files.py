import os
import sys
import pandas as pd
from functions.projlog import log

logger = log("logs")


def read_csv_proj(filename: str) -> pd.DataFrame:
    logger.debug(f"Reading in {filename}")
    df = pd.read_csv(filename)
    df = df.assign(source_filename=filename)
    return df


def import_from_dir(dir_path: "input") -> pd.DataFrame:
    csv_files = os.listdir(dir_path)
    print(csv_files)
    if len(csv_files) == 0:
        logger.warning("No files to read")
        sys.exit()
    input_files = [os.path.join(dir_path, file) for file in csv_files]
    files = (read_csv_proj(file) for file in input_files)
    files = pd.concat(files)
    logger.info(f"Input shape {files.shape}")
    return files
