from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth= Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method== 'POST':
        email=request.form.get('email')
        password=request.form.get('password') 

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("logged in successfully!",category="success")
                login_user(user,remember=True)
                return redirect(url_for('views.rec'))
            else:
                flash("incorrect password",category="error")
        else:
            flash("email doesnot exist",category="error")
    return render_template("LOGIN.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        if user:
            flash("email already exist",category="error")
        if len(email)<4:
            flash('Email must be greater than 4 characters',category="error")
        elif len(password)<4:
            flash('password is too short it should be atleast 4 characters long',category="error")
        else:
            new_user=User(email=email,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Acount Created')
            login_user(user,remember=True)
            return redirect(url_for('views.rec'))
    return render_template("trysignin.html",user=current_user)