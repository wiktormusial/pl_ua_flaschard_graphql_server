from ariadne import convert_kwargs_to_snake_case
from .models import Word


def resolve_words(obj, info):
    try:
        words = [word.to_dict() for word in Word.query.all()]
        payload = {
            "status": "succeeded", 
            "words": words
        }
    except Exception as error:
        payload = {
            "status": "error",
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_word(obj, info, word_id):
    try:
        word = Word.query.get(word_id)
        payload = {
            "status": "succeeded",
            "word": word.to_dict()
        }
    except AttributeError:
        payload = {
            "status": "error",
            "error": [f"Word with id={word_id} not found"]
        }
    return payload
