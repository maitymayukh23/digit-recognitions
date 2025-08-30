import numpy as np

from src.model.prediction_model import PredictionModel


class PredictionService:
  prediction_model = None

  def __init__(self):
    self.prediction_model = PredictionModel()

  def prediction(self, matrix):
    try:
      input_image_matrix = np.array([[x] for x in matrix])
      input_image_matrix = input_image_matrix
      result, predicted_number = self.prediction_model.prediction(input_image_matrix)
      return result, predicted_number.tolist()
    except Exception as e:
      print(e)
      raise e

  def prediction_to_percentages(self,arr):
    arr = arr.flatten()  # shape (10,)
    max_val = arr.max()
    min_val = arr.min()
    if max_val == min_val:
      # All values are the same, set all to 100%
      return np.full((10, 1), 100.0)
    percentages = (arr - min_val) / (max_val - min_val) * 100
    percentages[arr == max_val] = 100.0
    percentages[arr == min_val] = 0.0
    return percentages.tolist()
