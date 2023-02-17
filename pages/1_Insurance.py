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
insurance_premium_info=pd.read_excel('./data/insurance_premium_info.xlsx')

st.write("# Here is your disease-specific insurance policy information. \n **Please check the following.**")
st.write('---')
st.write("##### Please enter your age and desired insurance premium in the following fields.")

# Get the user inputs
age = st.number_input("Please enter your age", value=0)
insurance_amount = st.number_input("Please enter the desired insurance amount", value=0)


if st.button("Submit"):
    st.write("### DATA for INSURANCE:")
    st.dataframe(insurance_premium_info)
    st.write('#### RESULT')
    st.write('---')


    if 19<age<30 or 39<age<50:
        ipc_df=Insurance_function.calculator(insurance_premium, prediction_proba, age,insurance_amount)
        
        if ipc_df.iloc[5,0]=='0원':
            print('설정한 최소 보험료가 너무 낮습니다. 계산된 최소 보험료 : %s'%ipc_df.iloc[5,1])
            
        else:
            st.dataframe(ipc_df)
        
    else:
        print('죄송합니다. 현재 고객님을 위한 상품이 준비되어 있지 않습니다.')
        print('현재 저희는 20대와 40대를 위한 상품만 제공되고 있습니다.')
    


    #### 보험 #### 

