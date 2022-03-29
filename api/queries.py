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
