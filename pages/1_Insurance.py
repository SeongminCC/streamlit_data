import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from SMCluster import smC_v2
import Insurance_function
import numpy as np

prediction_proba = np.load('prediction_proba.npy')
prediction_proba = prediction_proba.tolist()[0]
insurance_premium=pd.read_excel('./data/insurance_premium.xlsx')

st.write("# Here is your disease-specific insurance policy information. \n **Please check the following.**")
st.write('---')
st.write("##### Please enter your age and desired insurance premium in the following fields.")

# Get the user inputs
age = st.number_input("Please enter your age", value=0)
insurance_amount = st.number_input("Please enter the desired insurance amount", value=0)


if st.button("Submit"):
    st.write("### DATA for INSURANCE:")
    st.dataframe(insurance_premium)
    st.write('#### RESULT')
    st.write('---')


    if 19<age<30 or 39<age<50:
        list_1, list_2, list_3=Insurance_function.calculator(insurance_premium, prediction_proba, age, insurance_amount)
        
        if sum(list_2)==0:
            st.write('설정한 최소 보험료가 너무 낮습니다. 계산된 최소 보험료 : %d원'%sum(list_3))
            
        else:
            for i in range(len(list_1)):
                st.write(f"**{list_1[i]} : {list_2[i]}원 / {list_3[i]}원**")
            st.write('---')
            st.write(f"**보험료 총합 : {sum(list_2)}원**")
        
    else:
        st.write('죄송합니다. 현재 고객님을 위한 상품이 준비되어 있지 않습니다.')
        st.write('현재 저희는 20대와 40대를 위한 상품만 제공되고 있습니다.')

    #### 보험 #### 

