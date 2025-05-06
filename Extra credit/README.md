# Cancer Risk Prediction

This is a simple web application for predicting cancer risk based on several health parameters. The application allows users to input various health-related details, such as age, gender, BMI, smoking habits, genetic risk, physical activity, alcohol intake, cancer history, BMI category, and age group. Based on these inputs, the system predicts the user's risk of developing cancer.

# Features

Predicts cancer risk based on user inputs.

Includes input fields for:

Age

Gender (0 = Female, 1 = Male)

BMI (Body Mass Index)

Smoking habits (0 = No, 1 = Yes)

Genetic risk (0 = No, 1 = Yes)

Physical activity (hours per week)

Alcohol intake (units per week)

Cancer history (0 = No, 1 = Yes)

BMI category (0 = Underweight, 1 = Normal, 2 = Overweight, 3 = Obese)

Age group (0 = <40, 1 = 40-60, 2 = 60-80, 3 = 80+)

# Predictive model to calculate cancer risk.

Attractive, simple UI with a background image.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.x

Flask (or any similar web framework)

A text editor like Visual Studio Code or any other editor of your choice.

Dependencies for the model (pandas, xgboost)

# Step 1: Clone the repository


git clone <your-repository-url>
cd <your-project-folder>

# Step 2: Install the required Python packages

You will need to install Flask or any other web framework you are using. You can create a virtual environment and install the dependencies as follows:

python3 -m venv venv
source venv/bin/activate  # For Windows use venv\Scripts\activate
pip install flask

# Step 3: Run the Application

Make sure to set up your Flask application properly, and if you are using templates (e.g., index.html), ensure the folder structure is correct.

# Start your Flask application:

python app.py  # or any other script file you use to run the app

Your app should be available at http://127.0.0.1:5000/.

# Step 4: Access the App

Open a web browser and navigate to:

http://127.0.0.1:5000/

You will see the "Cancer Risk Prediction" form.

Usage

Enter the required health data into the input fields.

Click "Predict" to see the result based on your inputs.

The prediction result will be displayed below the form.

Project Structure

Cancer-Risk-Prediction/
│
├── app.py              # Main Python file to run the app (Flask app)
├── templates/          # Contains HTML files (e.g., index.html)
│   └── index.html      # The form for collecting user data
├── static/             # Contains static files like CSS, images
│   └── img_2.png         # Background image
├── README.md           # This file
└── requirements.txt    # Python dependencies

Dependencies

Flask

# scikit-learn, pandas, or any required libraries for prediction model