from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ubuntu:dlatldhs@localhost/test?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True #로그를 위한 플래그
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #수정사항 추적, 로그사용으로 불필요
app.config['SECRET_KEY'] = 'this is secret'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'login_user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}    #한글인식

    userid = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(100))
    created = db.Column(db.DateTime)

    def __init__(self, userid, name, password):
        self.userid = userid
        self.name = name
        self.password = password
        self.created = datetime.now()

    #객체 출력했을 때 나오는 출력화면
    def __repr__(self):
        return 'userid : %s, name : %s, password : %s' % (self.userid, self.name, self.password)

    def getUserID(self):
        return str(self.userid)

#db.create_all()

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/join", methods=['POST'])
def joinPost():
    userID = request.form['inputID']
    name = request.form['inputName']
    password = request.form['inputPW']
    retryPassword = request.form['inputREPW']
    
    if password != retryPassword:
        return "비밀번호가 맞지 않습니다."

    for userid in User.query.filter_by(userid=userID).all():
        if userID == userid.getUserID():
            return "이미 가입된 ID입니다."

    user = User(userID, name, password)
    db.create_all()
    db.session.add(user)
    try:
        db.session.commit()
        return "{}님 안녕하세요?".format(user.name)
    except:
        return "no commit"


if __name__=="__main__":
    app.run(host="0.0.0.0")
