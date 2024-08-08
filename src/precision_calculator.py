import argparse
import pathlib
import math
import numpy as np
from utils.file_utils import get_thetas, get_data
from utils.linear_regression import LinearRegression


def args_parser():
    parser = argparse.ArgumentParser(prog='predictor.py', description="Predicts the price based on the specified mileage.")

    parser.add_argument('-d', '--dataset_path', type=pathlib.Path, help='Specify the path to the dataset.')
    parser.add_argument('-t', '--thetas_path', type=pathlib.Path, help='Specify the path to the thetas file.')
    parser.add_argument('-r', '--raw', help='Get the raw result of the calculations.', action='store_true')

    args = parser.parse_args()
    
    if not args.dataset_path or not args.thetas_path:
        parser.error('A path to the thetas and dataset files must be specified.')

    return args

def calculate_precision(thetas, data):
    predictions = LinearRegression().predict(thetas, data['x'])
    residuals = data['y'] - predictions
    y_mean = np.mean(data['y'])

    mse = np.mean(residuals ** 2) # Mean Squared Error
    rmse = math.sqrt(mse) # Root Mean Squared Error
    r_squared = 1 - ((np.sum(residuals ** 2)) / (np.sum((data['y'] - y_mean) ** 2)))

    results = {
        'mse': mse,
        'rmse': rmse,
        'r_squared': r_squared
    }

    return results

def print_result(result, raw_mode=False):
    if not raw_mode:
        result['mse'] = round(result['mse'], 2)
        result['rmse'] = round(result['rmse'], 2)
        result['r_squared'] = round(result['r_squared'] * 100, 2)
    else:
        result['r_squared'] *= 100
        
    print(f'''
ALGORITHM PRECISION:

    - Mean Square Error: {result['mse']}
    - Root Mean Square Error: {result['rmse']}
    - R-Squared: {result['r_squared']}
    
    The precission of your model is {result['r_squared']}%
          ''')

def main():
    args = args_parser()
    thetas = get_thetas(args.thetas_path)
    data = get_data(args.dataset_path)
    
    result = calculate_precision(thetas, data)
    print_result(result, args.raw)

if __name__ == '__main__':
    main()