
# config/settings.py
# Configuration settings for the Cancer Risk Prediction app

# ------------------------------
# Model and Encoder File Paths
# ------------------------------
MODEL_PATH = "src/cancer_model.pkl"
SCALER_PATH = "src/scaler.pkl"
BMI_ENCODER_PATH = "src/bmi_encoder.pkl"
AGE_ENCODER_PATH = "src/age_group_encoder.pkl"

# ------------------------------
# Input Feature Groups
# ------------------------------
NUMERICAL_FEATURES = ["Age", "BMI", "PhysicalActivity", "AlcoholIntake"]
CATEGORICAL_FEATURES = ["Gender", "Smoking", "GeneticRisk", "CancerHistory"]
ENGINEERED_FEATURES = ["BMI_Category", "Age_Group"]

# ------------------------------
# Deployment Settings
# ------------------------------
DEBUG = True
HOST = "127.0.0.1"
PORT = 5000
