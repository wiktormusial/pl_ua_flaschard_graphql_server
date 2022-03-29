import json
from api import db
from api.models import Word

with open('pl_ua.json') as file:
    data = json.load(file)

for i in data:
    d = data[str(i)]
    
    word = Word(word_pl=d['word'],
                word_ua=d['word_ua'],
                desc_pl=d['definition'],
                desc_ua=d['definition_ua'])
   
    db.session.add(word)
    db.session.commit()

