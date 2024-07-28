class LinearRegression():

    def __init__(self, x=[], y=[], m=None, learning_rate=None):
        self.x = self.__normalizer(x) # Mileage in this case
        self.y = self.__normalizer(y) # Price in this case
        self.learning_rate = learning_rate
        self.thetas = {
            'theta0': 0.0,
            'theta1': 0.0
        }
        self.m = m # Number of training examples

    def __estimate(self, x):
        return self.thetas['theta0'] + (self.thetas['theta1'] * float(x))

    def __normalizer(self, dataset):
        size = len(dataset)
        normalized_dataset = []

        for i in range(size):
            result = (dataset[i] - min(dataset)) / (max(dataset) - min(dataset))
            normalized_dataset.append(result)

        return normalized_dataset

    def __get_gradient0(self):
        summation = 0.0
        
        for i in range(self.m):
            summation += self.__estimate(float(self.x[i])) - float(self.y[i])
        
        result = self.learning_rate * (1 / self.m * summation)
        return result
    
    def __get_gradient1(self):
        summation = 0.0
        
        for i in range(self.m):
            summation += (self.__estimate(float(self.x[i])) - float(self.y[i])) * float(self.x[i])
        
        result = self.learning_rate * (1 / self.m * summation)
        return result

    def linear_regression(self):
        tmp_thetas = {
            'theta0': 0.0,
            'theta1': 0.0
        }

        for _ in range(self.m):
            tmp_thetas['theta0'] = self.__get_gradient0()
            tmp_thetas['theta1'] = self.__get_gradient1()

            self.thetas['theta0'] -= tmp_thetas['theta0']
            self.thetas['theta1'] -= tmp_thetas['theta1']

        return self.thetas

    def predict(self, thetas, x):
        self.thetas = thetas
        return self.__estimate(x)
