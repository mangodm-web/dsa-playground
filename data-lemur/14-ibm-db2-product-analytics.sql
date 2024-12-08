WITH query_count_by_employee_list AS (
    SELECT
        employees.employee_id,
        COALESCE(COUNT(queries.query_id), 0) AS query_count
    FROM employees
    LEFT JOIN queries
        ON
            employees.employee_id = queries.employee_id
            AND queries.query_starttime >= '2023-07-01'
            AND queries.query_starttime < '2023-10-01'
    GROUP BY employees.employee_id
)

SELECT
    query_count AS unique_queries,
    COUNT(*) AS employee_count
FROM query_count_by_employee_list
GROUP BY unique_queries
ORDER BY unique_queries;
