from flask import Flask
from flask_bcrypt import Bcrypt    
from decouple import config

# from flask_socketio import SocketIO

app = Flask(__name__)

bcrypt = Bcrypt(app) 

DATABASE = "bz1q1gbtsqegcc4di2gn"
# DATABASE = "flak_db"