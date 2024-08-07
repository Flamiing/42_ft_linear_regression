import matplotlib.pyplot as plt
import numpy as np
from utils.linear_regression import LinearRegression
from utils.errors import ErrorHandler


class DataPlotter():

    def __init__(self, x, y, thetas):
        self.x = x
        self.y = y
        self.thetas = thetas

        self.__setup_graph()

    def __setup_graph(self):
        plt.scatter(self.x, self.y, color='blue', label='Data Points')
        
        y_values = LinearRegression().predict(self.thetas, self.x)
        plt.plot(self.x, y_values, color='r', label='Regression Line')
        
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.title('Linear Regression')
        
        plt.legend()

    def show(self):
        try:
            plt.show()
        except KeyboardInterrupt:
            ErrorHandler.closed_successfully()
