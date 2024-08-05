import pandas as pd
from utils.errors import ErrorHandler


def validate_csv(csv_path, csv_file, expected_header, check_rows=False):
    NUM_COLUMNS = 2
    
    if list(csv_file.columns) != expected_header:
        ErrorHandler.exit_with_error(ErrorHandler.INVALID_HEADER)

    with open(csv_path, mode='r', encoding='utf-8') as file:
        num_rows = 0
        for row_index, row in enumerate(file):
            num_rows += 1
            if check_rows and row_index > 2:
                ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_ROWS)
            columns = row.strip().split(',')
            if len(columns) > NUM_COLUMNS:
                ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_COLUMNS)
        
        if check_rows and num_rows != 2:
            ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_ROWS)
        
        if csv_file[csv_file.columns[0]].count() != csv_file[csv_file.columns[1]].count():
            ErrorHandler.exit_with_error(ErrorHandler.COL_LEN_MISMATCH)
