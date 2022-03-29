from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'PL_UA_FLASHCARDS'
