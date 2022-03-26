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

#real news
#"text": "they are all treasonous lying narcissistical sociopathic bastardswhen trump says they need to drain the swamp or whateverhes not wrong but whos going to have hes back when hes dredging the filth out of the swamp that is political washington and all the corporate skid marks along with the corrupt banksters and especially the fed reservewho"
def predict(text):
    print(f"Accepted payload: {text}")
    my_data = {
        "author": {0: "Jacques de Seingalt"},
        "published": {0: "2016-11-24T03:01:28.961+02:00"},
        "title": {0: "an exploration of finding meaning in life through logotherapy"},
        "text": {0: text},
        "language": {0: "english"},
        "site_url": {0: "returnofkings.com"},
        "main_img_url": {0: "No Image URL"},
        "type": {0: "hate"},
        "title_without_stopwords": {0: "ugly truth six leftist heroes"},
        "text_without_stopwords": {0: "saker message current saker messages russia celebrates unity day liberation moscow polish roman papists army views november comments scotts corner scott national unity day first celebrated november commemorates popular uprising lead prince dmitry pozharsky meat merchant kuzma minin ejected alien occupying forces polish roman papists army moscow november generally end time troubles foreign interventions russia name alludes idea classes russian society willingly united preserve russian statehood demise seemed inevitable even though neither tsar patriarch guide recently episode made russian movie minin pozharsky liberation moscow triptych russian land artist yuri pantyukhin russia muscovites celebrate unity day capital river dance simferopol crimea russia putin patriarch kirill bless new monument vladimir great nov president vladimir putin unveiled new monument russias first christian leader vladimir great moscow friday opening ceremony took place meters kremlin walls coincided russian national unity day vladimir putin russian president russian holiness respected muscovites dear friends greet congratulate opening monument saint equaltoapostles prince vladimir big significant event moscow whole country russian compatriots symbolic held national unity day centre capital near walls ancient kremlin heart russia vladimir putin russian president russian strong moral support cohesion unity helped ancestors overcome difficulties live win glory fatherland strengthen power greatness generation generation today duty stand together modern threats challenges basing spiritual precepts invaluable traditions unity concord move forward ensuring continuity thousandyear history patriarch kirill moscow russia russian monument prince vladimir symbol unity peoples farther peoples historical rus currently living within borders many states monument farther may everywhere children live contradiction bad children forget father essential saker trenches emerging multipolar world first comment leave reply click get info formatting leave name field empty want post anonymous preferable choose name becomes clear said email address mandatory either website automatically checks spam please refer moderation policies details check make sure comment mistakenly marked spam takes time effort please patient comment appears thanks replies comment maximum formating examples use writingbbold textb results bold text iitalic texti results italic text also combine two formating tags example get bolditalic textememphasized textem results emphasized text strongstrong textstrong results strong text qa quote textq results quote text quotation marks added automatically citea phrase block text needs citedcite results phrase block text needs cited blockquotea heavier version quoting block textblockquote results heavier version quoting block text span several lines use possibilities appropriately meant help create follow discussions better way assist grasping content value comment quickly last leasta hrefhttplinkaddresscomname linka results name link need use special character paragraphs need anymore write like paragraphs separated live preview appears automatically start typing text area show comment look like send think confusing ignore code write like search articles"},
        "hasImage": {0: 0},
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