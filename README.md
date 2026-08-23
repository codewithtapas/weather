# Prediction of CBR Strength of Clay Soil Stabilized with Stone Dust Using XGBoost
Project Overview

This project predicts the California Bearing Ratio (CBR) strength of clay soil stabilized with stone dust using the XGBoost Machine Learning algorithm.

The model helps civil engineers estimate soil strength efficiently without performing extensive laboratory testing.

Objectives
Analyze soil properties.
Predict CBR values using XGBoost.
Compare actual and predicted values.
Visualize feature importance and correlations.
Dataset

The dataset contains:

Soil parameters
Stone dust percentage
CBR values

Dataset Source:
UCI Machine Learning Repository

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
XGBoost
Scikit-Learn
Project Structure
CBR-Prediction/
│
├── cbr_data.csv
├── cbr_model.py
├── Actual_vs_Predicted.py
├── Statistical_summary.py
├── correlation_graph.py
├── README.md
│
├── actual_vs_predicted.png
├── correlation_matrix.png
├── feature_importance.png
└── statistical_summary.png
Results
Actual vs Predicted Values

<img width="2076" height="1708" alt="actual_vs_predicted" src="https://github.com/user-attachments/assets/c3627656-885e-4bb3-be13-d78c376355f7" />


Correlation Matrix

<img width="2264" height="1764" alt="correlation_matrix" src="https://github.com/user-attachments/assets/6431e475-536d-4a68-a799-efc77bfbcebb" />


Feature Importance

<img width="2646" height="1638" alt="feature_importance" src="https://github.com/user-attachments/assets/e781887a-bb2a-468e-bd6c-4c7719e284b3" />


Installation
git clone <repository-url>
cd CBR-Prediction
pip install -r requirements.txt
Run
python cbr_model.py
Future Scope
Hyperparameter optimization
Deployment using Streamlit
Real-time prediction system
Author

Tapas Mohanty
M.Tech in Data Science
IMIT


Content:

pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost



