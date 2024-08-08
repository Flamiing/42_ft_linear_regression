import numpy as np
from pandas import read_csv
from utils.validators import validate_csv
from utils.errors import ErrorHandler


def get_thetas(path):
    file_path = path if path else '../data/thetas.csv'
    try:
        thetas_csv = read_csv(file_path, sep=',')
        expected_header = ['theta0', 'theta1']
        validate_csv(file_path, thetas_csv, expected_header, check_rows=True)
        
        theta_zero = float(thetas_csv.theta0.values[0])
        theta_one = float(thetas_csv.theta1.values[0])
    except (ValueError, IndexError):
        ErrorHandler.exit_with_error(ErrorHandler.INVALID_THETAS)
    except Exception as e:
        ErrorHandler.exit_with_error(e)

    thetas = {
        'theta0': theta_zero,
        'theta1': theta_one
    }
    return thetas

def get_data(file_path):
    try:
        data_csv = read_csv(file_path, sep=',')
        expected_header = ['km', 'price']
        validate_csv(file_path, data_csv, expected_header)
        
        data = {
            'x': np.array(data_csv.km, dtype=float),
            'y': np.array(data_csv.price, dtype=float)
        }
    except ValueError:
        ErrorHandler.exit_with_error(ErrorHandler.WRONG_DATA_IN_DATASET)
    except Exception as e:
        ErrorHandler.exit_with_error(e)
    
    return data