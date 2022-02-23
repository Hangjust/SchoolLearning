from flask import Blueprint, render_template, request, flash



auth = Blueprint('auth', __name__)





@auth.route('/login', methods=['GET', 'POST'])
def login():
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


        if len(email) < 3:
            flash('Email too short, fucken idiot', category='error')

        elif len(name) < 2:
            flash('let me see your passport, who tf has 1 letter name?', category='error')

        elif password1 != password2:
            flash('why u try to test me? passwords dont match', category='error')

        elif len(password1) <4:
            flash('password too short, u retard?', category='error')

        elif name == password1:
            flash('cant be the same as' + name, category='error')
        else:
            #user to database
            flash('good job', category='success')

    return render_template("sign_up.html")

@auth.route('/some')
def some():
    return render_template("some.html")