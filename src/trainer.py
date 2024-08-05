import argparse
import pathlib
import numpy as np
from pandas import read_csv
from utils.linear_regression import LinearRegression
from utils.errors import ErrorHandler
from utils.validators import validate_csv


def args_parser():
    parser = argparse.ArgumentParser(prog='trainer.py', description="Trains a linear regression model to get a set of thetas.")

    parser.add_argument('-d', '--dataset_path', type=pathlib.Path, help='Specify the path to the dataset.')
    parser.add_argument('-s', '--save_thetas', help='Save the thetas in a thetas.csv file.', action='store_true')
    parser.add_argument('-t', '--thetas_path', type=pathlib.Path, help='Specify the path where thetas.csv file will be saved.')

    args = parser.parse_args()

    if not args.dataset_path:
        parser.error('No path to a dataset specified.')
    if args.thetas_path and not args.save_thetas:
        parser.error('--thetas_path argument requires --save_thetas to be set.')

    return args

def linear_regression(args, data):
    model = LinearRegression(args.thetas_path, x=data['mileage'], y=data['price'])

    thetas = model.linear_regression(args.save_thetas)

def get_data(file_path):
    try:
        data_csv = read_csv(file_path, sep=',')
        expected_header = ['km', 'price']
        validate_csv(file_path, data_csv, expected_header)
    except Exception as e:
        ErrorHandler.exit_with_error(e)
    
    data = {
        'mileage': np.array(data_csv.km),
        'price': np.array(data_csv.price)
    }
    return data

def main():
    args = args_parser()
    data = get_data(args.dataset_path)
    linear_regression(args, data)

if __name__ == '__main__':
    main()
