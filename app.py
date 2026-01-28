import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import sys

# Load the model and columns
try:
    # Try multiple paths for Vercel deployment
    current_dir = os.path.dirname(os.path.abspath(__file__))
    possible_paths = [
        os.path.join(current_dir, 'house_price_model.pkl'),
        os.path.join(os.getcwd(), 'house_price_model.pkl'),
        'house_price_model.pkl'
    ]
    
    model = None
    model_columns = None
    
    for model_path in possible_paths:
        columns_path = model_path.replace('house_price_model.pkl', 'model_columns.pkl')
        try:
            if os.path.exists(model_path) and os.path.exists(columns_path):
                model = joblib.load(model_path)
                model_columns = joblib.load(columns_path)
                st.success(f"Model loaded successfully from: {model_path}")
                break
        except Exception as e:
            continue
    
    if model is None or model_columns is None:
        st.error("❌ Model files not found!")
        st.info("Available files in current directory:")
        for file in os.listdir('.'):
            st.write(f"- {file}")
        st.stop()
        
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

st.title("House Price Prediction App")
st.write("Enter the details of the house to predict its price.")

# Input fields
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=0, value=5000)
    bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=0, value=1)
    stories = st.number_input("Stories", min_value=1, value=1)
    parking = st.number_input("Parking Spaces", min_value=0, value=1)

with col2:
    mainroad = st.selectbox("Main Road Access", ["yes", "no"])
    guestroom = st.selectbox("Guest Room", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
    airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
    prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# Prepare input data
input_data = {
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'mainroad': [1 if mainroad == "yes" else 0],
    'guestroom': [1 if guestroom == "yes" else 0],
    'basement': [1 if basement == "yes" else 0],
    'hotwaterheating': [1 if hotwaterheating == "yes" else 0],
    'airconditioning': [1 if airconditioning == "yes" else 0],
    'parking': [parking],
    'prefarea': [1 if prefarea == "yes" else 0]
}

# Add furnishing status dummies
# semi-furnished -> furnishingstatus_semi-furnished
# unfurnished -> furnishingstatus_unfurnished
input_data['furnishingstatus_semi-furnished'] = [1 if furnishingstatus == "semi-furnished" else 0]
input_data['furnishingstatus_unfurnished'] = [1 if furnishingstatus == "unfurnished" else 0]

# Create DataFrame and reorder columns to match training
input_df = pd.DataFrame(input_data)
input_df = input_df[model_columns]

if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"The estimated price of the house is: ${prediction[0]:,.2f}")
