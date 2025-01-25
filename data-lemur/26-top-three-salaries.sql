WITH salary_rank_list AS (
    SELECT
        department.department_name,
        employee.name,
        employee.salary,
        DENSE_RANK() OVER (
            PARTITION BY department.department_name
            ORDER BY employee.salary DESC
        ) AS ranking
    FROM employee
    INNER JOIN department
        ON employee.department_id = department.department_id
)

SELECT
    department_name,
    name,
    salary
FROM salary_rank_list
WHERE ranking <= 3
ORDER BY
    department_name,
    salary DESC,
    name;
