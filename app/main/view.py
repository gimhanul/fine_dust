from flask import Flask, redirect, render_template, request, url_for, Blueprint
from app import db
from .model import User
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    return render_template('login.html')



@main.route('/join', methods=['POST', 'GET'])
def joinPost():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password1']
        retryPassword = request.form['password2']
    
        if password != retryPassword:
            return '비밀번호가 맞지 않습니다.'

        for email in User.query.filter_by(email=email).all():
            if email == email.getEmail():
                return '이미 가입된 ID입니다.'

        user = User(email, name, password)
        db.session.add(user)
        try:
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'no commit'

    return render_template('join.html')