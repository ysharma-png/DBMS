# Experiment 5: Views, Updatability, & Recursive CTEs

## Overview
This experiment creates database views to simplify complex queries and restrict sensitive data exposure. It tests MySQL View Updatability constraints and constructs a Recursive Common Table Expression (CTE) to traverse organizational hierarchy trees.

---

## Files in this Directory
- `views.sql`: DDL for database views (`dept_salary_summary`, `emp_hierarchy_view`, `emp_contact_info`) and updatability test cases.
- `recursive_cte.sql`: MySQL 8.0 `WITH RECURSIVE` query displaying complete employee reporting paths and hierarchy levels.
- `README.md`: Detailed documentation and theoretical explanations.

---

## Views Breakdown

### 1. `dept_salary_summary` (Aggregate Summary View)
- Computes aggregated departmental statistics: total employee count, total salary expenditure, average salary, minimum salary, and maximum salary per department.
- Utilizes `LEFT JOIN` to include departments with zero employees.

### 2. `emp_hierarchy_view` (Relational Hierarchy View)
- Joins `employee` with `department` and self-joins `employee` with `manager` to present a unified organizational perspective: employee name, title, department, salary, manager name, and manager title.

### 3. `emp_contact_info` (Simple 1:1 Projection View)
- Exposes non-sensitive employee contact details (`emp_id`, `first_name`, `last_name`, `email`, `phone`).

---

## View Updatability Analysis

MySQL determines view updatability based on the underlying SELECT query structure:

### 1. Updatable View Test (`emp_contact_info`)
- **Statement**: `UPDATE emp_contact_info SET phone = '9999988888' WHERE emp_id = 7;`
- **Result**: Successfully executes and updates the underlying `employee` table row.
- **Reason**: The view contains a 1:1 mapping to a single base table without aggregate functions, `GROUP BY`, `DISTINCT`, or `UNION`.

### 2. Non-Updatable View Test (`dept_salary_summary`)
- **Statement**: `UPDATE dept_salary_summary SET total_salary_expenditure = 500000.00 WHERE dept_id = 1;`
- **Result**: Fails with `ERROR 1288 (HY000): The target table dept_salary_summary of the UPDATE is not updatable`.
- **Reason**: Views containing aggregate functions (`SUM`, `AVG`, `COUNT`), `GROUP BY`, or `HAVING` clauses are fundamentally non-updatable because individual base table rows cannot be uniquely derived from grouped aggregate values.

---

## Recursive CTE (`emp_reporting_chain`)

The recursive CTE computes reporting chains from top-level executives down through all management tiers:

1. **Anchor Member**:
   - Queries top-level executives where `manager_id IS NULL`.
   - Initializes `reporting_level = 1` and `hierarchy_path` with executive name.
2. **Recursive Member**:
   - Performs `INNER JOIN` between `employee e` and `emp_reporting_chain r` on `e.manager_id = r.emp_id`.
   - Increments `reporting_level = r.reporting_level + 1`.
   - Appends child employee name to `hierarchy_path` (e.g., `Rajesh Kumar -> Vikram Aditya -> Priya Nair`).
