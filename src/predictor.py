import argparse
import pathlib
from utils.errors import ErrorHandler
from utils.linear_regression import LinearRegression
from utils.file_utils import get_thetas


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
            ErrorHandler.close_successfully()

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
