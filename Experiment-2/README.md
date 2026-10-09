# Experiment 2: Relational Schema & MySQL Implementation

## Overview
This experiment converts the Indian E-Commerce ER Diagram from Experiment 1 into a complete MySQL relational schema. It enforces primary keys, foreign keys, `NOT NULL`, `UNIQUE` constraints, and specifies cascading referential integrity actions (`ON DELETE CASCADE` and `ON DELETE SET NULL`).

---

## Files in this Directory
- `schema.sql`: Contains `CREATE TABLE` DDL statements for all 13 relational tables.
- `sample_data.sql`: Contains realistic sample `INSERT INTO` statements.
- `referential_integrity.sql`: Contains executable SQL statements demonstrating constraint violations and cascading deletions.
- `README.md`: Complete documentation and analysis of the relational schema and test cases.

---

## Relational Schema & Tables

1. **`customer`**: Stores customer demographic information. (`customer_id` PK, `email` UNIQUE NOT NULL).
2. **`customer_phone`**: Multi-valued phone numbers for customers (`customer_id`, `phone_number` PK, FK to `customer` `ON DELETE CASCADE`).
3. **`address`**: Customer delivery addresses (`address_id` PK, FK to `customer` `ON DELETE CASCADE`).
4. **`seller`**: Registered sellers (`seller_id` PK, `gstin` UNIQUE NOT NULL).
5. **`seller_phone`**: Multi-valued contact numbers for sellers (`seller_id`, `phone_number` PK, FK to `seller` `ON DELETE CASCADE`).
6. **`category`**: Product categories (`category_id` PK, `category_name` UNIQUE NOT NULL).
7. **`product`**: Base product catalog (`product_id` PK, FK to `seller` `ON DELETE SET NULL`, FK to `category` `ON DELETE SET NULL`).
8. **`electronics`**: Sub-table for electronics specialization (`product_id` PK & FK to `product` `ON DELETE CASCADE`).
9. **`clothing`**: Sub-table for clothing specialization (`product_id` PK & FK to `product` `ON DELETE CASCADE`).
10. **`orders`**: Customer order headers (`order_id` PK, FK to `customer` `ON DELETE SET NULL`).
11. **`order_item`**: Weak entity order line items (`order_id`, `item_number` Composite PK, FK to `orders` `ON DELETE CASCADE`, FK to `product` `ON DELETE SET NULL`).
12. **`payment`**: Order payment details (`payment_id` PK, `order_id` UNIQUE FK to `orders` `ON DELETE CASCADE`).
13. **`delivery`**: Order shipment tracking details (`delivery_id` PK, `order_id` UNIQUE FK to `orders` `ON DELETE CASCADE`, `tracking_number` UNIQUE).

---

## Referential Integrity & Constraint Violations Analysis

### 1. Duplicate UNIQUE Email Violation
- **Statement**: `INSERT INTO customer (first_name, last_name, email) VALUES ('Duplicate', 'User', 'aarav.sharma@example.com');`
- **Result**: Fails with `ERROR 1062 (23000): Duplicate entry 'aarav.sharma@example.com' for key 'customer.email'`.
- **Reason**: The `email` column in the `customer` table has a `UNIQUE` constraint.

### 2. Foreign Key Violation (Non-existent Parent)
- **Statement**: `INSERT INTO orders (customer_id, total_amount, order_status) VALUES (9999, 1500.00, 'Pending');`
- **Result**: Fails with `ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails`.
- **Reason**: `customer_id = 9999` does not exist in the `customer` table.

### 3. NOT NULL Constraint Violation
- **Statement**: `INSERT INTO customer (first_name, last_name, email) VALUES (NULL, 'Kumar', 'null.test@example.com');`
- **Result**: Fails with `ERROR 1048 (23000): Column 'first_name' cannot be null`.
- **Reason**: `first_name` is defined with `NOT NULL`.

### 4. Primary Key Violation (Composite Key)
- **Statement**: `INSERT INTO order_item (order_id, item_number, product_id, quantity, unit_price) VALUES (1, 1, 1, 2, 49999.00);`
- **Result**: Fails with `ERROR 1062 (23000): Duplicate entry '1-1' for key 'order_item.PRIMARY'`.
- **Reason**: `(order_id = 1, item_number = 1)` already exists in `order_item`.

### 5. ON DELETE CASCADE and ON DELETE SET NULL Behavior
- **Customer Deletion**: `DELETE FROM customer WHERE customer_id = 1;`
  - Dependent records in `customer_phone` and `address` are automatically deleted (`ON DELETE CASCADE`).
  - In `orders`, `customer_id` is updated to `NULL` (`ON DELETE SET NULL`), retaining historical order sales data while unlinking the customer.
- **Category Deletion**: `DELETE FROM category WHERE category_id = 1;`
  - In `product`, `category_id` becomes `NULL` (`ON DELETE SET NULL`).
- **Order Deletion**: `DELETE FROM orders WHERE order_id = 2;`
  - Dependent line items in `order_item`, payment record in `payment`, and shipment record in `delivery` are automatically deleted (`ON DELETE CASCADE`).
