from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint
from craft import app, db
from craft.models import Products, CustomerOrder
from flask_login import login_required, current_user
import secrets


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2,list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False
@app.route('/addcart', methods=['POST'])
def AddCart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        products = Products.query.filter_by(id=product_id).first()
        if product_id and quantity and request.method == "POST":
            DictItems = {product_id:{'name':products.name, 'price':products.price, 'quantity':quantity, 'image_file':products.image_file, 'stock':products.stock, 'product_id':product_id}}
            if 'ShoppingCart' in session:
                print(session['ShoppingCart'])
                if product_id in session['ShoppingCart']:
                    flash('This product is already there in your cart', 'danger')
                else:
                    session['ShoppingCart'] = MagerDicts(session['ShoppingCart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['ShoppingCart'] = DictItems
                return redirect(request.referrer)
    except Exception as e:

        print(e)
    finally:
        return redirect(request.referrer)
    

@app.route('/carts')
def getCart():
    if 'ShoppingCart' not in session or len(session['ShoppingCart']) <=0:
        return redirect(url_for('product.product_list'))
    subtotal = 0
    grandtotal = 0
    for key, products in session['ShoppingCart'].items():
        subtotal += float(products['price']) * int(products['quantity'])
        tax = ("%.2f" % (.06 *  float(subtotal)))
        grandtotal = float("%.2f" % (1.06 * subtotal))
    return render_template('carts.html', tax= tax, grandtotal= grandtotal)


@app.route('/updatecart/<int:code>', methods=['POST'])
def updatecart(code):
    if 'ShoppingCart' not in session or len(session['ShoppingCart']) <= 0:
        return redirect(url_for('product.product_list'))
    if request.method =="POST":
        quantity = request.form.get('quantity')
        try:
            session.modified = True
            for key, item in session['ShoppingCart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    flash('item is updated!','success')
                    return redirect(url_for('getCart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))   

@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    if 'ShoppingCart' not in session or len(session['ShoppingCart']) <= 0:
        return redirect(url_for('product.product_list'))
    try: 
        session.modified = True
        for key, item in session['ShoppingCart'].items():
            if int(key) == id:
                session['ShoppingCart'].pop(key, None)   
        return redirect(url_for('getCart')) 
    except Exception as e:
        print(e)
        return redirect(url_for('getCart')) 

# cart order
@app.route('/getorder', methods=['POST'])
@login_required
def get_order():
    customer_id = current_user.id
    invoice = secrets.token_hex(5)
    name = request.form['name'] 
    address = request.form['address'] 
    pincode = request.form['pincode'] 
    city = request.form['city']
    state = request.form['state']
    mobile = request.form['mobile']
    try:
        order = CustomerOrder(invoice=invoice, customer_id=customer_id, orders=session['ShoppingCart'], name=name, address=address, pincode=pincode, city=city, state=state, mobile=mobile)
        db.session.add(order)
        db.session.commit()
        session.pop('ShoppingCart')
        flash('Your order has been submit successfully','success')
        return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        flash('Some thing went wrong while get order','danger')
        return redirect(url_for('getCart')) 

