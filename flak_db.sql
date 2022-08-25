SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM carts;
SELECT * FROM carts_has_products;

DELETE FROM carts WHERE id < 20;
##CREATE CART WITH ID = User id, PRODUCT ID = 
INSERT INTO carts (user_id) values (1);


INSERT INTO products (name, description, price, img_url, is_avaliable, stripe_id) VALUES ("Flak Tee", "Our most popular t-shirt. Wear it to our shows!", 25, "../static/imgs/flak_tshirt.png", 1, 'price_1LaPS5BpdBqI2NGfP06VLLnl');

INSERT INTO products (name, description, price, img_url, is_avaliable) VALUES ("Flak Hoodie", "Coming soon..", 50, "../static/imgs/flak_hoodie.png", 1, 'price_1LaPNmBpdBqI2NGfL6rGYNJN');

INSERT INTO products (name, description, price, img_url, is_avaliable) VALUES ("Flak Stickers", "Coming soon..", 50, "../static/imgs/flak_stickers.png", 0);

UPDATE products SET price=20 WHERE id = 1;

DELETE FROM carts WHERE id = 6;

##SELECT ALL USERS WITH A SPECIFIC ID WITH THEIR CART INFO
SELECT * FROM users LEFT JOIN carts ON users.id = user_id WHERE users.id = 2;

##SELECT ALL PRODUCTS WITH ID = 1 WITH WHAT CARTS THEY ARE IN
SELECT * FROM products LEFT JOIN carts ON products.id = product_id WHERE products.id = 1;


SELECT * FROM carts LEFT JOIN products ON carts.id = cart_id WHERE carts.id = 4;

SELECT * FROM products LEFT JOIN carts ON products.id = product_id WHERE products.id = 1;

SELECT * FROM products LEFT JOIN carts_has_products ON products.id = carts_has_products.product_id JOIN carts ON carts_has_products.cart_id = carts.id WHERE carts.id = 2;

SELECT * FROM products LEFT JOIN carts_has_products ON products.id = carts_has_products.product_id JOIN carts ON carts_has_products.cart_id = carts.id WHERE carts.id = 4;