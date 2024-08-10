import argparse
import pathlib
from utils.url import URL
from utils.scraper import Scraper
from utils.errors import ErrorHandler
from utils.file_utils import save_to_csv


def args_parser():
    parser = argparse.ArgumentParser(prog='dataset_generator.py', description="Generates a dataset.")

    parser.add_argument('-p', '--path', type=pathlib.Path, help='Specify the path where the new dataset will be saved.')
    parser.add_argument('-n', '--num_data_points', type=int, help='Specify the number of data points wanted.', default=0)

    args = parser.parse_args()

    return args

def scraping(args):
    url = URL('https://www.coches.com/coches-segunda-mano/coches-ocasion.htm')

    scraper = Scraper(url, args.num_data_points)
    try: 
        data_points = scraper.scrap()
    except (KeyboardInterrupt, EOFError):
        ErrorHandler.close_successfully()

    save_to_csv(args.path, data_points, columns=['km', 'price'])

def main():
    args = args_parser()
    scraping(args)

if __name__ == '__main__':
    main()
