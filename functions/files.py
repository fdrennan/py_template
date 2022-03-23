import os
import sys
import pandas as pd
from functions.projlog import mylog

logger = mylog("logs")


def read_pd(filename: str) -> pd.DataFrame:
    logger.debug(f"Reading in {filename}")
    df = pd.read_csv(filename)
    return df


def import_from_dir(dir_path: "input") -> pd.DataFrame:
    csv_files = os.listdir(dir_path)
    if csv_files is None:
        sys.exit()
    input_files = [os.path.join(dir_path, file) for file in csv_files]
    files = (read_pd(file) for file in input_files)
    files = pd.concat(files)
    logger.info(f"Input shape {files.shape}")
    return files
