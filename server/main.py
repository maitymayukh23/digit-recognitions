from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.configurations.config import SYSTEM_CONFIG
from src.helpers.request_validator import PredictionRequest
from src.controller.prediction_controller import PredictionController

app = FastAPI()
prediction_controller = PredictionController()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[SYSTEM_CONFIG.get("FE_URL")],  # Or specify your frontend URL(s)
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/")
def read_root():
  return {"message": "Hello, World!"}


@app.post("/predict")
async def predict(request: PredictionRequest):
  matrix = request.matrix
  return prediction_controller.prediction(matrix)


if __name__ == "__main__":
  uvicorn.run("main:app", host=SYSTEM_CONFIG.get("HOST"), port=SYSTEM_CONFIG.get("PORT"), reload=True)
