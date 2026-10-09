SELECT * FROM employee WHERE salary > 100000.00;

SELECT emp_id, first_name, last_name, job_title, salary FROM employee;

SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_payroll,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employee;

SELECT 
    dept_id,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_dept_salary,
    SUM(salary) AS total_dept_salary
FROM employee
GROUP BY dept_id;

SELECT 
    dept_id,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_dept_salary
FROM employee
GROUP BY dept_id
HAVING COUNT(*) >= 5 AND AVG(salary) > 75000.00;

SELECT 
    emp_id,
    first_name,
    last_name,
    salary,
    CASE 
        WHEN salary >= 150000.00 THEN 'Executive Tier'
        WHEN salary >= 100000.00 THEN 'Senior Tier'
        WHEN salary >= 70000.00 THEN 'Mid-Level Tier'
        ELSE 'Junior Tier'
    END AS salary_bracket
FROM employee;

SELECT 
    emp_id,
    first_name,
    last_name,
    job_title,
    salary,
    hire_date
FROM employee
ORDER BY salary DESC, last_name ASC;
