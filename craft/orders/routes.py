from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint
from craft import app, db, bcrypt
from craft.orders.forms import OrderForm
from craft.models import CustomerOrder,Products
from flask_login import login_user, current_user, logout_user, login_required

orders = Blueprint('orders', __name__)

@orders.route("/order/<int:pid>", methods=['GET', 'POST'])
@login_required
def order(pid):
    id = pid 
    form = OrderForm()
    products = Products.query.filter_by(id=id).first()
    if form.validate_on_submit():
     
        # insertion operation
        order =  Order(products_id=id,users_id=current_user.id,name=form.name.data, address=form.address.data, pincode=form.pincode.data, city=form.city.data, state=form.state.data, mobile=form.mobile.data, status=form.status.data)
        # if req is post,then insert title and content into db,for dat we assign those in new content
        products.stock = products.stock-1
        try:
            db.session.add(order) 
            db.session.commit() 
            flash(f'Your Order has been submitted', 'success')                       
            return redirect(url_for('orders.view')) #after successful insertion redirect back to home page
        except:
            flash(f'There is an issue', 'danger')
            return redirect(url_for('product.product_list'))
    else:
        #task = Order.query.all()
        products = Products.query.filter_by(id=pid).first()
        return render_template('order.html', products=products, form=form)

@orders.route("/view")
def view():
    return render_template('view.html')


@orders.route("/orderview")
def orderview():
    orders = CustomerOrder.query.filter_by(customer_id=current_user.id).all()
    subtotal = 0
    grandtotal = 0
    #orders = db.session.query(Order, Products).outerjoin(Products, Order.products_id == Products.id).add_columns(Order.id, Order.address , Order.pincode, Order.city, Order.state, Order.mobile, Order.status, Products.name, Products.price, Products.image_file).filter(Order.users_id == current_user.id).all()
    #orders = Order.query.join(Products, Order.id==Products.id).add_columns(Order.id, Order.address, Order.pincode, Order.city, Order.state,  Order.mobile, Products.name, Products.price, Products.image_file).filter(Order.products_id == Products.id).filter(Order.users_id == current_user.id).all()
    return render_template('orderview.html', orders=orders, subtotal=subtotal, grandtotal=grandtotal)
"""
@orders.route("/order/<int:order_id>/delete", methods=['POST'])
@login_required
def orderdelete(order_id):
    
    orders = Order.query.get_or_404(order_id)
    if orders.users_id != current_user.id:
        abort(403)
    products = Products.query.filter_by(id=orders.products_id).first()
    products.stock = products.stock+1
    db.session.delete(orders)
    db.session.commit()
    
    flash('Your Order has been deleted!', 'success')
    return redirect(url_for('main.home'))
    flash('Your Order has been deleted!', 'success')
"""

@orders.route('/deleteorder/<int:order_id>', methods=['POST'])
@login_required
def deleteorder(order_id):
    orders = CustomerOrder.query.filter_by(id=order_id).first()
    db.session.delete(orders)
    db.session.commit()
    flash('Your Order has been deleted!', 'success')
    return redirect(url_for('orders.orderview'))
