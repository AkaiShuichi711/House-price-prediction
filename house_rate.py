#  PHIÊN BẢN CHẠY BẰNG TERMINAL COMAND ĐỂ TEST HÀM PREDICT
# import pandas as pd
# import numpy as np
# import pickle
# import json

# # Load the trained model
# with open('model_pickle.pkl', 'rb') as file:
#     classifier = pickle.load(file)

# # Load the feature columns
# with open('columns.json', 'r') as f:
#     feature_columns = json.load(f)

# def predict_price(location, sqft, bath, bhk):
#     """
#     Predict the price of a house based on the given inputs.
#     """
#     # Initialize input array
#     x = np.zeros(len(feature_columns))

#     # Assign feature values
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk

#     # Encode location
#     if location in feature_columns:
#         loc_index = feature_columns.index(location)
#         x[loc_index] = 1
#     else:
#         raise ValueError(f"Location '{location}' is not recognized in the training data.")

#     # Convert input to DataFrame
#     x = pd.DataFrame([x], columns=feature_columns)  # Tạo DataFrame có tên feature
    
#     # Predict price
#     return classifier.predict(x)[0]  # Truyền trực tiếp DataFrame mà không bọc thêm trong danh sách


# def main():
#     print("Bangalore House Price Prediction")
#     print("Enter the following details to predict the house price:")

#     try:
#         location = input("Enter location (e.g., '1st Phase JP Nagar'): ").strip()
#         sqft = float(input("Enter total square feet (numeric): "))
#         bath = int(input("Enter number of bathrooms: "))
#         bhk = int(input("Enter number of BHK: "))

#         result = predict_price(location, sqft, bath, bhk)
#         print(f"\nThe predicted house price is: {result:.2f} Lakhs\n")
#     except ValueError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Unexpected error: {e}")

# if __name__ == "__main__":
#     main()

#  PHIÊN BẢN CHẠY HOÀN THIỆN: CÓ UI (DEPLOY BẰNG STREAMLIT) VÀ TƯƠNG TÁC UI với DATA đã TRAIN
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load the trained model
with open('model_pickle.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Load the feature columns
with open('columns.json', 'r') as f:
    feature_columns = json.load(f)

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
    else:
        raise ValueError(f"Location '{location}' is not recognized in the training data.")

    # Convert input to DataFrame
    x = pd.DataFrame([x], columns=feature_columns)  # Tạo DataFrame có tên feature
    
    # Predict price
    return classifier.predict(x)[0]  # Truyền trực tiếp DataFrame mà không bọc thêm trong danh sách

def main():
    # Title and description
    st.title("Bangalore House Price Prediction")
    st.markdown("Please find the code at: https://github.com/AkaiShuichi711/House-price-prediction")
    st.markdown(" ")
    st.write("Enter the details below to predict the house price:")

    # User inputs
    location = st.selectbox("Select Location", feature_columns[3:])
    sqft = st.number_input("Enter Total Square Feet", min_value=0.0, step=0.1)
    bath = st.number_input("Enter Number of Bathrooms", min_value=1, step=1)
    bhk = st.number_input("Enter Number of BHK", min_value=1, step=1)

    # Button to predict
    if st.button("Predict"):
        try:
            # Make prediction
            result = predict_price(location, sqft, bath, bhk)
            st.success(f"Predicted price: {result:.2f} Lakhs")
        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Unexpected Error: {e}")
    
    



if __name__ == "__main__":
    main()
