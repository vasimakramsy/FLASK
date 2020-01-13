from flask import render_template,url_for,flash, redirect
from flaskblog import app,db,bcrypt
from flaskblog.form import RegistrationForm,LoginForm
from flaskblog.model import User,Post
from flask_login import login_user, current_user, logout_user

posts=[
    {
        'author':'vasim',
        'title':'blog',
        'content':'1st post',
        'date_posted':'jan 2020'
    },
    {
        'author':'asif',
        'title':'blog',
        'content':'2st post',
        'date_posted':'jan 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')


@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password =bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'your account has been created! you are now able to login ','sucess')
        return redirect(url_for('login'))
    return render_template('register.html',title='register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsucessful please check email and password')
    return render_template('login.html',title='login',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')

@app.route('/account')
def account():
  return render_template('account.html',title='account')