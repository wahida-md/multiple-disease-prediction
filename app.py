import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load saved models
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Parkinsons Prediction'])

# ---------------- HEART DISEASE ----------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    age = st.number_input('Age')
    sex = st.number_input('Sex (0=Female, 1=Male)')
    cp = st.number_input('Chest Pain Type')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Cholesterol')
    fbs = st.number_input('Fasting Blood Sugar >120 (1=True, 0=False)')
    restecg = st.number_input('Rest ECG')
    thalach = st.number_input('Max Heart Rate')
    exang = st.number_input('Exercise Induced Angina')
    oldpeak = st.number_input('Oldpeak')
    slope = st.number_input('Slope')
    ca = st.number_input('Number of Major Vessels')
    thal = st.number_input('Thal (0,1,2)')

    if st.button('Heart Test Result'):
        prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs,
                                           restecg, thalach, exang, oldpeak,
                                           slope, ca, thal]])
        if prediction[0] == 1:
            st.success("Person has Heart Disease")
        else:
            st.success("Person does NOT have Heart Disease")

# ---------------- DIABETES ----------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    Pregnancies = st.number_input('Pregnancies')
    Glucose = st.number_input('Glucose')
    BloodPressure = st.number_input('Blood Pressure')
    SkinThickness = st.number_input('Skin Thickness')
    Insulin = st.number_input('Insulin')
    BMI = st.number_input('BMI')
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function')
    Age = st.number_input('Age')

    if st.button('Diabetes Test Result'):
        prediction = diabetes_model.predict([[Pregnancies, Glucose,
                                              BloodPressure, SkinThickness,
                                              Insulin, BMI,
                                              DiabetesPedigreeFunction, Age]])
        if prediction[0] == 1:
            st.success("Person is Diabetic")
        else:
            st.success("Person is NOT Diabetic")

# ---------------- PARKINSONS ----------------
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction')

    fo = st.number_input('MDVP:Fo')
    fhi = st.number_input('MDVP:Fhi')
    flo = st.number_input('MDVP:Flo')
    jitter = st.number_input('Jitter (%)')
    shimmer = st.number_input('Shimmer')
    NHR = st.number_input('NHR')
    HNR = st.number_input('HNR')
    RPDE = st.number_input('RPDE')
    DFA = st.number_input('DFA')
    spread1 = st.number_input('spread1')
    spread2 = st.number_input('spread2')
    D2 = st.number_input('D2')
    PPE = st.number_input('PPE')

    if st.button('Parkinsons Test Result'):
        prediction = parkinsons_model.predict([[fo, fhi, flo, jitter,
                                                shimmer, NHR, HNR,
                                                RPDE, DFA,
                                                spread1, spread2,
                                                D2, PPE]])
        if prediction[0] == 1:
            st.success("Person has Parkinsons Disease")
        else:
            st.success("Person does NOT have Parkinsons Disease")