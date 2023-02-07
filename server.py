from flask_app import app

from flask_app.controllers import controller_routes, controller_users, controller_products

from decouple import config

app.secret_key = config('SECRET_KEY')

if __name__=="__main__":       
    app.run(debug=True)
