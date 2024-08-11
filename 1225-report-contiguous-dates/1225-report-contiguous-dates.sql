WITH task_group_list AS (
    SELECT
        'failed' AS period_state,
        fail_date AS event_date,
        ROW_NUMBER() OVER (ORDER BY fail_date) AS rn
    FROM Failed
    WHERE EXTRACT(YEAR FROM fail_date) = 2019
    UNION
    SELECT
        'succeeded' AS period_state,
        success_date AS event_date,
        ROW_NUMBER() OVER (ORDER BY success_date) AS rn
    FROM Succeeded
    WHERE EXTRACT(YEAR FROM success_date) = 2019
)

SELECT
    MIN(period_state) AS period_state,
    MIN(event_date) AS start_date,
    MAX(event_date) AS end_date
FROM task_group_list
GROUP BY event_date - INTERVAL '1 DAY' * rn
ORDER BY start_date;
