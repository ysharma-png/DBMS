CREATE OR REPLACE VIEW dept_salary_summary AS
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
GROUP BY d.dept_id, d.dept_name;

CREATE OR REPLACE VIEW emp_hierarchy_view AS
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
LEFT JOIN employee m ON e.manager_id = m.emp_id;

CREATE OR REPLACE VIEW emp_contact_info AS
SELECT emp_id, first_name, last_name, email, phone
FROM employee;

SELECT * FROM dept_salary_summary;

SELECT * FROM emp_hierarchy_view;

UPDATE emp_contact_info 
SET phone = '9999988888' 
WHERE emp_id = 7;

SELECT emp_id, first_name, last_name, phone FROM employee WHERE emp_id = 7;

UPDATE dept_salary_summary 
SET total_salary_expenditure = 500000.00 
WHERE dept_id = 1;
