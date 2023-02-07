from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session

from flask_app.models.model_products import Product

class Cart:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.products = []
    # Now we use class methods to query our database

    #CREATE
    @classmethod
    def create_cart(cls, data:dict) -> int:
        query = "INSERT INTO carts (user_id) VALUES (%(user_id)s);"
        cart_id = connectToMySQL(DATABASE).query_db(query, data)
        return cart_id
    #READ
    @classmethod
    def get_cart(cls, data:dict) -> object:
        query = "SELECT * FROM carts WHERE user_id = %(user_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])


    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM carts;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return False
        carts = []
        for cart in results:
            carts.append( cls(cart) )
        return carts

    @classmethod
    def get_products_from_cart(cls, data, cart):
        query = "SELECT * FROM products LEFT JOIN carts_has_products ON products.id = carts_has_products.product_id JOIN carts ON carts_has_products.cart_id = carts.id WHERE carts.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        if not results:
            return False
        product = cls(results[0])
        for product in results:
            product_data = {
                **product,
                'size' : product['size'],
                'quantity' : product['quantity']
            }
            product_actual = Product(( product_data ))
            product_actual.size = product_data['size']
            product_actual.quantity = product_data['quantity']
            cart.products.append(product_actual)

        return results
    
    #EMPTY CART
    @classmethod
    def empty_cart(cls, data:dict) -> None:
        query = "DELETE FROM carts_has_products WHERE cart_id = %(cart_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    #EMPTY PRODUCT 
    @classmethod
    def delete_product_from_cart(cls, data:dict) -> None:
        query = "DELETE FROM carts_has_products WHERE cart_id = %(cart_id)s AND product_id = %(product_id)s AND size = %(size)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    #UPDATE RETURNS NOTHING
    @classmethod
    def update_cart(cls, data:dict) -> None:
        query = "UPDATE carts_has_products SET quantity=%(quantity)s, size=%(size)s WHERE carts_has_products.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    #UPDATE RETURNS NOTHING
    @classmethod
    def relate_product_to_cart(cls, data:dict) -> None:
        query = "INSERT INTO carts_has_products (cart_id, product_id, size, quantity) VALUES (%(cart_id)s, %(product_id)s, %(size)s, %(quantity)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_relation(cls, data:dict) -> None:
        query = "SELECT * FROM carts_has_products WHERE cart_id = %(cart_id)s AND product_id = %(product_id)s AND size=%(size)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]['id']

    #CHECK IF ITEM ALREADY EXIST IN CART
    @staticmethod
    def validate_relation(data:dict) -> None:
        query = "SELECT * FROM carts_has_products WHERE cart_id = %(cart_id)s AND product_id = %(product_id)s AND size=%(size)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        is_valid = True
        if results:
            flash('Product with that size is already in your cart!', 'err_product')
            is_valid = False
        return is_valid

