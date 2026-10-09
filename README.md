# Database Management Systems (DBMS) Lab

## Course Details
- **Course**: DBMS Lab (B.Tech Computer Science & Engineering)
- **Database Engine**: MySQL 8.0+

---

## Repository Structure & Overview

This repository contains the complete implementation of Experiments 1 through 6 for the DBMS Laboratory course. Each experiment is organized in its dedicated directory containing production-ready SQL scripts and detailed documentation.

```text
DBMS/
├── README.md
├── Experiment-1/
│   ├── ER_Diagram.png
│   └── README.md
├── Experiment-2/
│   ├── schema.sql
│   ├── sample_data.sql
│   ├── referential_integrity.sql
│   └── README.md
├── Experiment-3/
│   ├── schema.sql
│   ├── sample_data.sql
│   ├── queries.sql
│   └── README.md
├── Experiment-4/
│   ├── queries.sql
│   ├── explain_plans.sql
│   └── README.md
├── Experiment-5/
│   ├── views.sql
│   ├── recursive_cte.sql
│   └── README.md
└── Experiment-6/
    ├── procedure.sql
    ├── triggers.sql
    ├── test_cases.sql
    └── README.md
```

---

## Summary of Experiments

### Experiment 1: ER Diagram Design — Indian E-Commerce Platform
- **Description**: Conceptual design of an Indian E-Commerce platform managing Customers, Addresses, Sellers, Categories, Products (with Specialization into Electronics and Clothing), Orders, Weak Entity OrderItems, Payments, and Deliveries.
- **Key Concepts**: Primary keys, composite attributes, multi-valued attributes, weak entities, IS-A specialization, participation constraints.
- **Files**: `ER_Diagram.png`, `README.md`.

### Experiment 2: Relational Schema & MySQL Implementation
- **Description**: Mapping of the Experiment 1 ER diagram into a MySQL relational schema with 13 tables.
- **Key Concepts**: Primary keys, foreign keys, `NOT NULL`, `UNIQUE`, `ON DELETE CASCADE`, `ON DELETE SET NULL`, referential integrity tests.
- **Files**: `schema.sql`, `sample_data.sql`, `referential_integrity.sql`, `README.md`.

### Experiment 3: Employee–Department–Project Schema & Basic Queries
- **Description**: Enterprise Employee–Department–Project schema containing 32 employees (>30 required), 5 departments, 8 projects, and assignment junction table.
- **Key Concepts**: Selection, Projection, Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), `GROUP BY`, `HAVING`, `CASE` statements, `ORDER BY`.
- **Files**: `schema.sql`, `sample_data.sql`, `queries.sql`, `README.md`.

### Experiment 4: Advanced Joins, Subqueries, Set Operations, & EXPLAIN Plans
- **Description**: Advanced relational operations on the Employee schema.
- **Key Concepts**: `INNER JOIN`, `LEFT JOIN`, `SELF JOIN`, 3-way `JOIN`, correlated subqueries, `EXISTS`, simulated `INTERSECT`, simulated `EXCEPT`, `EXPLAIN` query execution plans.
- **Files**: `queries.sql`, `explain_plans.sql`, `README.md`.

### Experiment 5: Views, Updatability, & Recursive CTEs
- **Description**: Creation of database views for reporting and security, testing MySQL view updatability rules, and organizational hierarchy traversal using Recursive CTEs.
- **Key Concepts**: Aggregate summary views, multi-table hierarchy views, updatable 1:1 views, MySQL view updatability constraints, MySQL 8.0 `WITH RECURSIVE` reporting chains.
- **Files**: `views.sql`, `recursive_cte.sql`, `README.md`.

### Experiment 6: Stored Procedures, Triggers, & Edge-Case Testing
- **Description**: Programmatic DBMS components enforcing business logic, data validation, and transaction safety.
- **Key Concepts**: Stored procedure `transfer_employee`, input validation, custom error handling (`SIGNAL SQLSTATE '45000'`), transaction management (`START TRANSACTION`, `COMMIT`, `ROLLBACK`), salary validation triggers, automated audit table logging.
- **Files**: `procedure.sql`, `triggers.sql`, `test_cases.sql`, `README.md`.

---

## How to Execute SQL Scripts in MySQL

Launch MySQL CLI or Workbench and run the experiments sequentially:

### 1. Execute Experiment 2 (E-Commerce Schema)
```bash
mysql -u root -p < Experiment-2/schema.sql
mysql -u root -p < Experiment-2/sample_data.sql
mysql -u root -p < Experiment-2/referential_integrity.sql
```

### 2. Execute Experiment 3 (Employee Schema & Basic Queries)
```bash
mysql -u root -p < Experiment-3/schema.sql
mysql -u root -p < Experiment-3/sample_data.sql
mysql -u root -p < Experiment-3/queries.sql
```

### 3. Execute Experiment 4 (Advanced Joins & EXPLAIN Plans)
```bash
mysql -u root -p < Experiment-4/queries.sql
mysql -u root -p < Experiment-4/explain_plans.sql
```

### 4. Execute Experiment 5 (Views & Recursive CTE)
```bash
mysql -u root -p < Experiment-5/views.sql
mysql -u root -p < Experiment-5/recursive_cte.sql
```

### 5. Execute Experiment 6 (Procedure, Triggers & Test Suite)
```bash
mysql -u root -p < Experiment-6/procedure.sql
mysql -u root -p < Experiment-6/triggers.sql
mysql -u root -p < Experiment-6/test_cases.sql
```

---

## Expected Errors in Referential Integrity & Edge-Case Test Suites

When executing `referential_integrity.sql` (Experiment 2), `views.sql` (Experiment 5), and `test_cases.sql` (Experiment 6), the following errors are expected by design to demonstrate DBMS constraint enforcement:

1. **`Experiment-2/referential_integrity.sql`**:
   - `ERROR 1062 (23000)`: Duplicate entry for unique email constraint.
   - `ERROR 1452 (23000)`: Foreign key constraint failure (non-existent customer ID).
   - `ERROR 1048 (23000)`: `NOT NULL` constraint violation.
   - `ERROR 1062 (23000)`: Composite Primary Key duplicate entry in `order_item`.
2. **`Experiment-5/views.sql`**:
   - `ERROR 1288 (HY000)`: Non-updatable view update attempt on `dept_salary_summary` due to aggregate functions/grouping.
3. **`Experiment-6/test_cases.sql`**:
   - `ERROR 45000`: `Error: Invalid Employee ID` (transfer call with invalid emp_id).
   - `ERROR 45000`: `Error: Invalid Department ID` (transfer call with invalid dept_id).
   - `ERROR 45000`: `Error: Employee already belongs to the target department`.
   - `ERROR 45000`: Minimum wage threshold trigger violation on insert/update (`salary < 20000.00`).