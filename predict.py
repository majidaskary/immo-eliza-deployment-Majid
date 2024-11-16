# predict.py

import joblib
import os
import gc

# Function to load a model using joblib
def load_model(model_path):
    """
    Load a model from the specified file path using joblib.
    """
    print(f"Loading model from: {model_path}")
    if not os.path.exists(model_path):
        print(f"Model file not found: {model_path}")
        return None

    try:
        # Clear memory cache
        gc.collect()
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Load apartment and house models
apartment_model = load_model('gb.LGBM_Regressor_Apartment.joblib')
house_model = load_model('gb.LGBM_Regressor_House.joblib')

# Prediction function
def predict(property_type, total_area_sqm, nbr_bedrooms):
    """
    Make a prediction based on the property type, total area in square meters,
    and number of bedrooms.
    """
    # Select the appropriate model based on property type
    if property_type.lower() == "apartment":
        model = apartment_model
    elif property_type.lower() == "house":
        model = house_model
    else:
        return {"error": "Invalid property type. Use 'apartment' or 'house'."}

    # Check if the model is loaded
    if model is None:
        return {"error": "Model not loaded"}

    # Prepare the input features
    features = [total_area_sqm, nbr_bedrooms]
    try:
        # Make prediction
        prediction = model.predict([features])[0]
        return {"prediction": round(prediction, 2)}
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}



#--------------------------------------------------
# import joblib

# # Load models
# apartment_model = joblib.load("gb.LGBM_Regressor_Apartment.pkl")
# house_model = joblib.load("gb.LGBM_Regressor_House.pkl")

# # Prediction function
# def predict(property_type, total_area_sqm, nbr_bedrooms):
#     try:
#         # Choose model based on property type
#         if property_type.lower() == "apartment":
#             prediction = apartment_model.predict([[total_area_sqm, nbr_bedrooms]])[0]
#         elif property_type.lower() == "house":
#             prediction = house_model.predict([[total_area_sqm, nbr_bedrooms]])[0]
#         else:
#             return {"error": "Invalid property type"}
        
#         return {"prediction": prediction}
#     except Exception as e:
#         return {"error": str(e)}


#----------------------------------------------------------------
# import pickle
# import os
# import gc


# # Function to load a model using pickle
# def load_model(model_path):
#     print(f"Loading model from: {model_path}")
#     if not os.path.exists(model_path):
#         print(f"Model file not found: {model_path}")
#         return None

#     try:
#         # Clear memory cache
#         gc.collect()
#         with open(model_path, 'rb') as file:
#             model = pickle.load(file)
#         print(f"Model loaded successfully from {model_path}")
#         return model
#     except Exception as e:
#         print(f"Error loading model: {e}")
#         return None

# # Load apartment and house models
# apartment_model = load_model('gb.LGBM_Regressor_Apartment.pkl')
# house_model = load_model('gb.LGBM_Regressor_House.pkl')

# # Prediction function
# def predict(property_type, total_area_sqm, nbr_bedrooms):
#     # Select the appropriate model
#     model = apartment_model if property_type == "apartment" else house_model

#     if model is None:
#         return {"error": "Model not loaded"}

#     # Prepare the input features
#     features = [total_area_sqm, nbr_bedrooms]
#     try:
#         # Make prediction
#         prediction = model.predict([features])[0]
#         return {"prediction": prediction}
#     except Exception as e:
#         return {"error": str(e)}

# #def preprocessing(property_type, zip_code_cut, total_area_sqm, nbr_bedrooms,
#     #                 construction_category, Bulding_sta_encoded, kitchen_type_encoded, epc_encoded, 
#     #                 terrace, terrace_sqm, fl_furnished, garden, garden_sqm, surface_land_sqm, nbr_frontages):
# def preprocessing():
#     # property_type: Literal["apartment", "house"]
#     # zip_code_cut            # //  
#     # total_area_sqm: int
#     # nbr_bedrooms: int
#     # construction_category   # encode or ordinary ?
#     # Bulding_sta_encoded     # encode
#     # kitchen_type_encoded    # encode
#     # epc_encoded             # ordinary
        
#     ### only for apartment
#     # terrace
#     # terrace_sqm             # ?
#     # fl_furnished

#     ### only for house
#     # garden
#     # garden_sqm              # ?
#     # surface_land_sqm        # ?
#     # nbr_frontages
 
#     ### new feature to generate
#     #total_area_per_bedroom_scaled      # from "total_area_sqm" and "nbr_bedrooms"
#     pass