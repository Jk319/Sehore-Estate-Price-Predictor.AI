# Sehore-Real-Estate-Price-Predictor.AI

### *AI-powered real estate valuation using Machine Learning, Deep Learning & Flask*

---

##  Overview

- **Goal:** Predict real-estate property prices for the *Sehore district* using ML + DL models.  
- **Dataset:** 2,000+ real estate entries collected from Sehore district.  
- **Approach:**  
  Preprocessing → Feature Engineering → EDA → Train 8+ Models → Compare Performance → Deploy Flask Web App.

---

## Dataset

- **Source:** Sehore district real estate dataset (2000+ entries).  
- **Attributes:**  
  - Area  
  - Tehsil  
  - Property Type  
  - Ownership Type  
  - Price  
- **Data Analysis Includes:**  
  - Correlation heatmaps  
  - Trend analysis  
  - Boxplots, pairplots  
  - Outlier detection  
  - Feature importance  

---

##  Technologies Used

### **Machine Learning / Deep Learning**
- Python  
- Pandas, NumPy  
- Scikit-learn  
- TensorFlow / Keras  
- Matplotlib, Seaborn  

### **Web Development**
- Flask  
- HTML5, CSS3, JavaScript   
- Chart.js  

### **Deployment**
- Render  
- VS Code
---

##  Preprocessing Steps

- Handled missing values  
- Label encoding for categorical features  
- Scaling numeric features  
- Train–Validation–Test split  
- Feature engineering  
- Distribution analysis + outlier filtering  

---

##  Model Architectures (RF + ANN + LSTM)

### 🔹 **Random Forest (Best Model)**
- 100+ decision trees  
- Bootstrap aggregating  
- Calculates feature importance  
- High stability and low MAE  
- Best R² score (~0.90)

---

### 🔹 **Artificial Neural Network (ANN)**  
- **Input Layer:** Numeric + encoded features  
- **Hidden Layers:**  
  - Dense layers  
  - ReLU activation  
  - Dropout for regularization  
- **Output Layer:** Linear activation (for regression)  
- Optimizer: Adam  
- Loss: MSE / MAE  

---

 🔹 **LSTM Deep Learning Model**
- Sequence modeling approach  
- LSTM units  
- Dense regression output  
- Higher training time  

---

##  Results

| Model | R² Score | MAE | Status |
|-------|----------|------|--------|
| **Random Forest** | **0.90** | Low | Best Model |
| ANN | 0.85 | Medium | Good |
| LSTM | Lower | High | Not suitable |
| Linear Regression | 0.65 | High | Underfitting |

### **Selected Models for Deployment**
- **Random Forest → Best accuracy & stability**  
- **ANN → 2nd best model with good generalization**

---

##  Sample Predictions

-  **Area: 1200 sqft** → *Predicted Price: ₹ 18.4 lakhs (RF)*  
-  **Area: 800 sqft** → *Predicted Price: ₹ 11.7 lakhs (ANN)*
  
- Charts:  
  - Tehsil-wise price curve  
  - Property-type pie chart  

---

##  Folder Structure
```plaintext
Sehore_RealEstate_WebApp/
│ app.py
│ requirements.txt
│ render.yaml
│
├── models/
│   ├── random_forest.pkl
│   ├── ann_model.h5
│   └── scaler.pkl
│
├── data/
│   └── sehore_real_estate_2000_only_sehore.csv
│
├── templates/
│   ├── index.html
│   └── analysis.html
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── reports/thesis_report.pdf
│
└── notebooks/
    └── Sehore_Real_Estate_AI_Project_FIXED.ipynb

```

##  Future Enhancements

- Add Gradient Boosting / XGBoost models  
- Deploy mobile-friendly version  
- Add geolocation-based pricing (Maps API)  
- Add feature to compare predicted vs actual trends  
- Introduce ensemble hybrid model (RF + ANN)  

##  Author

**Jatin Kushwaha**  
[GitHub](https://github.com/Jk319) | [LinkedIn](https://linkedin.com/in/jatin-kushwaha)

---
