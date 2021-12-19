from ... import db
from datetime import datetime

class FineDust(db.Model):
    __tablename__ = 'fine_dust'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}    #한글인식

    datetime = db.Column(db.DateTime, primary_key=True)
    munge = db.Column(db.Integer)

    def __init__(self, munge):
        self.munge = munge
        self.created = datetime.now()

    #객체 출력했을 때 나오는 출력화면
    def __repr__(self):
        return 'munge: %d' % (self.munge)
