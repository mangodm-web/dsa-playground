SELECT 
    CASE
      WHEN Employees.employee_id IS NULL THEN Salaries.employee_id
      WHEN Salaries.employee_id IS NULL THEN Employees.employee_id
    END AS employee_id
FROM Employees
FULL JOIN Salaries
    ON Employees.employee_id = Salaries.employee_id
WHERE Employees.employee_id IS NULL 
   OR Salaries.employee_id IS NULL
ORDER BY employee_id;
