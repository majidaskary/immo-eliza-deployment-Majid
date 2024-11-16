from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from predict import predict
#from predict import preprocessing
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# Initialize FastAPI app
app = FastAPI()

# Input data model using Pydantic
class InputData(BaseModel):
    property_type: Literal["apartment", "house"]
    # zip_code_cut            # //  
    total_area_sqm: int
    nbr_bedrooms: int
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
  

@app.get("/")
def form_page():      
   return {"welcome to immo-Code"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Redirect from GET to POST for /predict
# @app.get("/predict")
@app.get("/")
async def redirect_to_post():
    response = RedirectResponse(url="/predict", status_code=307)
    response.method = "POST"
    return response

@app.post("/predict")
async def prediction(data: InputData):     # asynd def is an asynchronous function 
    # Get the prediction result after preprocessing
    result = predict(data.property_type, data.total_area_sqm, data.nbr_bedrooms)
    # result = preprocessing(data.property_type, data.zip_code_cut, data.total_area_sqm, 
    #                 data.nbr_bedrooms,data.construction_category, data.Bulding_sta_encoded,
    #                 data.kitchen_type_encoded, data.epc_encoded, data.terrace, terrace_sqm,
    #                 data.fl_furnished, data.garden, data.garden_sqm, data.surface_land_sqm, 
    #                 data.nbr_frontages)

    # Return the result
    if "error" in result:
        return {"error": result["error"]}
    else:
        return {"prediction": result["prediction"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)



# Adding CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to the specific Streamlit URL
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allow all HTTP headers
)



