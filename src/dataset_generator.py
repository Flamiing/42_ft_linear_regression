import math
import argparse
import pathlib
import numpy as np
from tqdm import tqdm
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

def scraping(num_data_points):
    url = URL('https://www.coches.com/coches-segunda-mano/citroen-c4.htm')

    scraper = Scraper(url, num_data_points)
    try:
        dataset = scraper.scrap()
    except (KeyboardInterrupt, EOFError):
        ErrorHandler.close_successfully()

    return dataset

def z_score(data_point, all_data_points):
    mean = np.mean(all_data_points)
    std_deviation = math.sqrt(np.mean((all_data_points - mean) ** 2))

    z_score = (data_point - mean) / std_deviation
    return z_score

def get_lower_and_upper_bound(q1, q3, iqr):
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return lower_bound, upper_bound

def interquartile_range(dataset):
    kms = [tup[0] for tup in dataset]
    prices = [tup[1] for tup in dataset]
    kms.sort()
    prices.sort()
    new_dataset = []

    q1_km = np.median(kms[:int(len(kms) / 2)])
    q1_price = np.median(prices[:int(len(prices) / 2)])

    q3_km = np.median(kms[int(len(kms) / 2):])
    q3_price = np.median(prices[int(len(prices) / 2):])

    iqr_km = q3_km - q1_km
    iqr_price = q3_price - q1_price

    lower_bound_km, upper_bound_km = get_lower_and_upper_bound(q1_km, q3_km, iqr_km)
    lower_bound_price, upper_bound_price = get_lower_and_upper_bound(q1_price, q3_price, iqr_price)

    for index, (km, price) in enumerate(dataset):
        if km > lower_bound_km and km < upper_bound_km \
            and price > lower_bound_price and price < upper_bound_price:
            new_dataset.append(dataset[index])

    return new_dataset

def clean_dataset(dataset):
    kms = np.array([tup[0] for tup in dataset])
    prices = np.array([tup[1] for tup in dataset])
    new_dataset = []

    for index, (km, price) in enumerate(dataset):
        km_z_score = z_score(km, np.array(kms))
        price_z_score = z_score(price, np.array(prices))

        if km_z_score >= -3 and km_z_score <= 3 and price_z_score >= -3 and price_z_score <= 3 \
            and dataset[index] not in new_dataset and price < 28000:
            new_dataset.append(dataset[index])

    new_dataset = interquartile_range(new_dataset)

    return new_dataset

def optimize_dataset(dataset):
    iterations = 100
    pbar = tqdm(total=iterations, desc='Optimizing Dataset', bar_format='{l_bar}{bar}{r_bar}', colour='green')
    for i in range(iterations):
        dataset_len = len(dataset)
        dataset = clean_dataset(dataset)
        if dataset_len == len(dataset):
            pbar.update(iterations - i)
            break
        pbar.update(1)
    pbar.close()

    return dataset

def main():
    args = args_parser()
    dataset = scraping(args.num_data_points)

    dataset = optimize_dataset(dataset)

    save_to_csv(args.path, dataset, columns=['km', 'price'])

if __name__ == '__main__':
    main()
