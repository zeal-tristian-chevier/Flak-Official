from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
 

class Product:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.img_url = data['img_url']
        self.stripe_id = data['stripe_id']
        self.is_avaliable = data['is_avaliable']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    #CREATE
    # @classmethod
    # def create_one(cls, data:dict) -> int:
    #     query = "INSERT INTO products (name, description, price, img_url, quantity) VALUES (%(name)s, %(description)s, %(price)s, %(img_url)s, %(quantity)s);"
    #     product_id = connectToMySQL(DATABASE).query_db(query, data)
    #     return product_id
    #READ
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM products WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return False
        products = []
        for product in results:
            products.append( cls(product) )
        return products

    #READ
    # @classmethod
    # def get_product_by_email(cls, data:dict) -> object:
    #     query = "SELECT * FROM products WHERE email = %(email)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
        
    #     if not results:
    #         return False
    #     return cls(results[0])
    
    #UPDATE RETURNS NOTHING
    # @classmethod
    # def update_one(cls, data:dict) -> None:
    #     query = "UPDATE products SET name='%(name)s' WHERE id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     return results

    # #DELETE RETURNS NOTHING
    # @classmethod
    # def delete_one(cls, data:dict) -> None:
    #     query = "DELETE FROM products WHERE id = %(id)s;"        
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     if not results:
    #         return False
    #     return results