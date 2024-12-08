SELECT
    e1.employee_id,
    e1.name AS employee_name
FROM employee AS e1
INNER JOIN employee AS e2
    ON e1.manager_id = e2.employee_id
WHERE e1.salary > e2.salary;
