import argparse
import pathlib
from utils.linear_regression import LinearRegression
from utils.data_plotter import DataPlotter
from utils.file_utils import get_data


def args_parser():
    parser = argparse.ArgumentParser(prog='trainer.py', description="Trains a linear regression model to get a set of thetas.")

    parser.add_argument('-d', '--dataset_path', type=pathlib.Path, help='Specify the path to the dataset.')
    parser.add_argument('-s', '--save_thetas', help='Save the thetas in a thetas.csv file.', action='store_true')
    parser.add_argument('-t', '--thetas_path', type=pathlib.Path, help='Specify the path where thetas.csv file will be saved.')
    parser.add_argument('--show_data', help='Use this flag to plot the data into a graph.', action='store_true')

    args = parser.parse_args()

    if not args.dataset_path:
        parser.error('No path to a dataset specified.')
    if args.thetas_path and not args.save_thetas:
        parser.error('--thetas_path argument requires --save_thetas to be set.')

    return args

def linear_regression(args, data):
    model = LinearRegression(args.thetas_path, x=data['x'], y=data['y'])
    thetas = model.linear_regression(args.save_thetas)
    return thetas

def main():
    args = args_parser()
    data = get_data(args.dataset_path)
    thetas = linear_regression(args, data)
    if args.show_data:
        data_plotter = DataPlotter(data['x'], data['y'], thetas)
        data_plotter.show()

if __name__ == '__main__':
    main()
