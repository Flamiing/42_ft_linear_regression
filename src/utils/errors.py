class ErrorHandler():
    ONLY_NUM_ACCEPTED = 'Only numbers are accepted. Try again.'
    NEGATIVE_INPUT = 'Negative input is not accepted. Try again.'
    INVALID_HEADER = 'Invalid file. Header is not valid.'
    WRONG_NUM_ROWS = 'Invalid file. Wrong number of rows in csv file.'
    WRONG_NUM_COLUMNS = 'Invalid file. Wrong number of columns.'
    INVALID_THETAS = 'Invalid file. Invalid Thetas in CSV file.'
    COL_LEN_MISMATCH = 'Invalid file. There is a column length mismatch.'
    WRONG_DATA_IN_DATASET = 'Invalid file. There is unexpected data in the dataset.'

    @staticmethod
    def exit_with_error(error_msg):
        print(f'Error: {error_msg}')
        exit(1)
    
    @staticmethod
    def closed_successfully():
        print('\nProgram closed successfuly.')
        exit(0)
