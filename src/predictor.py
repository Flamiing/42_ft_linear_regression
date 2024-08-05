import argparse
import pathlib
from pandas import read_csv
from utils.errors import ErrorHandler
from utils.linear_regression import LinearRegression
from utils.validators import validate_csv


def get_mileage():
    while True:
        try:
            mileage = float(input('Mileage: '))
            if mileage >= 0:
                return mileage
            print(ErrorHandler.NEGATIVE_INPUT)
        except ValueError:
            print(ErrorHandler.ONLY_NUM_ACCEPTED)
        except (KeyboardInterrupt, EOFError):
            print('\nProgram closed successfuly.')
            exit(0)

def get_thetas(path):
    file_path = path if path else '../data/thetas.csv'
    try:
        thetas_csv = read_csv(file_path, sep=',')
        expected_header = ['theta0', 'theta1']
        validate_csv(file_path, thetas_csv, expected_header, check_rows=True)
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

def args_parser():
    parser = argparse.ArgumentParser(prog='predictor.py', description="Predicts the price based on the specified mileage.")

    parser.add_argument('-p', '--path', type=pathlib.Path, help='Specify the path to the thetas.csv file.')
    parser.add_argument('-r', '--raw', help='Get raw price without getting it rounded.', action='store_true')

    args = parser.parse_args()

    return args

def main():
    args = args_parser()
    mileage = get_mileage()
    thetas = get_thetas(args.path)
    price_prediction = LinearRegression().predict(thetas, mileage)
    if price_prediction < 0:
        print('Predicted price is inferior than 0€')
    else:
        if args.raw:
            print(f'Predicted Price: {price_prediction}€')
        else:
            print(f'Predicted Price: {round(price_prediction, 2)}€')

if __name__ == '__main__':
    main()
