import pickle
import os
import gc

# Function to load a model using pickle
def load_model(model_path):
    print(f"Loading model from: {model_path}")
    if not os.path.exists(model_path):
        print(f"Model file not found: {model_path}")
        return None

    try:
        # Clear memory cache
        gc.collect()
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        print(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Load apartment and house models
apartment_model = load_model('gb.LGBM_Regressor_Apartment.pkl')
house_model = load_model('gb.LGBM_Regressor_House.pkl')

# Prediction function
def predict_price(property_type, total_area_sqm, nbr_bedrooms):
    # Select the appropriate model
    model = apartment_model if property_type == "apartment" else house_model

    if model is None:
        return {"error": "Model not loaded"}

    # Prepare the input features
    features = [total_area_sqm, nbr_bedrooms]
    try:
        # Make prediction
        prediction = model.predict_price([features])[0]
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}

#def preprocessing(property_type, zip_code_cut, total_area_sqm, nbr_bedrooms,
    #                 construction_category, Bulding_sta_encoded, kitchen_type_encoded, epc_encoded, 
    #                 terrace, terrace_sqm, fl_furnished, garden, garden_sqm, surface_land_sqm, nbr_frontages):
def preprocessing():
    # property_type: Literal["apartment", "house"]
    # zip_code_cut            # //  
    # total_area_sqm: int
    # nbr_bedrooms: int
    # construction_category   # encode or ordinary ?
    # Bulding_sta_encoded     # encode
    # kitchen_type_encoded    # encode
    # epc_encoded             # ordinary
        
    ### only for apartment
    # terrace
    # terrace_sqm             # ?
    # fl_furnished

    ### only for house
    # garden
    # garden_sqm              # ?
    # surface_land_sqm        # ?
    # nbr_frontages
 
    ### new feature to generate
    #total_area_per_bedroom_scaled      # from "total_area_sqm" and "nbr_bedrooms"
    pass