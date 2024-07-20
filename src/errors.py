from enum import Enum


class ErrorMessage(Enum):
    ONLY_INT_ACCEPTED = 'Invalid input. Only integers are accepted.'
    INVALID_HEADER = 'Invalid file. Header is not valid.'
    WRONG_NUM_ROWS = 'Invalid file. Wrong number of rows in the Thetas csv file.'
    WRONG_NUM_COLUMNS = 'Invalid file. Wrong number of columns'
    INVALID_THETAS = 'Invalid file. Invalid Thetas in CSV file.'
    
    def __str__(self):
        return self.value

def exit_with_error(error_msg):
    print(f'Error: {error_msg}')
    exit(1)