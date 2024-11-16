
# streamlit.py

import streamlit as st
from predict import predict

# Streamlit app
st.title("Immo-Code Prediction App")

property_type = st.selectbox("Select Property Type", ["Apartment", "House"])
total_area_sqm = st.number_input("Total Area (sqm)", min_value=10.0)
nbr_bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)

if st.button("Predict"):
    result = predict(property_type, total_area_sqm, nbr_bedrooms)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"Predicted Price: {result['prediction']}")




#----------------------------------------------------------------------------------

# import streamlit as st
# import requests


# # Title of the Streamlit app
# st.title("immo-Eliza Property Price Prediction")

# # Input fields for user data
# property_type = st.selectbox("Select Property Type", ["apartment", "house"])
# total_area_sqm = st.number_input("Enter Total Area (sqm)", min_value=0, step=1)
# nbr_bedrooms = st.number_input("Enter Number of Bedrooms", min_value=0, step=1)

# # Button to trigger prediction
# if st.button("Predict Price"):
#     # Prepare the input data for the API request
#     input_data = {
#         "property_type": property_type,
#         "total_area_sqm": total_area_sqm,
#         "nbr_bedrooms": nbr_bedrooms,
#         # property_type: 
#         # "zip_code_cut" :           
#         # "total_area_sqm": 
#         # "nbr_bedrooms": 
#         # "construction_category"   
#         # "Bulding_sta_encoded"     
#         # "kitchen_type_encoded"    
#         # "epc_encoded"             
            
#         ### only for apartment
#         # "terrace"
#         # "terrace_sqm"             
#         # "fl_furnished"

#         ### only for house
#         # "garden"
#         # "garden_sqm"             
#         # "surface_land_sqm"        #
#         # "nbr_frontages"
    
#         ### new feature to generate
#         #total_area_per_bedroom_scaled      # from "total_area_sqm" and "nbr_bedrooms"
#     }

#     # Send a POST request to the FastAPI backend    
#     try:
#         # api_url = "https://immo-code.onrender.com/predict"
#         response = requests.post("http://localhost:8000/predict", json=input_data)
#         # response = requests.post("https://immo-code.onrender.com/predict", json=input_data)
#         # Check the response
#         if response.status_code == 200:
#             result = response.json()
#             if "prediction" in result:
#                 st.success(f"Predicted Price: ${result['prediction']:.2f}")
#             else:
#                 st.error(f"Error: {result.get('error', 'Unknown error')}")
#         else:
#             st.error("Failed to get a response from the API.")
#     except Exception as e:
#         st.error(f"Request failed: {e}")
