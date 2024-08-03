class ErrorHandler():
    ONLY_NUM_ACCEPTED = 'Only numbers are accepted. Try again.'
    NEGATIVE_INPUT = 'Negative input is not accepted. Try again.'
    INVALID_HEADER = 'Invalid file. Header is not valid.'
    WRONG_NUM_ROWS = 'Invalid file. Wrong number of rows in the Thetas csv file.'
    WRONG_NUM_COLUMNS = 'Invalid file. Wrong number of columns.'
    INVALID_THETAS = 'Invalid file. Invalid Thetas in CSV file.'

    @staticmethod
    def exit_with_error(error_msg):
        print(f'Error: {error_msg}')
        exit(1)
