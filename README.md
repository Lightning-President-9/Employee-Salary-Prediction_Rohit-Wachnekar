# Employee-Salary-Prediction_Rohit-Wachnekar

## Project Overview
This project predicts whether an employee's salary is **`<=50K`** or **`>50K`** per year using demographic and work-related attributes. It uses **Random Forest Classifier** for prediction and a **Streamlit app** for interactive visualization and salary prediction.

---

## Features
- **Data Preprocessing**
  - Handles missing values by replacing `?` and removing incomplete rows.
  - Encodes categorical variables using `LabelEncoder`.
- **Model Training**
  - Uses **Random Forest Classifier** with 85.61% accuracy.
  - Generates a classification report with precision, recall, and F1-score.
- **Model Deployment**
  - Built an interactive **Streamlit app** for:
    - Data visualization (Histograms, Boxplots).
    - Predicting employee salary category based on input features.
- **Model & Encoder Persistence**
  - Saves model and encoders using `joblib` for reuse.

---

## Dataset
- Dataset used: **Adult Income Dataset**
- File: `adult 3.csv`
- Source: [Download Here](https://github.com/Lightning-President-9/Employee-Salary-Prediction_Rohit-Wachnekar/blob/main/adult%203.csv)

---

## Model Details
- **Algorithm**: Random Forest Classifier
- **Accuracy**: 85.61%
- **Evaluation Metrics**:
