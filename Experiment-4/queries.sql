SELECT e.emp_id, e.first_name, e.last_name, d.dept_name, d.location 
FROM employee e 
INNER JOIN department d ON e.dept_id = d.dept_id;

SELECT d.dept_id, d.dept_name, p.project_id, p.project_name, p.budget 
FROM department d 
LEFT JOIN project p ON d.dept_id = p.dept_id;

SELECT e.emp_id, e.first_name AS emp_first_name, e.last_name AS emp_last_name, e.job_title AS emp_title,
       m.emp_id AS manager_id, m.first_name AS manager_first_name, m.last_name AS manager_last_name, m.job_title AS manager_title
FROM employee e
LEFT JOIN employee m ON e.manager_id = m.emp_id;

SELECT e.emp_id, e.first_name, e.last_name, p.project_name, w.role, w.hours_worked
FROM employee e
INNER JOIN works_on w ON e.emp_id = w.emp_id
INNER JOIN project p ON w.project_id = p.project_id;

SELECT e1.emp_id, e1.first_name, e1.last_name, e1.dept_id, e1.salary
FROM employee e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e1.dept_id
);

SELECT d.dept_id, d.dept_name, d.location
FROM department d
WHERE EXISTS (
    SELECT 1 FROM project p WHERE p.dept_id = d.dept_id AND p.budget > 1000000.00
);

SELECT e.emp_id, e.first_name, e.last_name
FROM employee e
WHERE e.emp_id IN (SELECT emp_id FROM works_on WHERE project_id = 1)
  AND e.emp_id IN (SELECT emp_id FROM works_on WHERE project_id = 2);

SELECT e.emp_id, e.first_name, e.last_name, e.job_title
FROM employee e
WHERE e.dept_id = 1
  AND NOT EXISTS (
    SELECT 1 FROM works_on w WHERE w.emp_id = e.emp_id
  );
