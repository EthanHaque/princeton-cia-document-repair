"""
Reads in a xlsx file and splits it into its individual sheets as csv files.
Prepends the name of the xlsx file to the sheet name to generate unique
filenames.
"""

import os
import pandas as pd
from tqdm import tqdm


def create_dfs_from_xlsx(xlsx_file_path):
    """Returns a list of dataframes from a xlsx file

    Parameters
    ----------
    xlsx_file_path : str
        Path to the xlsx file.

    Returns
    -------
    dfs : Dict
        Dictionary of dataframes, where the key is the sheet name.
    """
    dfs = pd.read_excel(xlsx_file_path, sheet_name=None)
    return dfs


def write_dfs_to_csv(dfs, xlsx_file_name, output_direcotry):
    """Writes a dictionary of dataframes to csv files.

    Parameters
    ----------
    output_direcotry : str
        Path to the output directory.
    dfs : Dict
        Dictionary of dataframes, where the key is the sheet name.
    xlsx_file_name : str
        Name of the xlsx file.
    """
    for sheet_name, df in tqdm(dfs.items()):
        csv_file_name = f"{xlsx_file_name}{sheet_name}.csv"
        csv_file_path = os.path.join(output_direcotry, csv_file_name)
        df.to_csv(csv_file_path, index=False)


if __name__ == '__main__':
    file_path = "./data/2018.xlsx"
    output_directory = "./data/split-csvs"
    file_name = os.path.basename(file_path).split(".")[0]
    dfs = create_dfs_from_xlsx(file_path)
    write_dfs_to_csv(dfs, file_name, output_directory)
