# Fastapi-mobile
This project predicts smartphone prices based on hardware specifications such as RAM, storage, battery, display, chipset, brand, and connectivity features.

It demonstrates a complete data science pipeline:
✔ Data preprocessing & EDA
✔ Feature engineering & encoding
✔ Model training & hyperparameter tuning
✔ Model serialization
✔ REST API using FastAPI
✔ Web UI using Streamlit
✔ Deployment-ready structure
✔ GitHub documentation + demo video

# Project Structure
├── Mobile_price_prediction.ipynb   # Model training + EDA
├── FastApi.py                      # FastAPI inference server
├── Front_end.py                   # Streamlit frontend UI
├── final_MPP.pkl                  # Trained ML model
├── scaled_value.pkl               # Feature scaler
├── requirements.txt
└── README.md

# Model Training
Training was performed in Mobile_price_prediction.ipynb and included:

Exploratory Data Analysis
  -price distribution
  -feature correlations
  -brand-wise price variation
  -numeric feature scaling
  
Feature Engineering
 One-hot encoding for:
  -brands
  -processors
Ordinal encoding for:
  -battery sizes
  -screen types
  -numeric normalization using StandardScaler
  
Models Tested
 -Linear Regression
 -Random Forest Regressor
 -KNeighborsRegressor
 -Gradient Boosting
 -Ensemble methods

Hyperparameter Tuning
Used:
  -GridSearchCV
  -cross-validation

# FastAPI
Prediction Flow

1️st Input arrives via API
2️nd Converted to NumPy array
3️rd Scaled using saved scaler
4️th Passed into trained model
5️th Prediction returned

# Streamlit
Streamlit Frontend
Frontend is implemented in Front_end.py 
Front_end
It allows users to:
  -select smartphone specs
  -choose brand & chipset
  -pick battery size
  -select screen type
  -submit data
  -see predicted price instantly

# Frontend → API Flow

User Input → Streamlit UI
             ↓
        JSON Request
             ↓
         FastAPI
             ↓
     Scaler → Model
             ↓
        Predicted Price
             ↓
         Displayed in UI

# LinkedIn: 
         
