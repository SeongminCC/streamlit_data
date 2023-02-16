import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from SMCluster import smC_v2


# Load the model
loaded_model = joblib.load('model_10.txt')
target = ['B형간염', '뇌졸중', '협심증또는심근경색증', '고혈압&당뇨']

def create_bar_graph(data):
    plt.bar(range(len(data)), data)
    plt.show()

def get_prediction_proba():
    global prediction_proba
    return prediction_proba

# Create the main function
def main():
    global prediction_proba
    st.title('Please Enter your *HEALTH METRICS*')

    # Get the user inputs
    HE_glu = st.number_input(smC_v2().trans('HE_glu'), value=0.0)
    HE_dbp = st.number_input(smC_v2().trans('HE_dbp'), value=0.0)
    HE_sbp = st.number_input(smC_v2().trans('HE_sbp'), value=0.0)
    HE_HbA1c = st.number_input(smC_v2().trans('HE_HbA1c'), value=0.0)
    HE_wc = st.number_input(smC_v2().trans('HE_wc'), value=0.0)
    HE_BMI = st.number_input(smC_v2().trans('HE_BMI'), value=0.0)
    HE_ht = st.number_input(smC_v2().trans('HE_ht'), value=0.0)
    EC_wht_23 = st.number_input(smC_v2().trans('EC_wht_23'), value=0.0)
    HE_wt = st.number_input(smC_v2().trans('HE_wt'), value=0.0)
    HE_fst = st.number_input(smC_v2().trans('HE_fst'), value=0.0)


    st.markdown("B형간염 / 뇌졸중 / 협심증또는심근경색증 / 고혈압&당뇨")

    
    # Predict the target
    if st.button('Predict'):
        global prediction_proba
        prediction = loaded_model.predict([[HE_glu, HE_dbp, HE_sbp, HE_HbA1c, HE_wc, HE_BMI, HE_ht, EC_wht_23, HE_wt, HE_fst]])
        st.write('The predicted target is:', target[int(prediction)])

        prediction_proba = loaded_model.predict_proba([[HE_glu, HE_dbp, HE_sbp, HE_HbA1c, HE_wc, HE_BMI, HE_ht, EC_wht_23, HE_wt, HE_fst]])
        st.write("---")
        st.write("B형간염: {:.2f}%".format(prediction_proba[0][0]*100))
        st.write("뇌졸중: {:.2f}%".format(prediction_proba[0][1]*100))
        st.write("협심증또는심근경색증: {:.2f}%".format(prediction_proba[0][2]*100))
        st.write("고혈압&당뇨: {:.2f}%".format(prediction_proba[0][3]*100))

        st.title("Visualization")
        fig = fig = px.bar(x=target, y=prediction_proba[0], color=prediction_proba[0], height=400)
        st.plotly_chart(fig)
        np.save('prediction_proba.npy', prediction_proba)
        st.write("*You can now check your insurance premium.*")
        st.write("*Check out the Insurance page!*")


    
# Run the main function
if __name__ == '__main__':
    main()
