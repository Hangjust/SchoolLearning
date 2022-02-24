from distutils.log import error
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash





auth = Blueprint('auth', __name__)





@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):   #checks if user.password is the same as password you entered
                flash('logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again.', category='error')
        else:
            flash('Email doesnt exist.', category='error')




    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    

    

        user = User.query.filter_by(email=email).first()            #checks if user is already created
        if user:
            flash('Account already exists', category='error')


        elif len(email) < 3:
            flash('Email too short, fucken idiot', category='error')

        elif len(name) < 2:
            flash('let me see your passport, who tf has 1 letter name?', category='error')

        elif password1 != password2:
            flash('why u try to test me? passwords dont match', category='error')

        elif len(password1) <4:
            flash('password too short, u retard?', category='error')

        elif name == password1:
            flash('password cant be the same as ' + "'" + name + "'", category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            #user to database
            flash('good job', category='success')
            return redirect(url_for('views.home'))






    return render_template("sign_up.html")

@auth.route('/some')
def some():
    return render_template("some.html")