# Experiment 4: Advanced Joins, Subqueries, Set Operations, & EXPLAIN Plans

## Overview
This experiment implements advanced relational queries on the Employee–Department–Project schema. It demonstrates relational joins (`INNER`, `LEFT`, `SELF`, 3-way `JOIN`), correlated subqueries, existential quantification (`EXISTS`), simulated set operations (`INTERSECT` and `EXCEPT`), and analyzes query optimization using `EXPLAIN` execution plans.

---

## Files in this Directory
- `queries.sql`: Contains pure executable SQL queries for all required join types, subqueries, and set operations.
- `explain_plans.sql`: Contains `EXPLAIN` statements for key query patterns to analyze execution performance.
- `README.md`: Comprehensive documentation explaining query design and execution plan analysis.

---

## Query Explanations

### 1. INNER JOIN
- Combines `employee` and `department` tables on `dept_id`.
- Returns only employees who belong to a valid department.

### 2. LEFT OUTER JOIN
- Performs a `LEFT JOIN` between `department` and `project`.
- Returns all departments, including departments that currently have no assigned projects (null-padded for project columns).

### 3. SELF JOIN
- Joins the `employee` table with itself using `e.manager_id = m.emp_id`.
- Pairwise maps each employee to their respective manager's name and title.

### 4. 3-Way JOIN
- Joins `employee`, `works_on` junction table, and `project`.
- Resolves the many-to-many relationship, displaying employee name, assigned project name, role, and hours worked.

### 5. Correlated Subquery
- Finds employees whose salary is strictly greater than the average salary of **their own department**.
- For each candidate row in the outer `e1` query, the inner subquery dynamically computes `AVG(e2.salary)` for `e2.dept_id = e1.dept_id`.

### 6. EXISTS Subquery
- Retrieves departments that have at least one high-budget project (> ₹1,00,00,000.00).
- Employs semi-join evaluation: processing short-circuits as soon as a matching project row is found.

### 7. Simulated INTERSECT (Set Intersection)
- MySQL 8.0 `INTERSECT` set operation equivalent: finds employees who work on **both** Project 1 AND Project 2.
- Implemented using multiple `IN (SELECT ...)` subqueries to guarantee portability across SQL dialects.

### 8. Simulated EXCEPT (Set Difference)
- MySQL 8.0 `EXCEPT` set operation equivalent: finds employees in Department 1 (Engineering) who are **NOT** assigned to any project in `works_on`.
- Implemented using `NOT EXISTS (SELECT 1 FROM works_on w WHERE w.emp_id = e.emp_id)`.

---

## EXPLAIN Execution Plan Analysis

Running `EXPLAIN` on these queries allows inspecting the MySQL Query Optimizer execution path:

1. **INNER JOIN & 3-Way JOIN**:
   - `type`: `eq_ref` / `ref` using Primary Key or Foreign Key indexes.
   - Low row scan cost, efficient nested loop join strategy.

2. **Correlated Subquery**:
   - `select_type`: `DEPENDENT SUBQUERY`.
   - Executed once for each outer row. Indexing `dept_id` on `employee` optimizes the aggregate evaluation per group.

3. **EXISTS (Semi-Join Optimization)**:
   - MySQL transforms `EXISTS` into a semi-join execution plan (`type: ref`), scanning only until the first matching row is encountered.

4. **Simulated Set Operations**:
   - `IN` / `NOT EXISTS` clauses utilize index subquery strategies (`unique_subquery` or `materialized subquery`), delivering optimal performance comparable to native `INTERSECT` / `EXCEPT`.
