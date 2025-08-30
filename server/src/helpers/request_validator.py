from pydantic import BaseModel
from typing import Annotated
from annotated_types import Len

class PredictionRequest(BaseModel):
  matrix: Annotated[list[int], Len(min_length=784, max_length=784)]
