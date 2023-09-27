# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# function to run the program
def run():
    # Create title
    st.title('Exploratory Data Analysis')

    # Create a sub header
    st.subheader('E-Commerce Churn Customer Analysis')

    # Add an Image
    st.image('eda_banner.png')

    # Load the csv file
    data_viz = pd.read_csv('ecommerce.csv', sep=';')

    # Create canvas
    fig = plt.figure(figsize=(6, 5))

    # Check the churn
    data_viz['Churn'].value_counts().plot(kind='bar', rot=0)

    # Adding annotations to the bars in Subplot 3
    for p in plt.gca().patches:
        plt.gca().annotate(str(int(p.get_height())), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
        xytext=(0, 5), textcoords='offset points')

    # Set labels and title
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.title('Churn Distribution')

    # Show the plots
    st.pyplot(fig)
    st.write('#### The data shows there are 948 e-commerce customer \
            that churn or about 16.83%')
    
    # Create separator
    st.markdown('---')

    # Interactive Histogram
    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h3 class="centered-text">Interactive Visualization</h3>', 
                unsafe_allow_html=True)
    option = st.selectbox('Select the column :', ('WarehouseToHome','OrderAmountHikeFromlastYear','CashbackAmount'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data_viz[option],bins=30,kde=True)
    st.pyplot(fig)

    # Create separator
    st.markdown('---')

    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h3 class="centered-text">Churn and Non-Churn Customer Characteristic</h3>', 
                unsafe_allow_html=True)

    # Create subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

    # Churned customers
    churn_cust = data_viz[data_viz['Churn'] == 1]

    # Gender distribution - Churn
    churn_gender_counts = churn_cust['Gender'].value_counts()
    axes[0, 0].pie(churn_gender_counts, labels=churn_gender_counts.index, 
                autopct='%1.1f%%', startangle=90)
    axes[0, 0].set_title('Gender Distribution - Churn')

    # Marital status - Churn
    churn_marital_counts = churn_cust['MaritalStatus'].value_counts().sort_values()
    axes[0, 1].barh(churn_marital_counts.index, churn_marital_counts.values)
    axes[0, 1].set_title('Marital Status - Churn')

    # Non-churned customers
    not_churn = data_viz[data_viz['Churn'] == 0]

    # Gender distribution - Not Churn
    not_churn_gender_counts = not_churn['Gender'].value_counts()
    axes[1, 0].pie(not_churn_gender_counts, labels=not_churn_gender_counts.index, 
                autopct='%1.1f%%', startangle=90)
    axes[1, 0].set_title('Gender Distribution - Not Churn')

    # Marital status - Not Churn
    not_churn_marital_counts = not_churn['MaritalStatus'].value_counts().sort_values()
    axes[1, 1].barh(not_churn_marital_counts.index, not_churn_marital_counts.values)
    axes[1, 1].set_title('Marital Status - Not Churn')

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    st.pyplot(fig)
    st.write('''
             **Churn Customer**
             - Most of the churn customers are male
             - Where the majority of them is single
             
             **Non-Churn Customer**
             - Still dominated by Male
             - But most of them are married''')

    # Create separator
    st.markdown('---')

    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h3 class="centered-text">Hours Spend on App</h3>', 
                unsafe_allow_html=True)

    # Define figure size
    fig = plt.figure(figsize=(10, 5))

    # the distribution of observations
    sns.countplot(data=data_viz, x=data_viz['HourSpendOnApp'])
    plt.title('Histogram')

    # Show the plots
    st.pyplot(fig)
    st.write('''**Churn Customers**
    - Most of them spend their time on app 3 hours
    - with mean score around 2.9 hours''')

    # Create separator
    st.markdown('---')

    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h3 class="centered-text">City Tier</h3>', unsafe_allow_html=True)

    # Define figure size
    fig = plt.figure(figsize=(10, 8))

    # the distribution of observations
    sns.countplot(data=data_viz, x=data_viz['CityTier'], hue='Churn')
    plt.title('Histogram')

    # Show the plots
    st.pyplot(fig)
    st.write('''
            - If we looked from the bar chart above, most of them is\
            stay in City tier 1 and tier 3
            - No differences in city tier rank if we group the \
            data based on who are churn and not churn. The first position still \
            at city tier 1 and followed by city tier 3''')

    # Create separator
    st.markdown('---')

    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h3 class="centered-text">Device and The Payment Method - Churn Customer</h3>', 
                unsafe_allow_html=True)

    # Combine Values
    churn_cust['PreferredPaymentMode'] = churn_cust['PreferredPaymentMode'].str.replace('CC', 'Credit Card', n=1).str.replace('COD', 'Cash on Delivery', n=1).astype('str')
    churn_cust['PreferredLoginDevice'] = churn_cust['PreferredLoginDevice'].replace('Mobile Phone', 'Phone')

    # Create canvas
    fig = plt.figure(figsize=(16,6))

    # Subplot contains pie chart
    plt.subplot(1,2,1)
    plt.pie(churn_cust['PreferredLoginDevice'].value_counts(), labels = churn_cust['PreferredLoginDevice'].value_counts().index, autopct='%1.1f%%', startangle=90)
    plt.title("Preferred login device of customer", fontsize=15)

    # subplot contains horizontal barchart
    plt.subplot(1,2,2)
    churn_cust['PreferredPaymentMode'].value_counts().sort_values().plot(kind='barh')
    plt.title("Preferred payment method of customer", fontsize=15)

    # Show the plots
    st.pyplot(fig)
    st.write('''
             **Churn Customers:**
             - They prefer to access via phone compared to their computer.
             - Payment method is dominated by Debit Card, followed by Credit Card.''')

if __name__== '__main__':
    run()