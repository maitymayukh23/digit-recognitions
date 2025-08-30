from src.helpers.response_template import Response
from src.service.prediction_service import PredictionService


class PredictionController:
  prediction_service = None

  def __init__(self):
    self.prediction_service = PredictionService()

  def prediction(self, matrix):
    try:
      computed_prediction, predicted_number = self.prediction_service.prediction(matrix)
      result = self.prediction_service.prediction_to_percentages(computed_prediction)
      res = {
        "predicted_number": predicted_number,
        "percentages": result
      }
      return Response(success=True, message="Prediction successful", data=res)
    except Exception as e:
      print(e)
      return Response(success=False, message=str(e))
