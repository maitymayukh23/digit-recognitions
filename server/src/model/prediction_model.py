import json
import os
import numpy as np


class PredictionModel:
  w1 = None
  w2 = None
  b1 = None
  b2 = None

  def __init__(self) -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, '../notebooks/model_params.json')
    with open(json_path, "r") as f:
      params = json.load(f)

    self.w1 = np.array(params["W1"])
    self.b1 = np.array(params["b1"])
    self.w2 = np.array(params["W2"])
    self.b2 = np.array(params["b2"])

  def __forward_propagation(self, matrix, w1, b1, w2, b2):
    z1 = np.dot(w1, matrix) + b1
    a1 = self.__ReLU(z1)
    z2 = np.dot(w2, a1) + b2
    a2 = self.__softmax(z2)
    return a2

  def __ReLU(self, z):
    return np.maximum(0, z)

  def __softmax(self, z):
    exp_x = np.exp(z - np.max(z))
    sum_exp_x = exp_x.sum(axis=0, keepdims=True)
    return exp_x / (sum_exp_x + 1e-8)

  def prediction(self, current_image: np.ndarray):
    try:
      print(current_image.shape)
      a2 = self.__forward_propagation(current_image, self.w1, self.b1, self.w2, self.b2)
      predicted_number = np.argmax(a2, axis=0)
      return a2, predicted_number
    except Exception as e:
      print(e)
      raise e
