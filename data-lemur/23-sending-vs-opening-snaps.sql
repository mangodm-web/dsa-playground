WITH snap_stats_list AS (
    SELECT
        age_breakdown.age_bucket,
        SUM(activities.time_spent) FILTER (WHERE activities.activity_type = 'send') AS send_time_spent,
        SUM(activities.time_spent) FILTER (WHERE activities.activity_type = 'open') AS open_time_spent,
        SUM(activities.time_spent) AS total_time_spent
    FROM activities
    INNER JOIN age_breakdown
        ON activities.user_id = age_breakdown.user_id
    WHERE activities.activity_type IN ('send', 'open')
    GROUP BY age_breakdown.age_bucket
)

SELECT
    age_bucket,
    ROUND(send_time_spent / total_time_spent * 100.0, 2) AS send_perc,
    ROUND(open_time_spent / total_time_spent * 100.0, 2) AS open_perc
FROM snap_stats_list
ORDER BY age_bucket;
