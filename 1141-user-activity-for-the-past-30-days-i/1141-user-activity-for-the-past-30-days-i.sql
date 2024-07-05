SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date <= '2019-07-27'
  AND activity_date >= '2019-07-27'::date - INTERVAL '29 day'
GROUP BY activity_date;
