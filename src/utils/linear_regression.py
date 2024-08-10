import os
import numpy as np
from utils.file_utils import save_to_csv


class LinearRegression():
    def __init__(self, thetas_file_path=None, x=None, y=None, learning_rate=0.1, epoch=1000):
        if x is not None and y is not None:
            self.raw_x = x
            self.raw_y = y
            self.x = np.array(self.__normalizer(x)) # Mileage in this case
            self.y = np.array(self.__normalizer(y)) # Price in this case
            self.learning_rate = learning_rate
            self.epoch = epoch
            self.path = thetas_file_path if thetas_file_path else '.'
            self.thetas = {
                'theta0': 0.0,
                'theta1': 0.0
            }

    def __estimate(self, x):
        return self.thetas['theta0'] + (self.thetas['theta1'] * x)

    def __normalizer(self, data):
        size = len(data)
        normalized_data = []

        for i in range(size):
            result = (data[i] - min(data)) / (max(data) - min(data))
            normalized_data.append(result)

        return normalized_data

    def __denormalize_thetas(self):
        max_y = max(self.raw_y)
        min_y = min(self.raw_y)
        max_x = max(self.raw_x)
        min_x = min(self.raw_x)

        self.thetas['theta1'] = self.thetas['theta1'] * (max_y - min_y) / (max_x - min_x)
        self.thetas['theta0'] = self.thetas['theta0'] * (max_y - min_y) + min_y - self.thetas['theta1'] * min_x

    def linear_regression(self, save_result):
        for _ in range(self.epoch):
            predictions = self.__estimate(self.x)
            errors = predictions - self.y

            self.thetas['theta0'] -= self.learning_rate * np.mean(errors)
            self.thetas['theta1'] -= self.learning_rate * np.mean(errors * self.x)

        self.__denormalize_thetas()
        
        if save_result:
            save_to_csv(self.path, [(self.thetas['theta0'], self.thetas['theta1'])], ['theta0', 'theta1'], 'thetas')

        return self.thetas

    def predict(self, thetas, x):
        self.thetas = thetas
        return self.__estimate(x)
