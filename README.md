# 42_ft_linear_regression 🚗📈

## Overview ✨

This project is an **machine learning toolset** for performing linear regression analysis on car mileage and price data. Linear regression is a foundational technique in artificial intelligence and machine learning, used for predicting continuous values. This project covers the full pipeline: data scraping, cleaning, model training, prediction, and evaluation. The codebase is modular, allowing users to generate datasets, train a model, make predictions, and evaluate model precision.

---

## Features 🚀

- 🤖 **ML Powered:** Utilizes linear regression, a core machine learning algorithm, to model and predict car prices.
- 🕸️ **Dataset Generation:** Scrape car mileage and price data from the web, clean and save as CSV.
- 🤖 **Model Training:** Train a linear regression model to predict car prices based on mileage.
- 🔮 **Prediction:** Predict car prices for given mileage using trained model parameters.
- 📊 **Precision Calculation:** Evaluate model performance with MSE, RMSE, and R-squared metrics.
- 📉 **Data Visualization:** Plot data points and regression line.

---

## Project Structure 🗂️

```
42_ft_linear_regression/
├── data/                # Datasets and model parameters (CSV files)
├── requirements.txt     # Python dependencies
└── src/
    ├── dataset_generator.py      # Scrape and clean data
    ├── precision_calculator.py   # Evaluate model precision
    ├── predictor.py              # Predict price from mileage
    ├── trainer.py                # Train linear regression model
    └── utils/
        ├── data_plotter.py       # Plotting utilities
        ├── errors.py             # Error handling
        ├── file_utils.py         # Data/model I/O
        ├── linear_regression.py  # Core regression logic
        ├── scraper.py            # Web scraping logic
        ├── url.py                # URL handling
        ├── validators.py         # CSV/data validation
        └── __init__.py
```

---

## Installation ⚙️

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd 42_ft_linear_regression
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage 🛠️

### 1. Generate Dataset 🕸️
Scrape and clean car data, then save as CSV:
```sh
python src/dataset_generator.py -p data/data_original.csv -n 1000
```

### 2. Train Model 🤖
Train a linear regression model on your dataset:
```sh
python src/trainer.py -d data/data_original.csv --save_thetas -t data/thetas.csv --show_data
```

### 3. Predict Price 🔮
Predict the price for a given mileage:
```sh
python src/predictor.py -p data/thetas.csv
```

### 4. Evaluate Model Precision 📊
Calculate MSE, RMSE, and R-squared for your model:
```sh
python src/precision_calculator.py -d data/data_original.csv -t data/thetas.csv
```

---

## Dependencies 📦

- pandas
- numpy
- matplotlib
- tqdm
- requests
- beautifulsoup4
- lxml

Install all dependencies with:
```sh
pip install -r requirements.txt
```

---

## How It Works 🔄

1. **Data Acquisition:** 🕸️ Scrape car data → Clean and optimize dataset → Save as CSV.
2. **Model Training:** 🤖 Load dataset → Train linear regression model → Save thetas.
3. **Prediction:** 🔮 Load thetas → Input mileage → Predict price.
4. **Evaluation:** 📊 Load dataset and thetas → Calculate precision metrics.

---
