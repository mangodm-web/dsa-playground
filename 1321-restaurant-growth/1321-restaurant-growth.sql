WITH daily_sum_list AS (
    SELECT
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
)

SELECT
    visited_on,
    SUM(daily_amount) OVER (
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    ROUND(AVG(daily_amount) OVER (
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 2) AS average_amount
FROM daily_sum_list
OFFSET 6;
