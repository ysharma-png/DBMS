CALL transfer_employee(9999, 1);

CALL transfer_employee(7, 9999);

CALL transfer_employee(7, 1);

INSERT INTO employee (first_name, last_name, email, phone, hire_date, job_title, salary, manager_id, dept_id)
VALUES ('Test', 'User', 'test.user@company.com', '9000000000', '2026-01-01', 'Trainee', 15000.00, 1, 1);

UPDATE employee SET salary = 12000.00 WHERE emp_id = 7;

CALL transfer_employee(7, 2);

SELECT emp_id, first_name, last_name, dept_id FROM employee WHERE emp_id = 7;

SELECT * FROM employee_audit;
