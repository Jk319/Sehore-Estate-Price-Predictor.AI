# 🏠 Sehore Real Estate Price Predictor.AI

**AI-powered real estate valuation system built using Machine Learning and Streamlit**

##  Project Overview

## Key Features

### 🔹 Machine Learning Models
- Linear Regression (**best-performing model**)
- Random Forest Regressor 
- Gradient Boosting Regressor
- XGBoost Regressor (optional comparison)

### 🔹 Web Application (Streamlit)
- Two-page interactive web interface:
  - **Property Price Prediction**
  - **Model Analytics & Report Download**
- Clean, responsive UI
- Real-time predictions
- Downloadable PDF evaluation report
- Deployed and runnable locally or online

### 🔹 Data & Insights
- Real estate dataset from Sehore district
- Exploratory Data Analysis (EDA)
- Feature importance visualization
- Model comparison using R², RMSE, and MAE
- Actual vs Predicted analysis
- Residual error analysis

---

## 📁 Project Structure
```plaintext
Sehore_RealEstate_WebApp/
│
├── app.py
├── requirements.txt
│
├── streamlit_app/
│ ├── Home.py
│ ├── Analytics.py
│
├── models/
│ └── final_real_estate_model.pkl
│
├── data/
│ └── sehore_real_estate_2000.xlsx
│
├── reports/
│ └── evaluation_report.pdf
│
├── notebooks/
│ └── Sehore_Real_Estate_ML_Project.ipynb
│
└── assets/
├── system_architecture.png
└── system_workflow.png
```

```bash
##  Installation & Setup

 Clone the Repository
git clone https://github.com/YOUR_USERNAME/Sehore-RealEstate-Price-Predictor-AI.git
cd Sehore-RealEstate-Price-Predictor-AI

 Install Dependencies
pip install -r requirements.txt

 Run the Streamlit App
streamlit run app.py

 Open in Browser
http://localhost:8501


```
---

##  Machine Learning Workflow

### 🔹 Data Preprocessing
- Missing value handling
- Categorical feature encoding
- Feature scaling
- Train–Test split

### 🔹 Model Training & Evaluation
Multiple regression models were trained and evaluated using:
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Root Mean Square Error (RMSE)**

### 🔹 Best Model Selection
**Linear Forest Regressor** was selected based on:
- Highest R² score
- Lowest MAE & RMSE
- Stable generalization on unseen data

---

##  Model Performance Summary

| Model              | R² Score | MAE    | RMSE   | Status       |
|-------------------|----------|--------|--------|---------------|
| Linear Regression | Low      | High   | High   | Best Model    |
| Random Forest     | High     | Low    | Low    |  Good         |
| Gradient Boosting | Medium   | Medium | Medium | Good          |
| XGBoost           | Comparable | Medium | Medium | Optional    |

---

##  Web Application Features

 Property Price Prediction  
 Model Analytics Dashboard  
 PDF Report Download  
 Clean & professional UI  

> Screenshots can be added in the `/assets` directory

---

##  Technologies Used

### Machine Learning & Data Science
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn

### Web Development
- Streamlit
- HTML / CSS

### Tools & Deployment
- VS Code
- Git & GitHub
- Virtual Environment (venv)

---
 
 ### Contributions are welcome.
Feel free to fork the repository and submit a pull request.
- Virtual Environment (venv)

### 👨‍💻 Author

**Jatin Kushwaha**  
[GitHub](https://github.com/Jk319) | [LinkedIn](https://linkedin.com/in/jatin-kushwaha)




