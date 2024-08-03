SELECT
    employee_id,
    COUNT(employee_id) OVER (PARTITION BY team_id) AS team_size
FROM Employee;
