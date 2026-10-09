CREATE TABLE IF NOT EXISTS employee_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    action_type VARCHAR(50) NOT NULL,
    old_dept_id INT,
    new_dept_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(100) DEFAULT (CURRENT_USER())
);

DROP TRIGGER IF EXISTS trg_salary_validation_insert;

DELIMITER //

CREATE TRIGGER trg_salary_validation_insert
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
    IF NEW.salary < 20000.00 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Employee salary cannot be less than the minimum wage threshold of 20000.00';
    END IF;
END //

DELIMITER ;

DROP TRIGGER IF EXISTS trg_salary_validation_update;

DELIMITER //

CREATE TRIGGER trg_salary_validation_update
BEFORE UPDATE ON employee
FOR EACH ROW
BEGIN
    IF NEW.salary < 20000.00 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Updated salary cannot be less than the minimum wage threshold of 20000.00';
    END IF;
END //

DELIMITER ;

DROP TRIGGER IF EXISTS trg_employee_audit_update;

DELIMITER //

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
END //

DELIMITER ;
