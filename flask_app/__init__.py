from flask import Flask
from flask_bcrypt import Bcrypt    
from decouple import config

# from flask_socketio import SocketIO

app = Flask(__name__)

bcrypt = Bcrypt(app) 

DATABASE = config('SQL_DB')
# DATABASE = "flak_db"