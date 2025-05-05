
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('cancer_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load label encoders for engineered features
bmi_encoder = joblib.load('bmi_encoder.pkl')
age_group_encoder = joblib.load('age_group_encoder.pkl')

# Features expected by the model (must match training)
numerical_features = ['Age', 'BMI', 'PhysicalActivity', 'AlcoholIntake']
categorical_features = ['Gender', 'Smoking', 'GeneticRisk', 'CancerHistory']
engineered_features = ['BMI_Category', 'Age_Group']

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# Function to categorize age
def categorize_age(age):
    if age < 40:
        return '<40'
    elif age < 60:
        return '40-60'
    elif age < 80:
        return '60-80'
    else:
        return '80+'

# Function to safely transform categories, handling unseen labels
def safe_transform(encoder, value):
    try:
        return encoder.transform([value])[0]
    except ValueError:
        # Handle unseen labels gracefully by encoding as a default value (use first label)
        return encoder.transform([encoder.classes_[0]])[0]

@app.route('/')
def home():
    return render_template('index.html', content_type='text/html; charset=utf-8')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from form
    data = request.form
    age = float(data['Age'])
    gender = int(data['Gender'])
    bmi = float(data['BMI'])
    smoking = int(data['Smoking'])
    genetic_risk = int(data['GeneticRisk'])
    physical_activity = float(data['PhysicalActivity'])
    alcohol_intake = float(data['AlcoholIntake'])
    cancer_history = int(data['CancerHistory'])

    # Feature engineering
    bmi_category = categorize_bmi(bmi)
    age_group = categorize_age(age)

    # Encode engineered features using safe_transform
    bmi_cat_encoded = safe_transform(bmi_encoder, bmi_category)
    age_group_encoded = safe_transform(age_group_encoder, age_group)

    # Combine all features
    input_array = np.array([ 
        age, bmi, physical_activity, alcohol_intake,
        gender, smoking, genetic_risk, cancer_history,
        bmi_cat_encoded, age_group_encoded
    ]).reshape(1, -1)

    # Normalize numerical features only
    input_array[:, 0:4] = scaler.transform(input_array[:, 0:4])

    # Predict cancer diagnosis (0 = No Cancer, 1 = Has Cancer)
    diagnosis = model.predict(input_array)[0]

    # Determine result based on prediction
    if diagnosis == 1:
        result = 'Has Cancer'
    else:
        result = 'Does Not Have Cancer'

    # Return the result in the template
    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == '__main__':
    app.run(debug=True)
    
