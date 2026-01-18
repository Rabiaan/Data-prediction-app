import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv('Housing.csv')

# Preprocessing
# List of binary categorical variables
binary_vars = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']

# Convert yes/no to 1/0
for var in binary_vars:
    df[var] = df[var].map({'yes': 1, 'no': 0})

# Convert furnishingstatus using one-hot encoding
# furnished, semi-furnished, unfurnished
df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)

# Split features and target
X = df.drop('price', axis=1)
y = df['price']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and columns
joblib.dump(model, 'house_price_model.pkl')
joblib.dump(X.columns.tolist(), 'model_columns.pkl')

print("Model trained and saved successfully.")
print(f"Model Score: {model.score(X_test, y_test)}")
