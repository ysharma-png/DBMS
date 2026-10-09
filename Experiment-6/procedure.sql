DROP PROCEDURE IF EXISTS transfer_employee;

DELIMITER //

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
END //

DELIMITER ;
