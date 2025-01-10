import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from PIL import Image

# Load the trained model
pickle_in = open('model_pickel', 'rb')
classifier = pickle.load(pickle_in)

# Feature columns used during training
feature_columns = ['total_sqft', 'bath', 'bhk'] + ['location1', 'location2', 'location3', '...']  # Replace with actual locations

def Welcome():
    return "WELCOME ALL!"

def predict_price(location, sqft, bath, bhk):
    """
    Predict the price of a house based on the given inputs.
    """
    # Initialize input array
    x = np.zeros(len(feature_columns))
    
    # Assign feature values
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Encode location
    if location in feature_columns:
        loc_index = feature_columns.index(location)
        x[loc_index] = 1

    # Predict price
    return classifier.predict([x])[0]

def main():
    # App title and header
    st.title("Bangalore House Price Prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;">Streamlit House Prediction ML App</h2>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Input fields
    st.subheader('Please enter the required details:')
    location = st.text_input("Location", "")
    sqft = st.text_input("Sq-ft area (numeric)", "")
    bath = st.text_input("Number of Bathrooms", "")
    bhk = st.text_input("Number of BHK", "")

    result = ""

    # Prediction button
    if st.button("Predict House Price (in Lakhs)"):
        try:
            # Convert inputs to numeric
            sqft = float(sqft)
            bath = int(bath)
            bhk = int(bhk)

            # Predict price
            result = predict_price(location, sqft, bath, bhk)
            st.success(f"The predicted price is: {result:.2f} Lakhs")
        except ValueError:
            st.error("Please enter valid numeric values for Sq-ft, Bathrooms, and BHK.")
    
    # About button
    if st.button("About"):
        st.text("Bangalore House Price Prediction App")
        st.text("Developed using Streamlit and Machine Learning.")
        st.text("Find the code at: https://github.com/Lokeshrathi/Bangalore-house-s-rate")

if __name__ == "__main__":
    main()
