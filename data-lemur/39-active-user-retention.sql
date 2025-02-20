-- Active User Retention
WITH active_users_list AS (
    SELECT
        user_id,
        COUNT(DISTINCT EXTRACT(MONTH FROM event_date)) AS month_count,
        MAX(EXTRACT(MONTH FROM event_date)) AS month
    FROM user_actions
    WHERE event_date >= '2022-06-01'
      AND event_date < '2022-08-01'
    GROUP BY user_id
    HAVING COUNT(DISTINCT EXTRACT(MONTH FROM event_date)) = 2
)

SELECT
    month,
    COUNT(user_id) AS monthly_active_users
FROM active_users_list
GROUP BY month;

