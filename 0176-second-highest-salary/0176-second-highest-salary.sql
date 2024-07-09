WITH second_highest_salary_list AS (

    SELECT
        id,
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rn
    FROM Employee

)

SELECT DISTINCT
    CASE 
        WHEN (SELECT MAX(rn) FROM second_highest_salary_list) >= 2 THEN (SELECT DISTINCT salary FROM second_highest_salary_list WHERE rn = 2)
        ELSE NULL 
    END AS SecondHighestSalary
FROM Employee;

