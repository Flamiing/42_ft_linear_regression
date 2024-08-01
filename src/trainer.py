from utils.linear_regression import LinearRegression
import matplotlib.pyplot as plt


def main():
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

    model = LinearRegression(mileage, price, len(DATA), 0.1)

    thetas = model.linear_regression()

    print(thetas)
    
    
    # MAKE GRAPH
    plt.scatter(mileage, price, color='blue', label='Data Points')

    x_values = range(min(mileage), max(mileage))
    y_values = [thetas['theta0'] + thetas['theta1'] * x for x in x_values]
    plt.plot(x_values, y_values, color='red', label='Regression Line')

    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Linear Regression of Car Prices based on Mileage')
    plt.legend()

    plt.show()

if __name__ == '__main__':
    main()