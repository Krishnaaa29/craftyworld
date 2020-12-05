from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint
from craft import app, db, bcrypt
from craft.user.forms import RegistrationForm, LoginForm, UpdateAccountForm
from craft.models import Users
from flask_login import login_user, current_user, logout_user, login_required





user = Blueprint('user', __name__)




@user.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created! You are now able to log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('register.html', title='Register', form=form)

@user.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash(f'Login Unsuccessful, Please check emailid and password','danger')
    return render_template('login.html', title='Login', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@user.route("/youraccount", methods=['GET', 'POST'])
@login_required
def youraccount():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your Account has been Updated!', 'success')
        return redirect(url_for('user.youraccount'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('youraccount.html', titl='Update', form=form)


