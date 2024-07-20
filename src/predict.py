from pandas import read_csv
from errors import exit_with_error, ErrorMessage


def main():
    mileage = get_mileage()
    thetas = get_thetas()
    print(thetas)
    # If Valid read thetas and calculate
    
def get_mileage():
    try:
        mileage = int(input('Mileage: '))
        return mileage
    except ValueError:
        exit_with_error(ErrorMessage.ONLY_INT_ACCEPTED)

def validate_csv(csv_file):
    EXPECTED_HEADER = ['theta0', 'theta1']
    NUM_COLUMNS = 2
    
    if list(csv_file.columns) != EXPECTED_HEADER:
        exit_with_error(ErrorMessage.INVALID_HEADER)
        
    with open('../data/thetas.csv', mode='r') as csv_file:
        num_rows = 0
        for row_index, row in enumerate(csv_file):
            num_rows += 1
            if row_index > 2:
                exit_with_error(ErrorMessage.WRONG_NUM_ROWS)
            columns = row.strip().split(',')
            if len(columns) > NUM_COLUMNS:
                exit_with_error(ErrorMessage.WRONG_NUM_COLUMNS)
        
        if num_rows != 2:
            exit_with_error(ErrorMessage.WRONG_NUM_ROWS)

def get_thetas():
    try:
        thetas_csv = read_csv('../data/thetas.csv', sep=',')
        validate_csv(thetas_csv)
    except Exception as e:
        exit_with_error(e)
    
    try:
        theta_zero = int(thetas_csv.theta0.values[0])
        theta_one = int(thetas_csv.theta1.values[0])
    except (ValueError, IndexError):
        exit_with_error(ErrorMessage.INVALID_THETAS)
    thetas = {
            'theta0': theta_zero,
            'theta1': theta_one
        }
    return thetas

if __name__ == '__main__':
    main()
