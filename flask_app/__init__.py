from flask import Flask
from flask_bcrypt import Bcrypt    

# from flask_socketio import SocketIO

app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = "pk_test_51LZfwfBpdBqI2NGfTcsVuhYX7cGryM01JYho5soGOJZUc631Toshd5bjjxFNmhqRV70E9rDw1XDdOd0VmpYyajNX003T3MoQAW"
app.config['STRIPE_SECRETY_KEY'] = "sk_test_51LZfwfBpdBqI2NGfeg0WCAbt76TgguncRH6nL6KtvErDSgmoSEkjTcOeRJFUZdAaPBaTReS4XoGIRUlC4qZyHntV00vJ7CMz5a"

bcrypt = Bcrypt(app) 


DATABASE = "flak_db"