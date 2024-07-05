WITH salary_rank_list AS (
    SELECT
        Department.name AS Department,
        Employee.name AS Employee,
        Employee.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY Department.id ORDER BY Employee.salary DESC) AS rank
    FROM Department
    INNER JOIN Employee
        ON Department.id = Employee.departmentId
)

SELECT 
    Department,
    Employee,
    Salary
FROM salary_rank_list
WHERE rank <= 3;
