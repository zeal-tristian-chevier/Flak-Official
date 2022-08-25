from flask import Flask, render_template, redirect, session
from flask_app import app

from flask_app.models.model_users import User
from flask_app.models.model_products import Product

#HOME PAGE
@app.route('/')
def index():
    if 'user_id' in session:
        user = User.get_one({'id': session['user_id']})
        return render_template('home_page.html', user = user)
    return render_template('home_page.html')

#CONTACT PAGE
@app.route('/contact')
def contact():
    return render_template('contact.html')

#SHOP DASHBOARD
@app.route('/shop')
def shop():
    products = Product.get_all()
    return render_template('shop.html', products = products)

#ITEM PREVIEW
@app.route('/shop/<int:id>/view')
def view_process(id):
    product = Product.get_one({'id': id})
    session['product_id'] = id
    return render_template('item_page.html', product = product)

#LOGOUT DELETE SESSION
@app.route('/logout')
def user_logout():
    session.clear()
    return redirect('/login')
