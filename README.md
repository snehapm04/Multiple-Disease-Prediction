# Disease Outbreak Prediction Using Machine Learning

## Problem Statement
Develop a system to predict the likelihood of disease outbreaks using machine learning techniques, utilizing diagnostic, demographic, and biomedical data for early intervention and resource allocation.

## Aim
Build machine learning models for disease prediction and outbreak analysis using diverse medical datasets to support public health decision-making.

## Learning Objectives
- Understand medical datasets and their preprocessing.
- Apply machine learning for disease prediction.
- Build and evaluate predictive models for heart disease, Parkinson’s disease, and diabetes.

## About the Project
Utilizing datasets for Heart Disease, Parkinson's Disease, and Diabetes, this project combines preprocessing techniques and machine learning to predict disease presence and assess outbreak risks.

## Datasets
1. **Heart Disease Dataset:** Diagnostic data including age, cholesterol, and heart rate (Target: Disease presence).
2. **Parkinson’s Disease Dataset:** Voice measurements from 31 individuals (Target: Health status).
3. **Diabetes Dataset:** Diagnostic metrics from Pima Indian women (Target: Diabetes presence).

## Tools and Techniques
- **Python Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn.
- **Models:** Logistic Regression, Random Forest, SVM.
- **Deployment:** Streamlit for interactive dashboards.

## Findings
- Preprocessing improved data quality and feature selection.
- Models were evaluated using accuracy, precision, recall, and F1-score.
- Streamlit provided real-time predictions through a user-friendly interface.

## Conclusion
This project applies machine learning for public health by predicting risks for heart disease, Parkinson’s, and diabetes. Future work includes integrating more datasets and exploring deep learning techniques.

---

## Repository Structure
```
Disease_Outbreak_Prediction/
├── data/               # Datasets
├── notebooks/          # Analysis and modeling
├── src/                # Preprocessing and evaluation
├── app/                # Streamlit app
├── requirements.txt  # Dependencies
└── README.md          # Project overview
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Disease_Outbreak_Prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```bash
   streamlit run app/main.py
   ```


## Acknowledgments
- Data sourced from medical research institutions.
- Inspired by advancements in machine learning for healthcare.

