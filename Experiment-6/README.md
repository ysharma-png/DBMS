# Experiment 6: Stored Procedures, Triggers, & Edge-Case Testing

## Overview
This experiment implements advanced database programming in MySQL using Stored Procedures and Triggers. It encapsulates business logic for employee department transfers inside an atomic transaction, enforces minimum wage rules via validation triggers, and maintains an automated audit log table.

---

## Files in this Directory
- `procedure.sql`: DDL for stored procedure `transfer_employee(emp_id, new_dept_id)` with input validation, error signals, and transaction handling.
- `triggers.sql`: DDL for audit table `employee_audit` and triggers (`trg_salary_validation_insert`, `trg_salary_validation_update`, `trg_employee_audit_update`).
- `test_cases.sql`: Executable SQL calls testing edge cases, boundary conditions, error handling, successful operations, and audit logging.
- `README.md`: Detailed documentation and test case breakdown.

---

## Stored Procedure (`transfer_employee`)

### Architecture & Logic
- **Parameters**: `p_emp_id INT` (Target Employee ID), `p_new_dept_id INT` (Target Department ID).
- **Validation Checks**:
  1. Checks if `p_emp_id` exists in `employee`. If missing, raises `Error: Invalid Employee ID`.
  2. Checks if `p_new_dept_id` exists in `department`. If missing, raises `Error: Invalid Department ID`.
  3. Checks if the employee already belongs to `p_new_dept_id`. If so, raises `Error: Employee already belongs to the target department`.
- **Transaction & Error Recovery**:
  - `DECLARE EXIT HANDLER FOR SQLEXCEPTION`: Executes `ROLLBACK` and `RESIGNAL` upon runtime failure.
  - `START TRANSACTION`: Initiates atomic transaction.
  - `UPDATE employee`: Transfers the employee to the new department.
  - `COMMIT`: Persists changes upon successful update.

---

## Triggers & Audit Logging

1. **Salary Validation Triggers (`trg_salary_validation_insert`, `trg_salary_validation_update`)**:
   - `BEFORE INSERT` and `BEFORE UPDATE` on `employee`.
   - Rejects inserts or updates where `salary < 20000.00` with `Error: Employee salary cannot be less than the minimum wage threshold of 20000.00`.

2. **Audit Logging Trigger (`trg_employee_audit_update`)**:
   - `AFTER UPDATE` on `employee`.
   - Captures changes to `dept_id` or `salary` and automatically inserts a record into `employee_audit` containing `emp_id`, `action_type`, `old_dept_id`, `new_dept_id`, `old_salary`, `new_salary`, `changed_at`, and `changed_by`.

---

## Edge Case Test Suite Breakdown

### Test Case 1: Invalid Employee ID
- **Call**: `CALL transfer_employee(9999, 1);`
- **Expected Outcome**: Fails with `ERROR 45000: Error: Invalid Employee ID`.

### Test Case 2: Invalid Department ID
- **Call**: `CALL transfer_employee(7, 9999);`
- **Expected Outcome**: Fails with `ERROR 45000: Error: Invalid Department ID`.

### Test Case 3: Duplicate Department Transfer
- **Call**: `CALL transfer_employee(7, 1);` (Employee 7 is currently in Dept 1)
- **Expected Outcome**: Fails with `ERROR 45000: Error: Employee already belongs to the target department`.

### Test Case 4: Invalid Salary Insert Trigger Violation
- **Call**: `INSERT INTO employee ... VALUES (..., 15000.00, ...);`
- **Expected Outcome**: Fails with `ERROR 45000: Error: Employee salary cannot be less than the minimum wage threshold of 20000.00`.

### Test Case 5: Invalid Salary Update Trigger Violation
- **Call**: `UPDATE employee SET salary = 12000.00 WHERE emp_id = 7;`
- **Expected Outcome**: Fails with `ERROR 45000: Error: Updated salary cannot be less than the minimum wage threshold of 20000.00`.

### Test Case 6: Successful Transfer & Trigger Audit Record Generation
- **Call**: `CALL transfer_employee(7, 2);`
- **Expected Outcome**: Transaction commits successfully. Employee 7 is transferred from Department 1 to Department 2.
- **Verification**: `SELECT * FROM employee_audit;` shows a new record logged with `action_type = 'DEPARTMENT_TRANSFER'`, `old_dept_id = 1`, `new_dept_id = 2`.
