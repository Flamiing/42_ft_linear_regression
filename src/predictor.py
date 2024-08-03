import sys
from pandas import read_csv
from utils.errors import ErrorHandler
from utils.linear_regression import LinearRegression


def get_mileage():
    while True:
        try:
            mileage = float(input('Mileage: '))
            if mileage >= 0:
                return mileage
            print(ErrorHandler.NEGATIVE_INPUT)
        except ValueError:
            print(ErrorHandler.ONLY_NUM_ACCEPTED)

def validate_csv(csv_file):
    EXPECTED_HEADER = ['theta0', 'theta1']
    NUM_COLUMNS = 2

    if list(csv_file.columns) != EXPECTED_HEADER:
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

        if num_rows != 2:
            ErrorHandler.exit_with_error(ErrorHandler.WRONG_NUM_ROWS)

def get_thetas():
    try:
        thetas_csv = read_csv('../data/thetas.csv', sep=',')
        validate_csv(thetas_csv)
    except Exception as e:
        ErrorHandler.exit_with_error(e)

    try:
        theta_zero = float(thetas_csv.theta0.values[0])
        theta_one = float(thetas_csv.theta1.values[0])
    except (ValueError, IndexError):
        ErrorHandler.exit_with_error(ErrorHandler.INVALID_THETAS)
    thetas = {
            'theta0': theta_zero,
            'theta1': theta_one
        }
    return thetas

def main():
    mileage = get_mileage()
    thetas = get_thetas()
    price_prediction = LinearRegression().predict(thetas, mileage)
    if price_prediction < 0:
        print('Predicted price is inferior than 0€')
    else:
        if len(sys.argv) > 1 and sys.argv[1] in ['-r', '--raw']:
            print(f'Predicted Price: {price_prediction}€')
        else:
            print(f'Predicted Price: {round(price_prediction, 2)}€')

if __name__ == '__main__':
    main()
