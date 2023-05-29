# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 22:13:39 2023

@author: krgupta
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd



heart_disease_model = pickle.load(open('C:/Final Year Project/Disease Prediction System/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Final Year Project/Disease Prediction System/saved models/parkinsons_model.sav', 'rb'))

diabetes_model = pickle.load(open('C:/Final Year Project/Disease Prediction System/saved models/diabetes_model.sav', 'rb'))

st.set_page_config(page_title="Disease Prediction System", page_icon=":smiley:", layout="wide")

hide_menu_style = """
<style>
footer{visibility: hidden;}
</style>
"""
st.markdown(
    hide_menu_style,
    unsafe_allow_html=True)

st.markdown(
    """
    <style>
    body{
        background-image: linear-gradient(90deg, rgb(255, 75, 75), rgb(255, 253, 128));
        }
    </style>
    """,
    unsafe_allow_html=True
)




# Define the login page
def login():
    users = pd.read_csv('C:/Users/krgupta/Desktop/users.csv')
    st.title('Welcome to Disease Prediction System')
    
    st.write("Login to Predict whether a patient is affected by Heart, Diabetes, or Parkinson's Disease")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    login_button = st.button("Login")
    signup_button = st.button("New User - Signup")
    
    if login_button:
        user = users.loc[users['username'] == username]
        if not user.empty and password == user['password'].iloc[0]:
            st.success("Logged in!")
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")
    
    if signup_button:
        new_user = {'username': username, 'password': password}
        users = users.append(new_user, ignore_index=True)
        users.to_csv('C:/Users/krgupta/Desktop/users.csv', index=False)
        st.success("You have successfully registered!")
        
            
        


def report(patient_id,patient_name,doc_name,age,sex,prediction, disease):
    
    st.title("Disease Prediction Report by " + doc_name)
    st.header("Patient Information")
    gender = ""
    if sex == "1" or sex == 1:
        gender += "Male"
    else:
        gender += "Female"
    st.write("Patient ID: " + patient_id) 
    st.write("Patient Name: " + patient_name) 
    st.write("Age: " + str(age)) 
    st.write("Gender: " + gender)
    
    st.header("Prediction Results")
    
    if prediction == 0 and disease == "Heart Disease":
        result = f"{patient_name} is having {disease}"
        st.success(result)
    
        st.header("Tests Recommended")
        st.write("Electrocardiogram (ECG)")
        st.write("Echocardiogram")
        st.write("CT scan or MRI")
        st.write("Cardiac catheterization")
        st.write("Stress test")
    elif prediction == 1 and disease == "Parkinson's Disease":
        result = f"{patient_name} is having {disease}"
        st.success(result)
    
        st.header("Tests Recommended")
        st.write("Neurological examination")
        st.write("DaTscan")
        st.write("Blood tests")
        st.write("MRI or CT scan")
        st.write("PET scan")
    elif prediction == 1 and disease == "Diabetes":
        result = f"{patient_name} is having {disease}"
        st.success(result)
    
        st.header("Tests Recommended")
        st.write("Fasting Plasma Glucose (FPG) Test")
        st.write("Oral Glucose Tolerance Test (OGTT)")
        st.write("Glycated Hemoglobin (A1C) Test")
        st.write("Random Plasma Glucose Test")
        st.write("Urine Tests")
    else:
        st.success(f"{patient_name} is perfectly fine!!")        
    
        
    
# Define the home page
def Heart_Disease_Prediction():
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        patient_id = st.text_input('Pateint ID')
        
    with col2:
        patient_name = st.text_input('Patient Name')
        
    with col3:
        doc_name = st.text_input('Doctor Name')
        
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex (Gender)', placeholder="1 for male/2 for female")
        
    with col3:
        cp = st.text_input('Chest Pain Types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')    # > 120 mg/dl
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST Depression induced by Exercise')
        
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
        
    with col3:
        ca = st.text_input('Major Vessels colored by Flourosopy')
        
    with col1:
        thal = st.text_input('Thalassemia') # thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
        
    if age != '':
        age = int(age)
    if sex != '':    
        sex = int(sex)
    if cp != '':    
        cp = int(cp)
    if trestbps != '':    
        trestbps = int(trestbps)
    if chol != '':    
        chol = int(chol)
    if fbs != '':    
        fbs = int(fbs)
    if restecg != '':    
        restecg = int(restecg)
    if thalach != '':    
        thalach = int(thalach)
    if exang != '':    
        exang = int(exang)
    if oldpeak != '':    
        oldpeak = float(oldpeak)
    if slope != '':    
        slope = int(slope)
    if ca != '':    
        ca = int(ca)
    if thal != '':
        thal = int(thal)
     
    # code for Prediction
    #heart_diagnosis = ''
    
    # creating a button for Prediction
    heart_disease = "Heart Disease"
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        report(patient_id,patient_name,doc_name,age,sex,heart_prediction[0], heart_disease)                          
        


