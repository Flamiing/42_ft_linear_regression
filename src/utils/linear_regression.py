class LinearRegression():

    def __init__(self, x=None, y=None, m=None, learning_rate=None):
        self.x = x # Mileage in this case
        self.y = y # Price in this case
        self.learning_rate = learning_rate
        self.thetas = {
            'theta0': 0,
            'theta1': 0
        }
        self.m = m # Number of training examples
    
    def __estimate(self, x):
        return self.thetas['theta0'] + (self.thetas['theta1'] * x)
    
    def __calculate_gradient0(self, prediction, y):
        return self.learning_rate * (prediction - y)

    def __calculate_gradient1(self, prediction, x, y):
        return self.learning_rate * (prediction - y) * x
    
    def linear_regression(self):
        for i in range(self.m):
            prediction = self.__estimate(self.x[i])
            
            self.thetas['theta0'] = self.__calculate_gradient0(prediction, self.y[i])
            self.thetas['theta1'] = self.__calculate_gradient1(prediction, self.y[i], self.x[i])
        
        return self.thetas

    def predict(self, thetas, x):
        self.thetas = thetas
        return self.__estimate(x)