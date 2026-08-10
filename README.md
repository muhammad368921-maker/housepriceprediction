# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on different characteristics of a house and its surrounding area.

## 📌 Project Overview

This project uses **Linear Regression** to predict house prices from five input features:

* Average Area Income
* Average Area House Age
* Average Area Number of Rooms
* Average Area Number of Bedrooms
* Area Population

The trained machine learning model is integrated into a **Streamlit web application**, allowing users to enter house information and receive a predicted house price.

## 📊 Dataset

The project uses the `Housing.csv` dataset containing **5,000 house records** and 7 columns.

The original dataset contains:

* 5 numerical input features
* 1 target variable (`Price`)
* 1 address column

The `Address` column was removed because it was not used as an input feature for our model.

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

### Features

```text
Avg. Area Income
Avg. Area House Age
Avg. Area Number of Rooms
Avg. Area Number of Bedrooms
Area Population
```

### Target

```text
Price
```

## 📈 Model Performance

The model was evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

Results:

| Metric   |             Value |
| -------- | ----------------: |
| MAE      |         80,879.10 |
| MSE      | 10,089,009,299.50 |
| RMSE     |        100,444.06 |
| R² Score |             0.918 |

The R² score of approximately **0.918** means that the model explains about 91.8% of the variation in the target values in the test set.

## 🌐 Streamlit Application

The trained model is saved as:

```text
house_price_model.pkl
```

The Streamlit application loads this saved model and uses it to make predictions based on user input.

## 📁 Project Structure

```text
House Prediction/
│
├── house_price_prediction.ipynb
├── house_price_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Create or activate the Python environment used for the project and install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Open a terminal in the project folder and run:

```bash
streamlit run app.py
```

The application will open in a web browser.

## 🧪 Example Input

```text
Average Area Income: 70000
Average Area House Age: 6
Average Area Number of Rooms: 7
Average Area Number of Bedrooms: 4
Area Population: 35000
```

The model predicts approximately:

```text
1,250,170.95
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 🎯 Learning Objectives

Through this project, the following machine learning concepts were practiced:

* Data loading
* Data exploration
* Data preprocessing
* Feature and target selection
* Train-test splitting
* Linear Regression
* Model training
* Model prediction
* Model evaluation
* MAE, MSE, RMSE and R²
* Feature scaling with StandardScaler
* Saving and loading a trained model
* Building a Streamlit ML application
* Creating project documentation
