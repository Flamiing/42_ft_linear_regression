import numpy as np


class LinearRegression():

    def __init__(self, x=None, y=None, num_iterations=None, learning_rate=None):
        self.x = np.array(x) # Mileage in this case
        self.y = np.array(y) # Price in this case
        self.learning_rate = learning_rate
        self.thetas = {
            'theta0': 0.0,
            'theta1': 0.0
        }
        self.num_iterations = num_iterations # Number of training examples
    
    def __estimate(self, x):
        return self.thetas['theta0'] + (self.thetas['theta1'] * x)
    
    def __mean(self, values):
        return sum(values) / len(values)
    
    def __calculate_gradient0(self, predictions):
        return self.learning_rate * sum(predictions - self.y) / self.num_iterations

    def __calculate_gradient1(self, predictions):
        return self.learning_rate * sum((predictions - self.y) * self.x) / self.num_iterations
    
    def linear_regression(self):
        tmp_thetas = {
            'theta0': 0.0,
            'theta1': 0.0
        }
        
        for _ in range(self.num_iterations):
            predictions = self.__estimate(self.x)
            
            tmp_thetas['theta0'] = self.__calculate_gradient0(predictions)
            tmp_thetas['theta1'] = self.__calculate_gradient1(predictions)
            
            self.thetas['theta0'] -= tmp_thetas['theta0']
            self.thetas['theta1'] -= tmp_thetas['theta1']
        
        return self.thetas

    def predict(self, thetas, x):
        self.thetas = thetas
        return self.__estimate(x)