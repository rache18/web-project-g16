from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.db.db_users import dbusers

# catalog blueprint definition
UpdateDetails = Blueprint('UpdateDetails', __name__, static_folder='static', static_url_path='/UpdateDetails', template_folder='templates')


# Routes
@UpdateDetails.route('/UpdatePhone')
def UpdatePhone():
    return render_template('UpdateDetails.html',update = 'phone')

@UpdateDetails.route('/UpdateAddress')
def UpdateAddress():
    return render_template('UpdateDetails.html',update = 'address')

@UpdateDetails.route('/UpdatePassword')
def UpdatePassword():
    return render_template('UpdateDetails.html',update = 'password')

@UpdateDetails.route('/UpdateEmail')
def UpdateEmail():
    return render_template('UpdateDetails.html',update = 'email')


@UpdateDetails.route('/update_user', methods=['POST'])
def update_user():
        username = session['user_data']['username']
        if request.form['email'] != "":
            email = request.form['email']
            dbusers.update_user_email(username, email)
            session['user_data']["email"] = email

        if request.form['password'] != "":
            password = request.form['password']
            dbusers.update_user_password(username, password)
            session['user_data']["password"] = password

        if request.form['phone'] != "":
            phone = request.form['phone']
            dbusers.update_user_phone(username, phone)
            session['user_data']["phone"] = phone

        if request.form['address'] != "":
            address = request.form['address']
            dbusers.update_user_address(username, address)
            session['user_data']["address"] = address

        return redirect(url_for('profile.index'))
