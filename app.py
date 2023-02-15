import streamlit as st
import joblib
import pandas as pd
from SMCluster import smC_v2

# Load the model
loaded_model = joblib.load('model.txt')
target = ['B형간염', '뇌졸중', '협심증또는심근경색증', '고혈압&당뇨']

# Create the main function
def main():
    st.title('LightGBM Model Predictor')

    # Get the user inputs
    HE_glu = st.number_input(smC_v2().trans('HE_glu'), value=0.0)
    HE_dbp = st.number_input(smC_v2().trans('HE_dbp'), value=0.0)
    HE_sbp = st.number_input(smC_v2().trans('HE_sbp'), value=0.0)

    st.write('Disease : B형간염 / 뇌졸중 / 협심증또는심근경색증 / 고혈압&당뇨')

    # Predict the target
    if st.button('Predict'):
        prediction = loaded_model.predict([[HE_glu, HE_dbp, HE_sbp]])
        st.write('The predicted target is:', target[int(prediction)])

# Run the main function
if __name__ == '__main__':
    main()
