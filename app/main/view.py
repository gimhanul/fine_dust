import os
import fcntl
from flask import Flask, redirect, render_template, request, url_for, Blueprint, session
from app import db
from .domain.user import User
from .domain.fineDust import FineDust
from apscheduler.schedulers.background import BackgroundScheduler

main = Blueprint('main', __name__, url_prefix='/')

#미세먼지 값 받기
I2C_SLAVE = 0x703
PM2008 = 0x28

fd = os.open('/dev/i2c-1',os.O_RDWR)
if fd < 0 :
    print("Failed to open the i2c bus\n")
io = fcntl.ioctl(fd,I2C_SLAVE,PM2008)
if io < 0 :
    print("Failed to acquire bus access/or talk to salve\n")

def getFineDust():
    data = os.read(fd,32)
    now = FineDust(256*int(data[11])+int(data[12]))
    db.session.add(now)
    db.session.commit()

sched = BackgroundScheduler(daemon=True)
sched.add_job(getFineDust,trigger='interval',minutes=1)
sched.start()


#user 관리
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/join', methods=['POST', 'GET'])
def joinPost():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password1']
        retryPassword = request.form['password2']
   
        if password != retryPassword:
            return '비밀번호가 맞지 않습니다.'

        #bssm.hs.kr
        if email[-10:] != 'bssm.hs.kr':
            return '부산쏘마고 이메일을 사용해 주세요.'

        user = User(email, name, password)
        db.session.add(user)
        try:
            db.session.commit()
            return redirect(url_for('main.login'))
        except:
            return 'no commit'

    return render_template('join.html')


@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            return '존재하지 않는 사용자입니다.'

        if user.password == password:
            session['email'] = email
            return redirect(url_for('main.measure'))

    return render_template('login.html')

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))


#measure fineDust
@main.route('/measure')
def measure():
    latest = FineDust.query.all()
    return render_template('measure.html', munge=latest[-1])


@main.route('/chart')
def chart():
    data = FineDust.query.all()
    data = data[-6:]
    #TODO data 날짜별로 수정
    return render_template('chart.html', data=data)
