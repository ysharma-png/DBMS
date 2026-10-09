INSERT INTO customer (first_name, last_name, email) VALUES
('Aarav', 'Sharma', 'aarav.sharma@example.com'),
('Priya', 'Verma', 'priya.verma@example.com'),
('Rohan', 'Mehta', 'rohan.mehta@example.com'),
('Ananya', 'Iyer', 'ananya.iyer@example.com'),
('Vikram', 'Singh', 'vikram.singh@example.com');

INSERT INTO customer_phone (customer_id, phone_number) VALUES
(1, '9876543210'),
(1, '9876543211'),
(2, '9812345678'),
(3, '9988776655'),
(4, '9765432109'),
(5, '9654321098');

INSERT INTO address (customer_id, house_no, street, city, state, pincode, address_type) VALUES
(1, 'A-12', 'MG Road', 'Bengaluru', 'Karnataka', '560001', 'Home'),
(1, 'Flat 402', 'ORR Tech Park', 'Bengaluru', 'Karnataka', '560103', 'Work'),
(2, 'B-304', 'Civil Lines', 'New Delhi', 'Delhi', '110054', 'Home'),
(3, '78-C', 'Park Street', 'Kolkata', 'West Bengal', '700016', 'Home'),
(4, '15/2', 'Anna Nagar', 'Chennai', 'Tamil Nadu', '600040', 'Home'),
(5, '501', 'Banjara Hills', 'Hyderabad', 'Telangana', '500034', 'Home');

INSERT INTO seller (company_name, gstin, rating) VALUES
('TechSurge Retail Ltd', '29ABCDE1234F1Z5', 4.8),
('FashionHub Traders', '07FGHIJ5678K1Z2', 4.5),
('ApplianceWorld Online', '19LMNOP9012Q1Z8', 4.2);

INSERT INTO seller_phone (seller_id, phone_number) VALUES
(1, '080-23456789'),
(1, '9870001122'),
(2, '011-45678901'),
(3, '033-67890123');

INSERT INTO category (category_name, description) VALUES
('Electronics', 'Smartphones, Laptops, Accessories and Gadgets'),
('Apparel', 'Men, Women and Kids Fashion Wear'),
('Home Appliances', 'Kitchen and Home Electrical Appliances');

INSERT INTO product (seller_id, category_id, product_name, price, stock_quantity, description) VALUES
(1, 1, 'Smartphone X1', 49999.00, 50, '5G Smartphone with 128GB Storage'),
(1, 1, 'Wireless Earbuds Pro', 4999.00, 200, 'Noise Cancelling Wireless Earbuds'),
(2, 2, 'Slim Fit Denim Jeans', 1999.00, 150, '100% Cotton Stretch Denim'),
(2, 2, 'Casual Polo T-Shirt', 899.00, 300, 'Breathable Cotton Polo Shirt'),
(3, 3, 'Smart Microwave Oven', 12499.00, 40, '28L Convection Microwave Oven');

INSERT INTO electronics (product_id, warranty_period, brand, model_number) VALUES
(1, 12, 'TechBrand', 'X1-5G-2026'),
(2, 6, 'AudioTech', 'AT-EBP-02');

INSERT INTO clothing (product_id, size, material, color, gender) VALUES
(3, '32', 'Denim Cotton', 'Dark Blue', 'Men'),
(4, 'L', 'Pima Cotton', 'Navy Blue', 'Men');

INSERT INTO orders (customer_id, order_date, total_amount, order_status) VALUES
(1, '2026-09-01 10:30:00', 54998.00, 'Delivered'),
(2, '2026-09-02 14:15:00', 1999.00, 'Shipped'),
(3, '2026-09-03 16:45:00', 12499.00, 'Processing'),
(4, '2026-09-04 11:20:00', 899.00, 'Pending');

INSERT INTO order_item (order_id, item_number, product_id, quantity, unit_price, discount) VALUES
(1, 1, 1, 1, 49999.00, 0.00),
(1, 2, 2, 1, 4999.00, 0.00),
(2, 1, 3, 1, 1999.00, 0.00),
(3, 1, 5, 1, 12499.00, 0.00),
(4, 1, 4, 1, 899.00, 0.00);

INSERT INTO payment (order_id, payment_mode, payment_status, transaction_date, amount) VALUES
(1, 'UPI', 'SUCCESS', '2026-09-01 10:32:00', 54998.00),
(2, 'Credit Card', 'SUCCESS', '2026-09-02 14:17:00', 1999.00),
(3, 'Net Banking', 'SUCCESS', '2026-09-03 16:47:00', 12499.00),
(4, 'COD', 'PENDING', '2026-09-04 11:20:00', 899.00);

INSERT INTO delivery (order_id, courier_partner, tracking_number, delivery_status, estimated_date) VALUES
(1, 'BlueDart', 'BD100987654', 'Delivered', '2026-09-03'),
(2, 'Delhivery', 'DEL88776655', 'In Transit', '2026-09-06'),
(3, 'Ekart', 'EK990011223', 'Processing', '2026-09-08');
