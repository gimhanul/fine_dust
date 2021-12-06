from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect
import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        return #raise ~~


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+get_secret("DB_USER")+':'+get_secret("DB_PW")+'@'+get_secret("DB_HOST")+'/'+get_secret("DB_NAME")+'?charset=utf8'
app.config['SQLALCHEMY_ECHO'] = True #로그를 위한 플래그
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #수정사항 추적, 로그사용으로 불필요
app.config['SECRET_KEY'] = 'this is secret'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'login_user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}    #한글인식

    email = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(20))
    created = db.Column(db.DateTime)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        self.created = datetime.now()

    #객체 출력했을 때 나오는 출력화면
    def __repr__(self):
        return 'email : %s, name : %s, password : %s' % (self.email, self.name, self.password)

    def getEmail(self):
        return str(self.email)

db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def userLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    return render_template('login.html')



@app.route("/join", methods=['POST', 'GET'])
def joinPost():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password1']
        retryPassword = request.form['password2']
    
        if password != retryPassword:
            return "비밀번호가 맞지 않습니다."

        for email in User.query.filter_by(email=email).all():
            if email == email.getEmail():
                return "이미 가입된 ID입니다."

        user = User(email, name, password)
        db.session.add(user)
        try:
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return "no commit"

    return render_template('join.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
