#Importing required libraries
import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

#Reading the csv file
df = pd.read_csv('Smartphones_Data.csv')

#Considering the essential features that one will look at before purchasing a mobile.   
factors = ['RAM', 'ROM', 'Front_camera', 'Battery_Capacity', 'Display_size']

#Scaling those features to bring them in the same unit.
sc = StandardScaler()
df[factors] = sc.fit_transform(df[factors])

#Setting up the page title
st.set_page_config(page_title="Phone Recommendation", layout="wide")

#Setting the background color and font
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    </style>
    """,unsafe_allow_html=True  
)

#TItle 
st.title('Select\'O Phone:iphone:')
st.subheader("Find the perfect smartphone for you!:dart::100:")

#Creating elements from where the users can give input
price = st.slider('*Budget Range*', min_value=5499, max_value=127999, value=(10000, 30000))

#Filtering out the phones according to the user's budget.
df = df[(df['After_Discount_Price']>=price[0]) & (df['After_Discount_Price']<=price[1])]

#Writing a text which asks the user to give the input
st.markdown("Please assign your importance values to each feature. The given importance values should add up to 10.")

ram = st.slider('*Performance*', min_value=0, max_value=10, value=2,step=1)
rom = st.slider('*Storage*', min_value=0, max_value=10, value=2,step=1)
cam = st.slider('*Camera*', min_value=0, max_value=10, value=2,step=1)
battery = st.slider('*Battery Performance*', min_value=0, max_value=10, value=2,step=1)
display = st.slider('*Display Size*', min_value=0, max_value=10, value=2,step=1)

#Summing up the values given by the user.
total = ram + rom + cam + battery + display

# Calculating the weighted scores for each feature that we considered.
df['Score'] = (df['RAM'] * ram) + (df['ROM'] * rom) + (df['Front_camera'] * cam) + (df['Battery_Capacity'] * battery) + (df['Display_size'] * display)

# Displaying the top 5 suggestions to the user
if st.button('Recommend'):

    #Checking if the summed up values given by user are equal to 10.
    if total == 10:
        
        #Transforming the data back to it's initial units, so that user can understand.
        df[factors] = sc.inverse_transform(df[factors])
        
        #Since the features are inverse transformed, they will be of float datatype.
        #Converting the datatype to 'int'.
        df[factors] = df[factors].astype('int')

        #Retriving the phones from each brand.
        new_df = df.groupby('Brand').first()
        new_df.reset_index(inplace=True)

        # Sorting the dataFrame by score in descending order.
        new_df = new_df.sort_values('Score', ascending=False)

        #Displays the below message. 
        st.success("Based on your preferences, I recommend you these following phones.")

        #Adjusting the horizontal layout to display the recommended results.
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.subheader("Phone 1")
            row = new_df.iloc[0]
            st.image(row['Product_Image'])
            st.write(f"{row['Product_name']}")
            st.write(f"Price: ₹{row['After_Discount_Price']}")
            st.write(f"RAM: {row['RAM']}GB")
            st.write(f"ROM: {row['ROM']}GB")
            st.write(f"Camera: {row['Front_camera']}MP")
            st.write(f"Battery: {row['Battery_Capacity']}mAH")
        
        #According to the results that are recommended, the layout and output varies.
        if len(new_df) > 1:
            with col2:
                st.subheader("Phone 2")
                row = new_df.iloc[1]
                st.image(row['Product_Image'])
                st.write(f"{row['Product_name']}")
                st.write(f"Price: ₹{row['After_Discount_Price']}")
                st.write(f"RAM: {row['RAM']}GB")
                st.write(f"ROM: {row['ROM']}GB")
                st.write(f"Camera: {row['Front_camera']}MP")
                st.write(f"Battery: {row['Battery_Capacity']}mAH")
        else:
            st.empty()
            
        if len(new_df) > 2:
            with col3:
                st.subheader("Phone 3")
                row = new_df.iloc[2]
                st.image(row['Product_Image'])
                st.write(f"{row['Product_name']}")
                st.write(f"Price: ₹{row['After_Discount_Price']}")
                st.write(f"RAM: {row['RAM']}GB")
                st.write(f"ROM: {row['ROM']}GB")
                st.write(f"Camera: {row['Front_camera']}MP")
                st.write(f"Battery: {row['Battery_Capacity']}mAH")
        else:
            st.empty()

        if len(new_df) > 3:
            with col4:
                st.subheader("Phone 4")
                row = new_df.iloc[3]
                st.image(row['Product_Image'])
                st.write(f"{row['Product_name']}")
                st.write(f"Price: ₹{row['After_Discount_Price']}")
                st.write(f"RAM: {row['RAM']}GB")
                st.write(f"ROM: {row['ROM']}GB")
                st.write(f"Camera: {row['Front_camera']}MP")
                st.write(f"Battery: {row['Battery_Capacity']}mAH")
        else:
            st.empty()

        if len(new_df) > 4:   
           with col5:
               st.subheader("Phone 5")
               row = new_df.iloc[4]
               st.image(row['Product_Image'])
               st.write(f"{row['Product_name']}")
               st.write(f"Price: ₹{row['After_Discount_Price']}")
               st.write(f"RAM: {row['RAM']}GB")
               st.write(f"ROM: {row['ROM']}GB")
               st.write(f"Camera: {row['Front_camera']}MP")
               st.write(f"Battery: {row['Battery_Capacity']}mAH")
        else:
            st.empty()

    #If the given input doesn't add up to 1. The error is raised.
    else:
        st.error('Oops! Given importance values are not adding up to 10',icon='🚨')
else:
    pass