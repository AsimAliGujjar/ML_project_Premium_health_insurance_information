import streamlit as st
import predited
# Set up the title of the app
st.title("Health Insurance Information")

# Create three columns
col1, col2, col3 = st.columns(3)

# Create a dictionary to store the inputs
input_data = {}

# In the first column, place some of the select boxes
with col1:
    input_data['gender'] = st.selectbox('Gender', ['Male', 'Female'])
    input_data['region'] = st.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])
    input_data['marital_status'] = st.selectbox('Marital Status', ['Unmarried', 'Married'])
    input_data['age'] = st.number_input('Age', min_value=0, max_value=100, value=30, step=1)


# In the second column, place some of the select boxes
with col2:
    input_data['bmi_category'] = st.selectbox('BMI Category', ['Overweight', 'Underweight', 'Normal', 'Obesity'])
    input_data['smoking_status'] = st.selectbox('Smoking Status', ['Regular', 'No Smoking', 'Occasional'])
    input_data['employment_status'] = st.selectbox('Employment Status', ['Self-Employed', 'Freelancer', 'Salaried'])
    input_data['number_of_dependants'] = st.number_input('Number of Dependants', min_value=0, max_value=10, value=0, step=1)

# In the third column, place the remaining select boxes
with col3:
    input_data['income_lakhs'] = st.number_input('Income (in Lakhs)', min_value=0.0, value=10.0, step=0.1)
    input_data['genetical_risk'] = st.number_input('Genetical Risk', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    input_data['medical_history'] = st.selectbox('Medical History', ['High blood pressure', 'No Disease', 'Diabetes & High blood pressure', 'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid', 'Heart disease', 'Thyroid', 'High blood pressure & Heart disease'])
    input_data['insurance_plan'] = st.selectbox('Insurance Plan', ['Silver', 'Bronze', 'Gold'])

# Button to submit the data
if st.button('Predict'):
    # Display the dictionary of selected inputs
    d=predited.predict_data(input_data)
    st.write(f"Annual Premium Amount: {d[0]}")

