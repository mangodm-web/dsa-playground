WITH salary_category_list AS (
    SELECT
        'Low Salary' AS category,
        0 AS min_range,
        19999 AS max_range
    UNION
    SELECT
        'Average Salary' AS category,
        20000 AS min_range,
        50000 AS max_range
    UNION
    SELECT
        'High Salary' AS category,
        50001 AS min_range,
        (2^31 - 1) AS max_range
)

SELECT
    salary_category_list.category,
    COUNT(Accounts.account_id) AS accounts_count
FROM salary_category_list
LEFT JOIN Accounts
    ON salary_category_list.min_range <= Accounts.income
    AND salary_category_list.max_range >= Accounts.income
GROUP BY salary_category_list.category;
