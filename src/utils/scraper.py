import requests
import re
import numpy as np
from tqdm import tqdm
from bs4 import BeautifulSoup
from utils.errors import ErrorHandler


class Scraper():
    KM_STRING = re.compile('km')
    PRICE_STRING = re.compile('€')
    
    def __init__(self, url, num_data_points):
        self.url = url
        self.num_dp = num_data_points if num_data_points > 0 else 25
        self.count_dp = 0
        self.data_points = []
        self.pbar = tqdm(total=self.num_dp, bar_format='{l_bar}{bar}{r_bar}', colour='green')

    def scrap(self):
        while self.count_dp != self.num_dp:
            self.__get_all_cars_from_page()
            self.url.next_page()

        return self.data_points
        
    def __get_all_cars_from_page(self):
        scraped_html = self.__extract_hmtl()
        
        raw_cars = scraped_html.find('div', class_='Grid-module_grid__h49fk ResultsCardGrid_searcher-classified-card-grid__3q2mR')
        for car in raw_cars:
            if self.count_dp == self.num_dp or not car or car.text == 'Publicidad':
                break
            raw_km = car.find('span', string=self.KM_STRING).text.split()[0].replace('.', '')
            raw_price = car.find('strong', string=self.PRICE_STRING).text.split()[0].replace('.', '')
            try: 
                km = int(raw_km) if int(raw_km) >= 0 else 0
                price = int(raw_price) if int(raw_price) >= 0 else 0
                self.data_points.append((km, price))
            except Exception as e:
                ErrorHandler.exit_with_error(e)
            self.count_dp += 1
            self.pbar.update(1)
    
    def __extract_hmtl(self):
        req = requests.get(self.url)
        
        if req.status_code >= 400:
            ErrorHandler.exit_with_error(f'Extracting HTML failed with status code {str(req.status_code)} using URL: {self.url}')

        return BeautifulSoup(req.text, 'lxml')
