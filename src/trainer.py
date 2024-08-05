import argparse
import pathlib
from utils.linear_regression import LinearRegression


def args_parser():
    parser = argparse.ArgumentParser(prog='trainer.py', description="Trains a linear regression model to get a set of thetas.")

    parser.add_argument('-s', '--save_thetas', help='Save the thetas in a thetas.csv file.', action='store_true')
    parser.add_argument('-p', '--path', type=pathlib.Path, help='Specify the path where thetas.csv file will be saved.')
    parser.add_argument('-d', '--dataset', type=pathlib.Path, help='Specify the path to the dataset.')

    args = parser.parse_args()

    if args.path and not args.save_thetas:
        parser.error('--path argument requires --save_thetas to be set.')

    return args

def linear_regression(args):
    DATA = [
        (240000, 3650),
        (139800, 3800),
        (150500, 4400),
        (185530, 4450),
        (176000, 5250),
        (114800, 5350),
        (166800, 5800),
        (89000, 5990),
        (144500, 5999),
        (84000, 6200),
        (82029, 6390),
        (63060, 6390),
        (74000, 6600),
        (97500, 6800),
        (67000, 6800),
        (76025, 6900),
        (48235, 6900),
        (93000, 6990),
        (60949, 7490),
        (65674, 7555),
        (54000, 7990),
        (68500, 7990),
        (22899, 7990),
        (61789, 8290)
    ]

    mileage = [240000, 139800, 150500, 185530, 176000, 114800, 166800, 89000, 144500, 84000, 82029, 63060, 74000, 97500, 67000, 76025, 48235, 93000, 60949, 65674, 54000, 68500, 22899, 61789]
    price = [3650, 3800, 4400, 4450, 5250, 5350, 5800, 5990, 5999, 6200, 6390, 6390, 6600, 6800, 6800, 6900, 6900, 6990, 7490, 7555, 7990, 7990, 7990, 8290]

    model = LinearRegression(args.path, x=mileage, y=price)

    thetas = model.linear_regression(args.save_thetas)

def main():
    args = args_parser()
    
    linear_regression(args)

if __name__ == '__main__':
    main()
