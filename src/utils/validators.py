from utils.errors import ErrorHandler


def validate_csv(csv_file, expected_header, check_rows=False):
    NUM_COLUMNS = 2
    
    if list(csv_file.columns) != expected_header:
        ErrorHandler.exit_with_error(ErrorHandler.INVALID_HEADER)

    with open('../data/thetas.csv', mode='r', encoding='utf-8') as file:
        num_rows = 0
        for row_index, row in enumerate(file):
            num_rows += 1
            if row_index > 2:
                ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_ROWS)
            columns = row.strip().split(',')
            if len(columns) > NUM_COLUMNS:
                ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_COLUMNS)
        
        if check_rows and num_rows != 2:
            ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_ROWS)
