import os
import pickle
import sys
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Prediction of Disease Outbreaks",layout="wide")
w_d=os.path.dirname(os.path.abspath(__file__))
diabetes=pickle.load(open('diabetes_model.sav','rb'))
heart=pickle.load(open('heart_disease_model.sav','rb'))

with st.sidebar:
    selected=option_menu("Prediction of Outbreaks System",
                         ['Diabetes Prediction',
                          'Heart Disease Prediction'],
                        menu_icon='hospital-fill',
                        icons=['activity','heart'],
                        default_index=0)
if selected=="Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Preg=st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level")
    with col3:
        BP=st.text_input("BP value")
    with col1:
        Skin=st.text_input("Skin thickness")
    with col2:
        Insulin=st.text_input("Insulin Level")
    with col3:
        BMI=st.text_input("BMI level")
    with col1:
        DPF=st.text_input("Diabetes Pedigree function value")
    with col2:
        age=st.text_input("Age")
    
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[Preg,Glucose,BP,Skin,Insulin,BMI,DPF,age]
        user_input=[float(x) for x in user_input]
        diab_pred=diabetes.predict([user_input])
        if diab_pred[0]==1:
            diab_diagnosis='Person is diabetic'
        else:
            diab_diagnosis='Person is not diabetic'
    st.success(diab_diagnosis)
if selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input("Age")
    with col2:
        sex=st.text_input("Sex")
    with col3:
        chest=st.text_input("Chest pain types")
    with col1:
        BP=st.text_input("Resting BP")
    with col2:
        chol=st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs=st.text_input("Fasting sugar")
    with col1:
        ecg=st.text_input("Resting electrocardiographic result")
    with col2:
        maxrate=st.text_input("Max Hear Rate achieved")
    with col3:
        ex=st.text_input("Exercie Induced Angina")
    with col1:
        dep=st.text_input("ST depression induced ")
    with col2:
        slope=st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca=st.text_input("Major vessels colored in flourosopy")
    with col1:
        tha=st.text_input("thal: 0-normal; 1=fixed defect;2=reversable defect")


    heart_diagnosis=''
    if st.button('Heart Disease Test Result'):
        user_input=[age,sex,chest,BP,chol,fbs,ecg,maxrate,ex,dep,slope,ca,tha]
        user_input=[float(x) for x in user_input]
        heart_pred=heart.predict([user_input])
        if heart_pred[0]==1:
            heart_diagnosis='Person has heart disease'
        else:
            heart_diagnosis='Person doesnot have heart diesease'
    st.success(heart_diagnosis)

                         
