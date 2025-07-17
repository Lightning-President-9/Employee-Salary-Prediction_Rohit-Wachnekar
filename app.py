import pandas as pd
import streamlit as st
import plotly.express as px
import joblib

# Load the pre-trained model and encoders
model = joblib.load("salary_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")

# Load dataset for visualization
@st.cache_data
def load_data():
    df = pd.read_csv("adult 3.csv")
    df.replace('?', None, inplace=True)
    return df

st.title("Employee Salary Prediction App")
df = load_data()

# Show sample data
st.subheader("Sample Data")
st.dataframe(df.head())

# Visualizations
st.subheader("Data Visualizations")

fig1 = px.histogram(df, x='income', title='Income Distribution', color='income')
st.plotly_chart(fig1)

fig2 = px.box(df, x='income', y='age', color='income', title='Age vs Income')
st.plotly_chart(fig2)

fig3 = px.histogram(df, x='education', color='income', title='Education vs Income', barmode='group')
st.plotly_chart(fig3)

# Prediction Section
st.subheader("Predict Employee Salary")

# Create input fields dynamically
input_data = {}
for col in df.columns:
    if col != 'income':
        if col in label_encoders:  # categorical column
            input_data[col] = st.selectbox(col, label_encoders[col].classes_)
        else:  # numeric column
            input_data[col] = st.number_input(col, value=float(df[col].mean()))

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical fields
for col in label_encoders:
    input_df[col] = label_encoders[col].transform(input_df[col])

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(input_df)[0]
    salary_label = target_encoder.inverse_transform([prediction])[0]
    st.success(f"Predicted Salary Category: {salary_label}")
