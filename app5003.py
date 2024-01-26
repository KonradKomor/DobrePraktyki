from flask import Flask, request
from pydantic import BaseModel
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

class Text(BaseModel):
    text: str

app = Flask(__name__)


@app.route('/', methods=['POST'])
def checkSentiment():
    text_data = request.json.get('text')
    text = Text(text=text_data)
    doc = nlp(text.text)
    return {"sentiment": doc._.polarity}

if __name__ == '__main__':
    app.run(port=5003, debug=True)