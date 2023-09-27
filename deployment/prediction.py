# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Config the page
st.set_page_config(
    page_title ='Customer Churn - Predictor',
    layout='wide',
)

# load file
with open('model.pkl', 'rb') as file_1 :
    model = pickle.load(file_1)

# Create run function
def run():
    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h1 class="centered-text">Customer Churn Prediction</h1>', unsafe_allow_html=True)

    # Add an Image
    st.image('prediction_banner.jpg')

    # The model Description
    st.write("""
            The Customer Churn Prediction App is a web-based application designed to \
            assist businesses in identifying and reducing customer churn. The app leverages advanced machine learning algorithms to analyze customer behavior, transaction history, and other pertinent data, enabling businesses to predict which customers are at risk of churning.

            By identifying potential churners in advance, the app empowers businesses to \
            proactively implement targeted marketing strategies and retention initiatives. This proactive approach can help retain valuable customers and optimize customer satisfaction, ultimately contributing to the long-term success and growth of the business.

            The Customer Churn Prediction App equips businesses with the insights they need \
            to make data-driven decisions, enhance customer loyalty, and ensure a thriving customer base.""")

    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h3 class="centered-text">Customer Profile</h3>', unsafe_allow_html=True)
    st.markdown('---')

    # Create a table feature
    col1, col2 = st.columns(2)

    # content column 1
    with col1:
        # Add an Image
        st.image('3.jpg', use_column_width='always')

    # content column 2
    with col2:
        # input form part 1
        id = st.text_input('Customer ID', value="00000", help='Fill with 5 digit of customer id')
        sex = st.selectbox('Gender',('Male','Female'), index=0)
        marital = st.selectbox('Marital Status', ['Single', 'Divorced', 'Married'], index=0)
        login_device = st.selectbox('Preferred Login Device', ['Phone', 'Computer'], index=0)
        citytier = st.select_slider('Choose the City Tier', options=[1,2,3], 
                                    help='City Tier 1: "Major", City Tier 2: "Secondary", City Tier 3: "Small"')
        paymentmode = st.selectbox('Preferred Payment Method', ['Debit Card', 'UPI', 
                                                                'Cash on Delivery', 'E wallet', 'COD', 'Credit Card'], 
                                index=0)

    # horizontal line
    st.markdown('***')

    # Create a table feature
    col1, col2 = st.columns(2)

    # content column 1
    with col2:
        # Add an Image
        st.image('4.jpg', use_column_width='always')

    # content column 2
    with col1:
        # input form part 2
        distance = st.slider('How far customer place from warehouse?', 0, 250, 5, help='Just estimation in kilometers')
        tenure = st.number_input('How long customer have been using the app', min_value=0, value=0,step=1, help="in months")
        spend = st.select_slider('How many hours customer on App?', options=[0.0, 1.0,2.0,3.0, 4.0, 5.0], 
                                    help='just in average hours')
        order_cat = st.selectbox('Prefered Order Category', ['Laptop & Accessory', 'Mobile', 'Others', 'Fashion', 'Grocery'], 
                                index=0)
        score = st.select_slider('Rate the satisfaction score?', options=[1,2,3,4,5])
        devices = st.number_input('Number Of Device Registered', min_value=1, max_value=50, value=1,step=1)

    # horizontal line
    st.markdown('***')

    # Create a table feature
    col1, col2 = st.columns(2)

    # content column 1
    with col1:
        # Add an Image
        st.image('5.jpg', use_column_width='always')

    # content column 2
    with col2:
        # input form part 2
        address = st.number_input('Number Of Address Registered', min_value=1, max_value=50, value=1,step=1)
        complain = 1 if st.selectbox('Did customer raised complain last month?',('Yes','No'), index=0) == 'Yes' else 0
        coupon = st.slider('How many coupon customer use last month?', 0, 25, 0)
        hike_order = st.number_input('Percentage increases in order from last year', min_value=0.0, 
                                    max_value=None, value=0.0,step=0.1)
        order_count = st.slider('Total number of orders has been places in last month', 0, 25, 0)

    day_lastOrder = st.number_input('Days Since last order by customer', min_value=0, max_value=50, value=0,step=1)
    cashback = st.number_input('Average cashback in last month', min_value=0, value=1, step=10, help='In dollars')


    # Create a dataframe
    feature = pd.DataFrame({
        'CustomerID': id, 
        'Tenure': tenure, 
        'PreferredLoginDevice': login_device, 
        'CityTier': citytier,
        'WarehouseToHome': distance, 
        'PreferredPaymentMode': paymentmode, 
        'Gender': sex, 
        'HourSpendOnApp': spend ,
        'NumberOfDeviceRegistered': devices, 
        'PreferedOrderCat': order_cat, 
        'SatisfactionScore':score,
        'MaritalStatus': marital, 
        'NumberOfAddress': address, 
        'Complain': complain,
        'OrderAmountHikeFromlastYear': hike_order, 
        'CouponUsed': coupon, 
        'OrderCount': order_count,
        'DaySinceLastOrder': day_lastOrder, 
        'CashbackAmount':cashback
    }, index=[0])

    # Predict button
    pred_process = st.button("Predict", use_container_width=True, type='primary')

    # The prediction process
    if pred_process:
        # Predict Inference set
        y_result = model.predict(feature)

        # Give the label
        if y_result == 1:
            # Create a table feature
            col1, col2 = st.columns(2)
            # content column 1
            with col1:
                # Add an Image
                st.image('7.png', use_column_width='always')

            # content column 2
            with col2:
                st.markdown("""
                <style>
                .centered-text {
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)

                # Write the churn prediction
                st.markdown('<h2 class="centered-text">Customer Probably will Churn</h2>', unsafe_allow_html=True)
        else:
            # Create a table feature
            col1, col2 = st.columns(2)
            # content column 1
            with col1:
                # Add an Image
                st.image('6.png', use_column_width='always')

            # content column 2
            with col2:
                st.markdown("""
                <style>
                .centered-text {
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    top: 50%;
                }
                </style>
                """, unsafe_allow_html=True)

                # Write the churn prediction
                st.markdown('<h2 class="centered-text">Customer Probably will Stay/Loyal</h2>', unsafe_allow_html=True)

if __name__== '__main__':
    run()