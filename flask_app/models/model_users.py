from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session

import re
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.products = []
    # Now we use class methods to query our database

    #CREATE
    @classmethod
    def create_one(cls, data:dict) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id
    #READ
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    #READ
    @classmethod
    def get_user_by_email(cls, data:dict) -> object:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        if not results:
            return False
        return cls(results[0])

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return False
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    #UPDATE RETURNS NOTHING
    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE users SET name='%(name)s' WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    #DELETE RETURNS NOTHING
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM users WHERE id = %(id)s;"        
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return results

    #VALIDATE REGISTRATION
    @staticmethod
    def validate_user(data):
        is_valid = True
        
        if(len(data['first_name']) < 2):
            is_valid = False
        if(len(data['last_name']) < 2):
            is_valid = False
        if(len(data['email']) < 3):
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'err_user')
            is_valid = False
        else:
            potential_user = User.get_user_by_email({'email': data['email']})
            if potential_user:
                flash("Email is already in use!", 'err_user')
                is_valid = False
        if(len(data['password']) < 8):
            is_valid = False
        if not is_valid:
            flash("Invalid email address!", 'err_user')
        return is_valid


#VALIDATE LOGIN
    @staticmethod
    def validate_login(data):
        is_valid = True
        print(data)
        if(len(data['email']) < 3):
            flash("Email must be at least 3 characters", 'err_user_email_login')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", 'err_user_email_login')
            is_valid = False
        else:
            potential_user = User.get_user_by_email({'email': data['email']})
            if not potential_user:
                flash("No Email found!", 'err_user_email_login')
                is_valid = False

        if(len(data['password']) < 8):
            flash("Password must be at least 8 characters", 'err_user_password_login')
            is_valid = False
        if is_valid:
            if not bcrypt.check_password_hash(potential_user.password, data['password']):
                flash("Invalid Credentials!", 'err_user_password_login')
                is_valid = False
            else:
                session['user_id'] = potential_user.id

        return is_valid