from fastapi import *
from states import get_address
from pydantic import BaseModel
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware

translator = Translator()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class message(BaseModel):
    text: str
    lang: str


@app.get("/translater")
async def translater(msg,lang):
    result = translator.translate(msg,dest=lang)
    return str(result.text)


@app.get("/translation")
async def translation(msg,lang):
    res = []
    messages = msg.split(",")
    for a in messages:
        res.append(translator.translate(a,dest=lang).text)
    return res

@app.get("/address")
async def getAddress(pincode,lang):
    res = []
    result1 = translator.translate("The Nearest Store is : ",dest=lang).text
    messages = get_address(int(pincode))
    for a in messages:
        res.append(translator.translate(a,dest=lang).text)
    return result1 + res[0]