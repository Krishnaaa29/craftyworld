from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint
from craft import app, db, bcrypt
from craft.product.forms import  ProductsForm
from craft.models import Products
from flask_login import login_user, current_user, logout_user, login_required


product = Blueprint('product', __name__)

@product.route("/product_list", methods=['GET', 'POST'])
@login_required
def product_list():
    products = Products.query.all()
    return render_template('product_list.html', title='Product', products=products)