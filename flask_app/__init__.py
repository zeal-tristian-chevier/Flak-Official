from flask import Flask
from flask_bcrypt import Bcrypt    
from decouple import config

# from flask_socketio import SocketIO

app = Flask(__name__)

bcrypt = Bcrypt(app) 

DATABASE = "flak_db"
# DATABASE = "flak_db"