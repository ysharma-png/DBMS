WITH RECURSIVE emp_reporting_chain AS (
    SELECT 
        emp_id,
        first_name,
        last_name,
        job_title,
        manager_id,
        1 AS reporting_level,
        CAST(CONCAT(first_name, ' ', last_name) AS CHAR(500)) AS hierarchy_path
    FROM employee
    WHERE manager_id IS NULL

    UNION ALL

    SELECT 
        e.emp_id,
        e.first_name,
        e.last_name,
        e.job_title,
        e.manager_id,
        r.reporting_level + 1 AS reporting_level,
        CAST(CONCAT(r.hierarchy_path, ' -> ', e.first_name, ' ', e.last_name) AS CHAR(500)) AS hierarchy_path
    FROM employee e
    INNER JOIN emp_reporting_chain r ON e.manager_id = r.emp_id
)
SELECT 
    emp_id,
    hierarchy_path,
    reporting_level,
    job_title
FROM emp_reporting_chain
ORDER BY hierarchy_path;
