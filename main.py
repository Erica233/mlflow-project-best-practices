# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI
import uvicorn
import mlflow
import pandas as pd
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class Story(BaseModel):
    text: str

'''
# fake news
def predict(text):
    print(f"Accepted payload: {text}")
    my_data = {
        "author": {0: "bigjim.com"},
        "published": {0: "2016-10-27T18:05:26.351+03:00"},
        "title": {0: "aliens are coming to invade earth"},
        "text": {0: text},
        "language": {0: "english"},
        "site_url": {0: "cnn.com"},
        "main_img_url": {
         0: "https://2.bp.blogspot.com/-0mdp0nZiwMI/UYwYvexmW2I/AAAAAAAAVQM/7C_X5WRE_mQ/w1200-h630-p-nu/Edison-Stock-Ticker.jpg"
        },
        "type": {0: "bs"},
        "title_without_stopwords": {0: "aliens are coming to invade earth"},
        "text_without_stopwords": {0: "aliens are coming to invade earth"},
        "hasImage": {0: 1.0},
    }
    data = pd.DataFrame(data=my_data)
    result = loaded_model.predict(pd.DataFrame(data))
    return result
'''

#real news
#"text": "they are all treasonous lying narcissistical sociopathic bastardswhen trump says they need to drain the swamp or whateverhes not wrong but whos going to have hes back when hes dredging the filth out of the swamp that is political washington and all the corporate skid marks along with the corrupt banksters and especially the fed reservewho"
def predict(text):
    print(f"Accepted payload: {text}")
    my_data = {
        "author": {0: "Jerry Miller"},
        "published": {0: "2016-10-26T22:46:21.055+03:00"},
        "title": {0: "no title"},
        "text": {0: text},
        "language": {0: "english"},
        "site_url": {0: "westernjournalism.com"},
        "main_img_url": {
         0: "http://static.westernjournalism.com/wp-content/uploads/2016/08/sheriffjoearpaio.jpg"
        },
        "type": {0: "bias"},
        "title_without_stopwords": {0: "title"},
        "text_without_stopwords": {0: "everyone see construciton worker took drill damaged mr trumps star hollywood walk fame boy bunch evil doers bet hillary obama thugs wonder much paid balloney obama visited california yesterday coindence poor losers"},
        "hasImage": {0: 1},
    }
    data = pd.DataFrame(data=my_data)
    result = loaded_model.predict(pd.DataFrame(data))
    return result


# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')
app = FastAPI()

@app.post("/predict")
async def predict_story(story: Story):
    print(f"predict_story accepted json payload: {story}")
    result = predict(story.text)
    print(f"The result is the following payload: {result}")
    payload = {"FakeNewsTrueFalse": result.tolist()[0]}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Hello Model"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')