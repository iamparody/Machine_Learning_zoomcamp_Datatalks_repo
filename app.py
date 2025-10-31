from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Define input schema
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Load the model
with open("pipeline_v1.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

# Create FastAPI app
app = FastAPI()

# Define endpoint
@app.post("/predict")
def predict(lead: Lead):
    record = lead.dict()
    probability = pipeline.predict_proba([record])[0, 1]
    return {"conversion_probability": probability}