def Parkinson_Prediction():
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        patient_id = st.text_input('Pateint ID')
        
    with col2:
        patient_name = st.text_input('Patient Name')
        
    with col3:
        doc_name = st.text_input('Doctor Name')
        
    with col1:
        fo = st.text_input('Average Vocal Fundamental Frequency')   #MDVP:Fo(Hz) 
        
    with col2:
        fhi = st.text_input('Maximum Vocal Fundamental Frequency')  #MDVP:Fhi(Hz)
        
    with col3:
        flo = st.text_input('Minimum Vocal Fundamental Frequency')    #MDVP:Flo(Hz)
        
    with col1:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col2:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col3:
        RAP = st.text_input('MDVP: RAP')
        
    with col1:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col2:
        DDP = st.text_input('Jitter: DDP')
        
    with col3:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col1:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
    with col2:
        APQ3 = st.text_input('Shimmer: APQ3')
        
    with col3:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col1:
        APQ = st.text_input('MDVP: APQ')
        
    with col2:
        DDA = st.text_input('Shimmer: DDA')
        
    with col3:
        NHR = st.text_input('Ratio of Noise to Tonal Components in the Voice 1: NHR')
        
    with col1:
        HNR = st.text_input('Ratio of Noise to Tonal Components in the Voice 2: HNR')
        
    with col2:
        RPDE = st.text_input('Dynamical Complexity Measure 1: RPDE')
        
    with col3:
        DFA = st.text_input('Signal Fractal Scaling Exponent') 
        
    with col1:
        spread1 = st.text_input('Fundamental Frequency Variation 1: spread1')
        
    with col2:
        spread2 = st.text_input('Fundamental Frequency Variation 2: spread2')
        
    with col3:
        D2 = st.text_input('Dynamical Complexity Measure 2: D2')
        
    with col1:
        PPE = st.text_input('Fundamental Frequency Variation 3: PPE')
    
    with col2:
        age = st.text_input('Age')
        
    with col3:
        sex = st.text_input('Gender', placeholder="1 for male/2 for female")
    
    
    # code for Prediction
    parkinsons_disease = "Parkinson's Disease"
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        report(patient_id,patient_name,doc_name,age,sex,parkinsons_prediction[0], parkinsons_disease)
        
    

def Diabetes_Prediction():
    
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        patient_id = st.text_input('Pateint ID')
        
    with col2:
        patient_name = st.text_input('Patient Name')
        
    with col3:
        doc_name = st.text_input('Doctor Name')
        
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    with col3:
        sex = st.text_input("Gender", placeholder="1 for male/2 for female")
    
    
    # code for Prediction
    diab_disease = 'Diabetes'
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        report(patient_id,patient_name,doc_name,Age,sex,diab_prediction[0], diab_disease)
        
    
    
# Define the logout page
def logout():
    st.session_state.logged_in = False
    st.experimental_rerun()

# Define the page navigation
def navigate():
    with st.sidebar:
        
        selected = option_menu('Disease Prediction System',

                              [ 'Heart Disease Prediction',
                               "Parkinson's Prediction",
                               'Diabetes Prediction', 'Logout'],
                              icons=['heart','person','activity'],
                              default_index=0)
        
        
    if selected == 'Heart Disease Prediction':
        Heart_Disease_Prediction()
    elif selected == "Parkinson's Prediction":
        Parkinson_Prediction()
    elif selected == 'Diabetes Prediction':
        Diabetes_Prediction()
    else:
        logout() 
    
    

# Check if the user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Show the login page if the user is not logged in
if not st.session_state.logged_in:
    login()

# Show the page navigation if the user is logged in
else:
    navigate()
    
st.markdown(
    """
    <div class="footer">
        Made by: Mansi Gupta and Krishna Kant Gupta<br>
        Purpose: Final Year Project<br>
        
    </div>
    """,
    unsafe_allow_html=True
)
    
st.markdown(
    """
    <style>
    .footer {
        background-image: linear-gradient(90deg, rgb(255, 75, 75), rgb(255, 253, 128));
        color: black;
        padding: 10px;
        text-align: center;
        border-radius: 10px;
        position:sticky;
        bottom: 10px;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class= "footer-copyright">
    <p>
    ©2023 DPS. All Rights Reserved
    </p>
    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .footer-copyright {
        padding-top: 8px;
        text-align: center;
        font-weight: 100;
        font-size: 12px;
        box-sizing: border-box;
        display: block;
        
        }
    </style>
    """,
    unsafe_allow_html=True
    )
