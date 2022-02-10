from flask import Blueprint, render_template, session, request,redirect,url_for
from utilities.db.db_cart import dbcart
from utilities.db.db_products_in_cart import dbproduct_in_cart as DBP
from utilities.db.db_products import dbProducts
from utilities.db.db_users import dbusers



# catalog blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment', methods=['GET', 'POST'])
def index():
    cart_id = dbcart.get_last_cart_id(session['user_data']['username'])
    print(session['user_data'])
    if 'logged_in' not in session:
        return render_template('SignIn.html')
    if session['logged_in'] == True:
        total_price = DBP.update_total(session['user_data']['username'], cart_id)
        if request.method == 'GET':
            if total_price == 0:
                return redirect(url_for('shop.index'))
            return render_template('payment.html',total_price=total_price)

        if request.method == 'POST':
            #check if we got all products in stock
            products_in_cart = DBP.get_cart_details(session['user_data']['username'], cart_id)
            missProductOnStock, product = dbProducts.isProductMiss(products_in_cart)
            if missProductOnStock:
                if 'message' not in session:
                    session['message'] = f'Patment falied! {product} is out of stock, please reduce quantity or order other product'
                return redirect(url_for('shop.index'))

            Delivery_Method = request.form['Delivery_Method']
            Address = request.form['address']
            if Delivery_Method == "new_Address" or Delivery_Method == "current_Address":
                status = dbcart.update_status(session['user_data']['username'], cart_id,"On the way")
            else:
                status = dbcart.update_status(session['user_data']['username'], cart_id, "Waiting for collection")
            if Delivery_Method == "new_Address":
                dbcart.update_address(session['user_data']['username'], cart_id,Address)
            elif Delivery_Method == "current_Address":
                details = dbusers.get_all_details(session['user_data']['username'])
                dbcart.update_address(session['user_data']['username'], cart_id, details[0].address)

            dbcart.update_total_cost(session['user_data']['username'], cart_id, total_price)
            #update stock
            dbProducts.update_stock(products_in_cart)

            next_cart = cart_id+1
            session['user_data']['cart_id']=next_cart
            dbcart.insert(session['user_data']['username'])

            return render_template('confirmationOrder.html', cart_id=cart_id)
