# House Price Prediction App

A Streamlit web application for predicting house prices based on various features.

## Features

- Predict house prices based on area, bedrooms, bathrooms, stories, and amenities
- Interactive web interface built with Streamlit
- Machine learning model trained on housing data

## Deployment to Vercel

This app is configured for deployment to Vercel. Follow these steps:

1. Go to [Vercel](https://vercel.com)
2. Sign in with your GitHub account
3. Click "Add New Project"
4. Import your GitHub repository (`Data-prediction-app`)
5. Vercel will automatically detect the configuration from `vercel.json`
6. Click "Deploy"

The app should be live within a few minutes!

## Local Development

To run locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model (if not already done):
   ```bash
   python train_model.py
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Files

- `app.py` - Main Streamlit application
- `train_model.py` - Script to train the machine learning model
- `Housing.csv` - Dataset used for training
- `house_price_model.pkl` - Trained model (pickled)
- `model_columns.pkl` - Feature columns used in training
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel deployment configuration

## Model Details

The model uses Linear Regression to predict house prices based on:
- Area (square feet)
- Number of bedrooms and bathrooms
- Number of stories
- Parking spaces
- Amenities (main road access, guest room, basement, etc.)
- Furnishing status