from datetime import datetime
from main import db


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_pl = db.Column(db.String(15)) 
    word_ua = db.Column(db.String(15)) 
    desc_pl = db.Column(db.String)
    desc_ua = db.Column(db.String)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'word_pl': self.word_pl,
            'word_ua': self.word_ua,
            'desc_pl': self.desc_pl,
            'desc_ua': self.word_ua,
            'pub_date': self.pub_date,
        }
