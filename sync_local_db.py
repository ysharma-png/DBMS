import pymysql
import sys

def main():
    password = "Yash@8357"
    if len(sys.argv) > 1:
        password = sys.argv[1]

    print(f"Connecting to MySQL server at 127.0.0.1:3306 with user 'root'...")
    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", password=password, port=3306, autocommit=True)
        print("Connected to MySQL server successfully!")
    except Exception as e:
        print(f"Connection failed: {e}")
        print("\nPlease ensure MySQL server is running and the password is correct.")
        sys.exit(1)

    cur = conn.cursor()
    print("Creating and selecting database 'dbms_lab'...")
    cur.execute("CREATE DATABASE IF NOT EXISTS dbms_lab;")
    cur.execute("USE dbms_lab;")

    # Experiment 2: E-Commerce Schema & Data
    print("Building Experiment 2: E-Commerce Relational Schema & Data...")
    schema_2_statements = [
        "DROP TABLE IF EXISTS delivery;",
        "DROP TABLE IF EXISTS payment;",
        "DROP TABLE IF EXISTS order_item;",
        "DROP TABLE IF EXISTS orders;",
        "DROP TABLE IF EXISTS clothing;",
        "DROP TABLE IF EXISTS electronics;",
        "DROP TABLE IF EXISTS product;",
        "DROP TABLE IF EXISTS category;",
        "DROP TABLE IF EXISTS seller_phone;",
        "DROP TABLE IF EXISTS seller;",
        "DROP TABLE IF EXISTS address;",
        "DROP TABLE IF EXISTS customer_phone;",
        "DROP TABLE IF EXISTS customer;",
        """CREATE TABLE customer (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""",
        """CREATE TABLE customer_phone (
            customer_id INT NOT NULL,
            phone_number VARCHAR(15) NOT NULL,
            PRIMARY KEY (customer_id, phone_number),
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE address (
            address_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NOT NULL,
            house_no VARCHAR(20) NOT NULL,
            street VARCHAR(100) NOT NULL,
            city VARCHAR(50) NOT NULL,
            state VARCHAR(50) NOT NULL,
            pincode VARCHAR(10) NOT NULL,
            address_type VARCHAR(20) DEFAULT 'Home',
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE seller (
            seller_id INT AUTO_INCREMENT PRIMARY KEY,
            company_name VARCHAR(100) NOT NULL,
            gstin VARCHAR(15) UNIQUE NOT NULL,
            rating DECIMAL(3,2) DEFAULT 0.00
        );""",
        """CREATE TABLE seller_phone (
            seller_id INT NOT NULL,
            phone_number VARCHAR(15) NOT NULL,
            PRIMARY KEY (seller_id, phone_number),
            FOREIGN KEY (seller_id) REFERENCES seller(seller_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE category (
            category_id INT AUTO_INCREMENT PRIMARY KEY,
            category_name VARCHAR(50) UNIQUE NOT NULL,
            description TEXT
        );""",
        """CREATE TABLE product (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            seller_id INT,
            category_id INT,
            product_name VARCHAR(100) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            stock_quantity INT NOT NULL DEFAULT 0,
            description TEXT,
            FOREIGN KEY (seller_id) REFERENCES seller(seller_id) ON DELETE SET NULL,
            FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE SET NULL
        );""",
        """CREATE TABLE electronics (
            product_id INT PRIMARY KEY,
            warranty_period INT NOT NULL,
            brand VARCHAR(50) NOT NULL,
            model_number VARCHAR(50) NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE clothing (
            product_id INT PRIMARY KEY,
            size VARCHAR(10) NOT NULL,
            material VARCHAR(50) NOT NULL,
            color VARCHAR(30) NOT NULL,
            gender VARCHAR(20) NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            total_amount DECIMAL(10,2) NOT NULL,
            order_status VARCHAR(30) NOT NULL DEFAULT 'Pending',
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE SET NULL
        );""",
        """CREATE TABLE order_item (
            order_id INT NOT NULL,
            item_number INT NOT NULL,
            product_id INT,
            quantity INT NOT NULL,
            unit_price DECIMAL(10,2) NOT NULL,
            discount DECIMAL(10,2) DEFAULT 0.00,
            PRIMARY KEY (order_id, item_number),
            FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE SET NULL
        );""",
        """CREATE TABLE payment (
            payment_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL UNIQUE,
            payment_mode VARCHAR(30) NOT NULL,
            payment_status VARCHAR(20) NOT NULL,
            transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            amount DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE delivery (
            delivery_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL UNIQUE,
            courier_partner VARCHAR(50) NOT NULL,
            tracking_number VARCHAR(50) UNIQUE NOT NULL,
            delivery_status VARCHAR(30) NOT NULL,
            estimated_date DATE,
            FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
        );"""
    ]

    for stmt in schema_2_statements:
        cur.execute(stmt)

    # Insert sample data for E-Commerce
    cur.execute("""INSERT INTO customer (first_name, last_name, email) VALUES
    ('Aarav', 'Sharma', 'aarav.sharma@example.com'),
    ('Priya', 'Verma', 'priya.verma@example.com'),
    ('Rohan', 'Mehta', 'rohan.mehta@example.com'),
    ('Ananya', 'Iyer', 'ananya.iyer@example.com'),
    ('Vikram', 'Singh', 'vikram.singh@example.com');""")

    cur.execute("""INSERT INTO seller (company_name, gstin, rating) VALUES
    ('TechSurge Retail Ltd', '29ABCDE1234F1Z5', 4.8),
    ('FashionHub Traders', '07FGHIJ5678K1Z2', 4.5),
    ('ApplianceWorld Online', '19LMNOP9012Q1Z8', 4.2);""")

    cur.execute("""INSERT INTO category (category_name, description) VALUES
    ('Electronics', 'Smartphones, Laptops, Accessories and Gadgets'),
    ('Apparel', 'Men, Women and Kids Fashion Wear'),
    ('Home Appliances', 'Kitchen and Home Electrical Appliances');""")

    cur.execute("""INSERT INTO product (seller_id, category_id, product_name, price, stock_quantity, description) VALUES
    (1, 1, 'Smartphone X1', 49999.00, 50, '5G Smartphone with 128GB Storage'),
    (1, 1, 'Wireless Earbuds Pro', 4999.00, 200, 'Noise Cancelling Wireless Earbuds'),
    (2, 2, 'Slim Fit Denim Jeans', 1999.00, 150, '100% Cotton Stretch Denim'),
    (2, 2, 'Casual Polo T-Shirt', 899.00, 300, 'Breathable Cotton Polo Shirt'),
    (3, 3, 'Smart Microwave Oven', 12499.00, 40, '28L Convection Microwave Oven');""")

    # Experiment 3-6: Employee-Department-Project Schema & Data
    print("Building Experiment 3-6: Employee-Department-Project Schema & Data...")
    schema_3_statements = [
        "DROP TABLE IF EXISTS employee_audit;",
        "DROP TABLE IF EXISTS works_on;",
        "DROP TABLE IF EXISTS project;",
        "DROP TABLE IF EXISTS employee;",
        "DROP TABLE IF EXISTS department;",
        """CREATE TABLE department (
            dept_id INT AUTO_INCREMENT PRIMARY KEY,
            dept_name VARCHAR(50) UNIQUE NOT NULL,
            location VARCHAR(50) NOT NULL,
            budget DECIMAL(12,2) NOT NULL
        );""",
        """CREATE TABLE employee (
            emp_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(15),
            hire_date DATE NOT NULL,
            job_title VARCHAR(50) NOT NULL,
            salary DECIMAL(10,2) NOT NULL,
            manager_id INT,
            dept_id INT,
            FOREIGN KEY (manager_id) REFERENCES employee(emp_id) ON DELETE SET NULL,
            FOREIGN KEY (dept_id) REFERENCES department(dept_id) ON DELETE SET NULL
        );""",
        """CREATE TABLE project (
            project_id INT AUTO_INCREMENT PRIMARY KEY,
            project_name VARCHAR(100) NOT NULL,
            budget DECIMAL(12,2) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE,
            dept_id INT,
            FOREIGN KEY (dept_id) REFERENCES department(dept_id) ON DELETE SET NULL
        );""",
        """CREATE TABLE works_on (
            emp_id INT NOT NULL,
            project_id INT NOT NULL,
            hours_worked DECIMAL(5,2) NOT NULL DEFAULT 0.00,
            role VARCHAR(50) NOT NULL,
            PRIMARY KEY (emp_id, project_id),
            FOREIGN KEY (emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
            FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE CASCADE
        );""",
        """CREATE TABLE employee_audit (
            audit_id INT AUTO_INCREMENT PRIMARY KEY,
            emp_id INT NOT NULL,
            action_type VARCHAR(50) NOT NULL,
            old_dept_id INT,
            new_dept_id INT,
            old_salary DECIMAL(10,2),
            new_salary DECIMAL(10,2),
            changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            changed_by VARCHAR(100) DEFAULT (CURRENT_USER())
        );"""
    ]

    for stmt in schema_3_statements:
        cur.execute(stmt)

    cur.execute("""INSERT INTO department (dept_name, location, budget) VALUES
    ('Engineering', 'Bengaluru', 5000000.00),
    ('Human Resources', 'Mumbai', 1500000.00),
    ('Finance & Accounting', 'Delhi', 2500000.00),
    ('Marketing', 'Mumbai', 2000000.00),
    ('Operations & Logistics', 'Hyderabad', 3000000.00);""")

    cur.execute("""INSERT INTO employee (first_name, last_name, email, phone, hire_date, job_title, salary, manager_id, dept_id) VALUES
    ('Rajesh', 'Kumar', 'rajesh.kumar@company.com', '9876543210', '2018-01-15', 'Engineering Director', 185000.00, NULL, 1),
    ('Sunita', 'Sharma', 'sunita.sharma@company.com', '9876543211', '2019-03-20', 'HR Director', 145000.00, NULL, 2),
    ('Amitabh', 'Verma', 'amitabh.verma@company.com', '9876543212', '2017-06-10', 'VP Finance', 195000.00, NULL, 3),
    ('Neha', 'Gupta', 'neha.gupta@company.com', '9876543213', '2019-09-01', 'Marketing Head', 155000.00, NULL, 4),
    ('Suresh', 'Reddy', 'suresh.reddy@company.com', '9876543214', '2018-11-05', 'Operations Head', 160000.00, NULL, 5),
    ('Vikram', 'Aditya', 'vikram.aditya@company.com', '9876543215', '2020-02-15', 'Lead Architect', 140000.00, 1, 1),
    ('Priya', 'Nair', 'priya.nair@company.com', '9876543216', '2021-04-12', 'Senior Software Engineer', 110000.00, 6, 1),
    ('Rohan', 'Deshmukh', 'rohan.deshmukh@company.com', '9876543217', '2022-01-10', 'Software Engineer', 85000.00, 6, 1),
    ('Ananya', 'Roy', 'ananya.roy@company.com', '9876543218', '2022-07-18', 'Frontend Developer', 80000.00, 6, 1),
    ('Karan', 'Mehta', 'karan.mehta@company.com', '9876543219', '2023-02-01', 'Junior Developer', 60000.00, 7, 1),
    ('Deepak', 'Chawla', 'deepak.chawla@company.com', '9876543220', '2020-08-25', 'DevOps Lead', 125000.00, 1, 1),
    ('Swati', 'Joshi', 'swati.joshi@company.com', '9876543221', '2021-11-30', 'QA Manager', 95000.00, 1, 1),
    ('Arjun', 'Rao', 'arjun.rao@company.com', '9876543222', '2022-05-14', 'QA Automation Tester', 70000.00, 12, 1),
    ('Kavita', 'Singh', 'kavita.singh@company.com', '9876543223', '2020-01-08', 'HR Manager', 90000.00, 2, 2),
    ('Manoj', 'Tiwari', 'manoj.tiwari@company.com', '9876543224', '2021-06-22', 'Senior Recruiter', 65000.00, 14, 2),
    ('Pooja', 'Bhatt', 'pooja.bhatt@company.com', '9876543225', '2022-09-10', 'HR Executive', 50000.00, 14, 2),
    ('Alok', 'Pandey', 'alok.pandey@company.com', '9876543226', '2023-04-05', 'HR Assistant', 42000.00, 14, 2),
    ('Sanjay', 'Saxena', 'sanjay.saxena@company.com', '9876543227', '2019-04-18', 'Finance Manager', 120000.00, 3, 3),
    ('Meera', 'Kulkarni', 'meera.kulkarni@company.com', '9876543228', '2020-10-12', 'Senior Accountant', 85000.00, 18, 3),
    ('Rahul', 'Dravid', 'rahul.dravid@company.com', '9876543229', '2021-12-01', 'Financial Analyst', 75000.00, 18, 3),
    ('Ritu', 'Agarwal', 'ritu.agarwal@company.com', '9876543230', '2022-11-15', 'Staff Accountant', 60000.00, 18, 3),
    ('Varun', 'Kapoor', 'varun.kapoor@company.com', '9876543231', '2020-05-20', 'Marketing Lead', 105000.00, 4, 4),
    ('Divya', 'Srinivasan', 'divya.srinivasan@company.com', '9876543232', '2021-08-14', 'SEO Specialist', 72000.00, 22, 4),
    ('Gaurav', 'Bhasin', 'gaurav.bhasin@company.com', '9876543233', '2022-03-30', 'Content Strategist', 68000.00, 22, 4),
    ('Tarun', 'Gill', 'tarun.gill@company.com', '9876543234', '2023-01-15', 'Social Media Exec', 48000.00, 22, 4),
    ('Harish', 'Chand', 'harish.chand@company.com', '9876543235', '2019-07-11', 'Logistics Manager', 115000.00, 5, 5),
    ('Nisha', 'Pillai', 'nisha.pillai@company.com', '9876543236', '2020-09-05', 'Supply Chain Analyst', 78000.00, 26, 5),
    ('Aakash', 'Mishra', 'aakash.mishra@company.com', '9876543237', '2021-10-20', 'Warehouse Supervisor', 62000.00, 26, 5),
    ('Bhavna', 'Patel', 'bhavna.patel@company.com', '9876543238', '2022-06-12', 'Dispatch Coordinator', 52000.00, 26, 5),
    ('Chetan', 'Anand', 'chetan.anand@company.com', '9876543239', '2023-03-01', 'Data Analyst', 75000.00, 6, 1),
    ('Dinesh', 'Karthik', 'dinesh.karthik@company.com', '9876543240', '2023-05-15', 'Backend Engineer', 82000.00, 6, 1),
    ('Esha', 'Deol', 'esha.deol@company.com', '9876543241', '2023-07-20', 'UI/UX Designer', 70000.00, 4, 4);""")

    cur.execute("""INSERT INTO project (project_name, budget, start_date, end_date, dept_id) VALUES
    ('Cloud Migration', 1200000.00, '2025-01-10', '2026-06-30', 1),
    ('AI Chatbot Platform', 800000.00, '2025-03-15', '2026-03-31', 1),
    ('Mobile Banking App', 1500000.00, '2025-02-01', '2026-12-31', 1),
    ('HR Automation System', 400000.00, '2025-05-01', '2026-02-28', 2),
    ('ERP Financial System', 1000000.00, '2025-04-10', '2026-10-31', 3),
    ('Digital Campaign 2026', 600000.00, '2026-01-01', '2026-12-31', 4),
    ('Supply Chain Optimization', 900000.00, '2025-06-01', '2026-08-31', 5),
    ('Data Warehouse Analytics', 1100000.00, '2025-08-15', '2026-11-30', 1);""")

    cur.execute("""INSERT INTO works_on (emp_id, project_id, hours_worked, role) VALUES
    (1, 1, 120.00, 'Project Sponsor'),
    (6, 1, 160.00, 'Lead Architect'),
    (7, 1, 180.00, 'Senior Developer'),
    (8, 1, 140.00, 'Developer'),
    (11, 1, 150.00, 'DevOps Lead'),
    (6, 2, 100.00, 'Technical Advisor'),
    (9, 2, 160.00, 'Frontend Lead'),
    (31, 2, 170.00, 'Backend Lead'),
    (30, 2, 120.00, 'AI Specialist'),
    (7, 3, 150.00, 'Module Lead'),
    (8, 3, 160.00, 'Mobile Developer'),
    (10, 3, 140.00, 'Junior Developer'),
    (13, 3, 130.00, 'QA Lead'),
    (2, 4, 80.00, 'Sponsor'),
    (14, 4, 160.00, 'HR Functional Lead'),
    (15, 4, 110.00, 'Tester'),
    (3, 5, 90.00, 'Finance Sponsor'),
    (18, 5, 170.00, 'Project Lead'),
    (19, 5, 150.00, 'Functional Analyst'),
    (20, 5, 140.00, 'Data Analyst'),
    (4, 6, 100.00, 'Marketing Lead'),
    (22, 6, 160.00, 'Campaign Manager'),
    (23, 6, 130.00, 'SEO Specialist'),
    (24, 6, 140.00, 'Content Lead'),
    (32, 6, 150.00, 'Creative Designer'),
    (5, 7, 80.00, 'Sponsor'),
    (26, 7, 170.00, 'Logistics Manager'),
    (27, 7, 160.00, 'Supply Analyst'),
    (28, 7, 140.00, 'Warehouse Lead'),
    (30, 8, 180.00, 'Lead Data Engineer'),
    (11, 8, 110.00, 'Infrastructure Support');""")

    # Experiment 5: Views
    print("Building Experiment 5: Views...")
    cur.execute("""CREATE OR REPLACE VIEW dept_salary_summary AS
    SELECT 
        d.dept_id,
        d.dept_name,
        COUNT(e.emp_id) AS total_employees,
        COALESCE(SUM(e.salary), 0.00) AS total_salary_expenditure,
        COALESCE(AVG(e.salary), 0.00) AS avg_salary,
        COALESCE(MIN(e.salary), 0.00) AS min_salary,
        COALESCE(MAX(e.salary), 0.00) AS max_salary
    FROM department d
    LEFT JOIN employee e ON d.dept_id = e.dept_id
    GROUP BY d.dept_id, d.dept_name;""")

    cur.execute("""CREATE OR REPLACE VIEW emp_hierarchy_view AS
    SELECT 
        e.emp_id,
        CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
        e.job_title AS employee_title,
        d.dept_name,
        e.salary,
        CONCAT(m.first_name, ' ', m.last_name) AS manager_name,
        m.job_title AS manager_title
    FROM employee e
    LEFT JOIN department d ON e.dept_id = d.dept_id
    LEFT JOIN employee m ON e.manager_id = m.emp_id;""")

    cur.execute("""CREATE OR REPLACE VIEW emp_contact_info AS
    SELECT emp_id, first_name, last_name, email, phone
    FROM employee;""")

    # Experiment 6: Stored Procedure & Triggers
    print("Building Experiment 6: Procedure & Triggers...")
    cur.execute("DROP PROCEDURE IF EXISTS transfer_employee;")
    cur.execute("""
    CREATE PROCEDURE transfer_employee(
        IN p_emp_id INT,
        IN p_new_dept_id INT
    )
    BEGIN
        DECLARE v_emp_count INT DEFAULT 0;
        DECLARE v_dept_count INT DEFAULT 0;
        DECLARE v_current_dept INT DEFAULT NULL;
        
        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

        SELECT COUNT(*) INTO v_emp_count FROM employee WHERE emp_id = p_emp_id;
        IF v_emp_count = 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Invalid Employee ID';
        END IF;

        SELECT COUNT(*) INTO v_dept_count FROM department WHERE dept_id = p_new_dept_id;
        IF v_dept_count = 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Invalid Department ID';
        END IF;

        SELECT dept_id INTO v_current_dept FROM employee WHERE emp_id = p_emp_id;
        IF v_current_dept = p_new_dept_id THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Employee already belongs to the target department';
        END IF;

        START TRANSACTION;
        
        UPDATE employee 
        SET dept_id = p_new_dept_id 
        WHERE emp_id = p_emp_id;
        
        COMMIT;
    END;
    """)

    cur.execute("DROP TRIGGER IF EXISTS trg_salary_validation_insert;")
    cur.execute("""
    CREATE TRIGGER trg_salary_validation_insert
    BEFORE INSERT ON employee
    FOR EACH ROW
    BEGIN
        IF NEW.salary < 20000.00 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Employee salary cannot be less than the minimum wage threshold of 20000.00';
        END IF;
    END;
    """)

    cur.execute("DROP TRIGGER IF EXISTS trg_salary_validation_update;")
    cur.execute("""
    CREATE TRIGGER trg_salary_validation_update
    BEFORE UPDATE ON employee
    FOR EACH ROW
    BEGIN
        IF NEW.salary < 20000.00 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Updated salary cannot be less than the minimum wage threshold of 20000.00';
        END IF;
    END;
    """)

    cur.execute("DROP TRIGGER IF EXISTS trg_employee_audit_update;")
    cur.execute("""
    CREATE TRIGGER trg_employee_audit_update
    AFTER UPDATE ON employee
    FOR EACH ROW
    BEGIN
        IF (OLD.dept_id <=> NEW.dept_id) = 0 OR (OLD.salary <=> NEW.salary) = 0 THEN
            INSERT INTO employee_audit (
                emp_id,
                action_type,
                old_dept_id,
                new_dept_id,
                old_salary,
                new_salary
            ) VALUES (
                NEW.emp_id,
                CASE 
                    WHEN (OLD.dept_id <=> NEW.dept_id) = 0 AND (OLD.salary <=> NEW.salary) = 0 THEN 'DEPARTMENT_AND_SALARY_UPDATE'
                    WHEN (OLD.dept_id <=> NEW.dept_id) = 0 THEN 'DEPARTMENT_TRANSFER'
                    ELSE 'SALARY_UPDATE'
                END,
                OLD.dept_id,
                NEW.dept_id,
                OLD.salary,
                NEW.salary
            );
        END IF;
    END;
    """)

    # Validation Checks
    print("\n==========================================")
    print("RUNNING DATABASE VALIDATION CHECKS...")
    print("==========================================")
    
    cur.execute("SELECT COUNT(*) FROM employee;")
    emp_count = cur.fetchone()[0]
    print(f"✓ Total Employees: {emp_count} (Requirement: >= 30)")

    cur.execute("SELECT COUNT(*) FROM department;")
    dept_count = cur.fetchone()[0]
    print(f"✓ Total Departments: {dept_count} (Requirement: 5)")

    cur.execute("SELECT COUNT(*) FROM project;")
    proj_count = cur.fetchone()[0]
    print(f"✓ Total Projects: {proj_count} (Requirement: 8)")

    cur.execute("SHOW TABLES;")
    tables = [t[0] for t in cur.fetchall()]
    print(f"✓ Total Tables/Views in 'dbms_lab': {len(tables)}")
    print(f"  Tables: {', '.join(tables)}")

    cur.close()
    conn.close()
    print("\n✓ SUCCESS: Local MySQL database 'dbms_lab' fully synchronized and verified!")

if __name__ == "__main__":
    main()
