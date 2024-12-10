WITH salary_list AS (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employee
)

SELECT DISTINCT salary
FROM salary_list
WHERE salary_rank = 2;
