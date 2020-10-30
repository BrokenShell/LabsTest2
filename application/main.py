from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field, validator
from joblib import load
import pandas as pd

application = FastAPI(
    title='LabsTest - FastAPI Pipenv AWS EB',
    description='',
    version='0.1',
    docs_url='/',
)
model = load('application/model.joblib')
router = APIRouter()


class Iris(BaseModel):
    """ Example: #55 [5.7, 2.8, 4.5, 1.3] == 1 (Versicolor) @ 92.69% """
    sepal_length: float = Field(..., example=5.7)
    sepal_width: float = Field(..., example=2.8)
    petal_length: float = Field(..., example=4.5)
    petal_width: float = Field(..., example=1.3)

    def to_df(self):
        return pd.DataFrame([dict(self)])

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
    def check_val(cls, value):
        assert 0 < value < 10, f'value == {value}, 0 < value < 10'
        return value


@router.post('/predict')
async def predict(iris: Iris):
    lookup = ('Setosa', 'Versicolor', 'Virginica')
    x = iris.to_df()
    y_pred, *_ = model.predict(x)
    y_prob, *_ = model.predict_proba(x)
    return {
        'prediction': lookup[y_pred],
        'confidence': f'{100 * max(y_prob):.2f}%',
    }


application.include_router(router)
