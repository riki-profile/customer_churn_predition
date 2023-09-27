import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pages:',('Churn Predictor', 'EDA'))

if navigation == 'Churn Predictor':
    prediction.run()
else:
    eda.run()