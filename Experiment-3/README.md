# Experiment 3: Employee–Department–Project Schema & Basic Queries

## Overview
This experiment constructs a corporate Employee–Department–Project database system fulfilling all requirements: 32 employees (exceeding the 30 employee minimum), 5 departments, 8 active projects, and project assignments. It demonstrates fundamental DML operations: Selection, Projection, Aggregates, `GROUP BY`, `HAVING`, `CASE` expressions, and `ORDER BY`.

---

## Files in this Directory
- `schema.sql`: Contains DDL statements for `department`, `employee`, `project`, and `works_on` tables.
- `sample_data.sql`: Contains population scripts for 5 departments, 32 employees, 8 projects, and 31 project assignments.
- `queries.sql`: Executable SQL statements demonstrating all required basic query types.
- `README.md`: Comprehensive documentation explaining the schema and queries.

---

## Schema Architecture

1. **`department`**: Represents organization departments.
   - Columns: `dept_id` (PK), `dept_name` (UNIQUE NOT NULL), `location`, `budget`.
2. **`employee`**: Stores employee details with recursive self-referencing management hierarchy.
   - Columns: `emp_id` (PK), `first_name`, `last_name`, `email` (UNIQUE NOT NULL), `phone`, `hire_date`, `job_title`, `salary`, `manager_id` (FK to `employee`), `dept_id` (FK to `department`).
3. **`project`**: Corporate initiatives attached to departments.
   - Columns: `project_id` (PK), `project_name`, `budget`, `start_date`, `end_date`, `dept_id` (FK to `department`).
4. **`works_on`**: M:N junction table between employees and projects.
   - Columns: (`emp_id`, `project_id`) Composite PK, `hours_worked`, `role`.

---

## Query Breakdown & Explanations

### 1. Selection (`WHERE` Clause)
- Filters rows based on a specific boolean condition.
- Query filters employees earning a salary strictly greater than ₹1,00,000.00.

### 2. Projection (`SELECT` Columns)
- Retrieves only specific attributes (`emp_id`, `first_name`, `last_name`, `job_title`, `salary`) rather than `SELECT *`.

### 3. Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
- Computes summary statistics over the entire employee population: total headcount, total payroll, average salary, minimum salary, and maximum salary.

### 4. Grouping (`GROUP BY`)
- Aggregates metrics per department group (`dept_id`), displaying employee count, average salary, and total payroll per department.

### 5. Group Filtering (`HAVING` Clause)
- Filters aggregated groups. Filters departments having at least 5 employees AND an average departmental salary exceeding ₹75,000.00.

### 6. Conditional Classification (`CASE` Expression)
- Evaluates individual employee salaries and assigns a human-readable grade label:
  - Salary ≥ ₹1,50,000 → 'Executive Tier'
  - Salary ≥ ₹1,00,000 → 'Senior Tier'
  - Salary ≥ ₹70,000 → 'Mid-Level Tier'
  - Otherwise → 'Junior Tier'

### 7. Sorting (`ORDER BY`)
- Orders the result set primarily by `salary` descending, and secondarily by `last_name` ascending.
