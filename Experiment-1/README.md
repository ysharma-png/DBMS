# Experiment 1: ER Diagram Design — Indian E-Commerce Platform

## Overview
This experiment designs a comprehensive Entity-Relationship (ER) diagram for an Indian E-Commerce platform (similar to Flipkart / Amazon India). The system manages Customers, Addresses, Sellers, Categories, Products (with Specialization into Electronics and Clothing), Orders, Weak Entity OrderItems, Payments, and Deliveries.

---

## Files in this Directory
- `ER_Diagram.png`: High-resolution graphical representation of the ER Diagram.
- `README.md`: Detailed documentation of entities, attributes, key constraints, relationships, weak entities, specializations, and participation constraints.

---

## Entity Sets and Attributes

### 1. Customer (Strong Entity)
- **Primary Key**: `customer_id`
- **Composite Attribute**: `name` (decomposed into `first_name`, `last_name`)
- **Multi-valued Attribute**: `mobile_numbers` (a customer can have multiple phone numbers)
- **Simple Attributes**: `email` (UNIQUE), `created_at`

### 2. Address (Strong Entity)
- **Primary Key**: `address_id`
- **Foreign Key**: `customer_id` (references Customer)
- **Composite Attribute**: `address_details` (`house_no`, `street`, `city`, `state`, `pincode`)
- **Simple Attributes**: `address_type` (Home, Work)

### 3. Seller (Strong Entity)
- **Primary Key**: `seller_id`
- **Simple Attributes**: `company_name`, `gstin` (UNIQUE), `rating`
- **Multi-valued Attribute**: `contact_numbers`

### 4. Category (Strong Entity)
- **Primary Key**: `category_id`
- **Simple Attributes**: `category_name` (UNIQUE), `description`

### 5. Product (Base Entity / Superclass)
- **Primary Key**: `product_id`
- **Simple Attributes**: `product_name`, `price`, `stock_quantity`, `description`
- **Foreign Keys**: `seller_id` (references Seller), `category_id` (references Category)

### 6. Product Specialization (IS-A Subclasses)
- **Electronics** (Subclass of Product):
  - Inherits: `product_id`, `product_name`, `price`, `stock_quantity`
  - Specific Attributes: `warranty_period` (in months), `brand`, `model_number`
- **Clothing** (Subclass of Product):
  - Inherits: `product_id`, `product_name`, `price`, `stock_quantity`
  - Specific Attributes: `size` (S, M, L, XL), `material`, `color`, `gender`

### 7. Order (Strong Entity)
- **Primary Key**: `order_id`
- **Foreign Key**: `customer_id` (references Customer)
- **Simple Attributes**: `order_date`, `total_amount`, `order_status` (Pending, Processing, Shipped, Delivered, Cancelled)

### 8. OrderItem (Weak Entity)
- **Weak Entity**: Dependent on `Order` (Identifying Entity)
- **Partial Key (Discriminator)**: `item_number`
- **Composite Primary Key in Relational Model**: (`order_id`, `item_number`)
- **Simple Attributes**: `product_id`, `quantity`, `unit_price`, `discount`

### 9. Payment (Strong Entity)
- **Primary Key**: `payment_id`
- **Foreign Key**: `order_id` (references Order)
- **Simple Attributes**: `payment_mode` (UPI, Credit Card, Debit Card, Net Banking, COD), `payment_status` (SUCCESS, FAILED, PENDING), `transaction_date`, `amount`

### 10. Delivery (Strong Entity)
- **Primary Key**: `delivery_id`
- **Foreign Key**: `order_id` (references Order)
- **Simple Attributes**: `courier_partner` (BlueDart, Delhivery, Ekart), `tracking_number` (UNIQUE), `delivery_status` (In Transit, Delivered), `estimated_date`

---

## Relationships & Participation Constraints

1. **Customer PLACES Order**
   - **Cardinality**: `1 : N` (1 Customer can place N Orders)
   - **Participation**: Total participation for Order (every Order must be placed by a Customer); Partial participation for Customer (a new customer may have placed 0 orders).

2. **Customer HAS Address**
   - **Cardinality**: `1 : N` (1 Customer can have N Addresses)
   - **Participation**: Total participation for Customer (a customer must provide at least 1 address).

3. **Seller SUPPLIES Product**
   - **Cardinality**: `1 : N` (1 Seller supplies N Products)
   - **Participation**: Total participation for Product (every product must have a seller).

4. **Category CONTAINS Product**
   - **Cardinality**: `1 : N` (1 Category contains N Products)
   - **Participation**: Total participation for Product (every product belongs to a category).

5. **Order HAS_ITEM OrderItem (Identifying Relationship)**
   - **Cardinality**: `1 : N` (1 Order contains N OrderItems)
   - **Participation**: Total participation for OrderItem (an OrderItem cannot exist without an Order).

6. **Product INCLUDED_IN OrderItem**
   - **Cardinality**: `1 : N` (1 Product can appear in N OrderItems)

7. **Order PAID_VIA Payment**
   - **Cardinality**: `1 : 1` (1 Order has 1 Payment record)
   - **Participation**: Total participation for Payment (Payment exists only for a valid Order).

8. **Order FULFILLED_BY Delivery**
   - **Cardinality**: `1 : 1` (1 Order has 1 Delivery tracking record)
   - **Participation**: Total participation for Delivery.
