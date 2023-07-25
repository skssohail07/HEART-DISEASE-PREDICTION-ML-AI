import pickle
import streamlit as st

from PIL import Image, ImageOps

import numpy as np
import tensorflow as tf
from streamlit_option_menu import option_menu

Heart_Disease_model = pickle.load(open(r'C:\Users\Mastermind\Desktop\Heart-Disease-Prediction-main\Heart_model.sav','rb'))
st.title('Heart Disease Prediction Using ML')
    
col1,col2,col3 = st.columns(3)
    
with col1:
        age = st.number_input("Your Age")
        
with col2:
        sex = st.number_input("Gender (1->Male , 0-> Female)")
        
with col3:
        cp = st.number_input("Chest Pain Type(cp)")
        
with col1:
        trestbps = st.number_input("Resting Blood Pressure")
        
with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl")
        
with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")
        
with col1:
        restecg = st.number_input("Resting Electrocardiographic Results (values 0,1,2)")
        
with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")
        
with col3:
        exang = st.number_input("Exercise Induced Angina")
        
with col1:
        oldpeak= st.number_input("ST depression induced by exercise relative to rest")
        
with col2:
        slope = st.number_input("The slope of the peak exercise ST segment")
        
with col3:
        ca = st.number_input("Number of Major Vessels (0-3) colored by flourosopy")
        
with col1:
        thal = st.number_input("Thalassemia (0,1,2)")
        
    #Code For Prediction
Heart_diagnosis = ''
     
     #Creating a Button For Prediction
     
if st.button("Heart Test Result"):
         Heart_Prediction = Heart_Disease_model.predict([[ int(age),int (sex),int (cp),int (trestbps),int (chol),int (fbs),int (restecg),int (thalach),
                                                          int (exang),int (oldpeak), int (slope),int (ca),int (thal )]])
         if (Heart_Prediction[0]==1):
             Heart_diagnosis='The Person Has Heart Issues'
         else:
             Heart_diagnosis = 'The Person Has Healthy Heart'
st.success(Heart_diagnosis)
        