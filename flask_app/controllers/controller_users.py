from flask import render_template, request, redirect, session
from flask_app import app, bcrypt

from flask_app.models.model_users import User
from flask_app.models.model_carts import Cart

#LOGIN & REGISTER PAGE
@app.route('/login')
def login():  

    session['is_false'] = True
    is_false = session['is_false']
    
    return render_template('login_registration.html', is_false = is_false)

#REGISTER PROCESS
@app.route('/register/process', methods=['POST'])
def user_register():
    #Validate function here
    if not User.validate_user(request.form):
        session['is_false'] = False
        return redirect('/login')
    hash_password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hash_password
    }
    id = User.create_one(data)
    session['user_id'] = id
    cart_id = Cart.create_cart({'user_id' : session['user_id']})
    session['cart_id'] = cart_id
    return redirect("/")

#LOGIN PROCESS
@app.route('/login/process', methods=['POST'])
def user_login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    #Validate function here
    if not User.validate_login(data):
        session['is_false'] = True
        return redirect('/login')
    user = User.get_user_by_email(data)
    session['user_id'] = user.id
    cart_id = Cart.get_cart({'user_id' : session['user_id']})
    session['cart_id'] = cart_id.id
    return redirect('/')   