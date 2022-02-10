from flask import Blueprint, render_template, session, request,url_for,redirect
from utilities.db.db_products import dbProducts
from utilities.db.db_products_in_cart import dbproduct_in_cart as DBP
from utilities.db.db_cart import dbcart

# import pyautogui



# shop blueprint definition
shop = Blueprint('shop', __name__, static_folder='static', static_url_path='/shop', template_folder='templates')


# Routes
@shop.route('/shop')
def index():
    if request.args.get('sale') is not None:
        products = dbProducts.get_products(sale=True)
    elif request.args.get('price') is not None:
        products = dbProducts.get_products(price=request.args.get('price'))
    elif request.args.get('color') is not None:
        products = dbProducts.get_products(color=request.args.get('color'))
    else:
        products = dbProducts.get_products()

    if 'message' in session:
        message = session['message']
        session.pop('message')
        return render_template('shop.html', products=products, message=message)
    return render_template('shop.html', products=products)

# add to cart
@shop.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # position = pyautogui.position()
    if 'logged_in' not in session or session['logged_in'] == False:
        return render_template('SignIn.html')
    else:
        productid = request.form['productId']
        productPrice = request.form['productPrice']
        productSale = request.form['productSale']
        cart_id = dbcart.get_last_cart_id(session['user_data']['username'])
        if DBP.get_product_from_product_cart(productid, session['user_data']['username'], cart_id):
            products = dbProducts.get_products()
            return render_template('shop.html', products=products)
        else:
                DBP.insert_product_to_product_cart(productid, cart_id, session['user_data']['username'])
        return redirect(url_for('shop.index'))
