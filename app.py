import datetime
from flask import Flask, render_template, request, redirect, url_for, make_response, session
from db import Db, User, Reply, Question
from model import Model
import uuid
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='statics',
            template_folder='templates')
app.secret_key = b'_$DIO@05{DK!@(&)}'

@app.route('/')
def home():
    if 'username' in session:
        print(f'Logged in as {session["username"]}')

    data=Db()
    questions=data.get_questions()
    model=Model(questions)
    return render_template('index.html', model=model)


@app.route('/users/<username>')
def questions_by_user(username):
    if 'username' in session:
        print(f'Logged in as {session["username"]}')

    data=Db()
    questions=data.get_questions_by_user(username)
    model=Model(questions)
    return render_template('index.html', model=model)

@app.route('/login')
def login():
    args = request.args
    redirect_url = args.get('redirect_url')
    if redirect_url is None:
        redirect_url=''
    return render_template('login.html', model=Model(None), redirect_url=redirect_url)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login_post():
    username=request.form['username']
    password=request.form['password']
    redirect_url=request.form['redirect_url']
    data=Db()
    user=data.login_user(username, password)
    if user is None:
        print("wrong acct")
        redirect('/login')
        # user found, set a cookie on the user's computer to track the login status
    session['user_id'] = user.id
    session['username'] = user.username
    print(f"redirect_url: {redirect_url}")
    if redirect_url != '':
        return redirect(redirect_url)
    return redirect('/')

@app.route('/questions/<id>')
def question(id):
    data=Db()
    question=data.get_question_by_id(id)
    replies=data.get_replies(id)
    return render_template('question.html', model=Model(None), question=question, replies=replies)

@app.route('/signup')
def signup():
    return render_template('signup.html', model=Model(None))


@app.route('/signup', methods=['POST'])
def signup_post():
    username=request.form['username']
    password=request.form['password']
    user=User(0, username, password, int(datetime.datetime.now().timestamp()))

    # TODO: before adding user, check if username already taken by someone else, return error if so.
    data=Db()
    data.add_user(user)

    # sign user in directly
    session['username'] = user.username
    return redirect('/')


@app.route('/questions/<id>/replies', methods=['POST'])
def reply_post(id):
    replytext=request.form['reply']
    reply=Reply(0, id, session['user_id'], replytext, replytext, int(datetime.datetime.now().timestamp()))
    data=Db()
    data.add_reply(reply)
    return redirect(f'/questions/{id}')


@app.route('/new-question')
def new_question():
    if 'username' not in session:
        return redirect('/login?redirect_url=new-question')

    return render_template('new-question.html', model=Model(None))


@app.route('/questions', methods=['POST'])
def new_question_post():
    img=request.files['img']
    if img:
        filename = str(uuid.uuid4()) + '.' + img.filename.rsplit('.', 1)[1].lower()
        img_path = os.path.join('images', filename)
        img.save('statics/' + img_path)
    else: 
        img_path = ''
    content_md=request.form['content_md']
    q=Question(0, session['user_id'], content_md, content_md, 0, 0, int(datetime.datetime.now().timestamp()), img_path)
    data=Db()
    newid=data.add_question(q)
    return redirect(f'/questions/{newid}')