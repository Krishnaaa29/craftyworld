from flask import render_template, url_for, request, redirect, session, flash, redirect
from craft import app, db, bcrypt
from craft.forms import RegistrationForm, LoginForm, UpdateAccountForm, ProductsForm
from craft.models import Users,Products
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/product_list", methods=['GET', 'POST'])
@login_required
def product_list():
    form = ProductsForm()
    products = Products.query.all()
    return render_template('product_list.html', title='Product', products=products)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful, Please check emailid and password','danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/youraccount", methods=['GET', 'POST'])
@login_required
def youraccount():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your Account has been Updated!', 'success')
        return redirect(url_for('youraccount'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('youraccount.html', titl='Update', form=form)


@app.route("/adminindex")
def adminindex():
    return render_template('adminindex.html')

@app.route("/adminlogin")
def adminlogin():
    return render_template('adminlogin.html')



   
    
@app.route("/order")
@login_required
def order():
    return render_template('order.html')




