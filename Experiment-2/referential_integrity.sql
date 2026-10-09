INSERT INTO customer (first_name, last_name, email) VALUES ('Duplicate', 'User', 'aarav.sharma@example.com');

INSERT INTO orders (customer_id, total_amount, order_status) VALUES (9999, 1500.00, 'Pending');

INSERT INTO customer (first_name, last_name, email) VALUES (NULL, 'Kumar', 'null.test@example.com');

INSERT INTO order_item (order_id, item_number, product_id, quantity, unit_price) VALUES (1, 1, 1, 2, 49999.00);

DELETE FROM customer WHERE customer_id = 1;

SELECT customer_id, phone_number FROM customer_phone WHERE customer_id = 1;

SELECT order_id, customer_id, total_amount FROM orders WHERE order_id = 1;

DELETE FROM category WHERE category_id = 1;

SELECT product_id, product_name, category_id FROM product WHERE product_id IN (1, 2);

DELETE FROM orders WHERE order_id = 2;

SELECT * FROM order_item WHERE order_id = 2;

SELECT * FROM payment WHERE order_id = 2;

SELECT * FROM delivery WHERE order_id = 2;
