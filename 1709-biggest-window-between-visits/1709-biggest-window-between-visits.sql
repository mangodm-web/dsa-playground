WITH user_visit_list AS (
    SELECT
        *,
        visit_date
        - LAG(visit_date)
            OVER (PARTITION BY user_id ORDER BY visit_date)
        AS visit_window
    FROM (
        SELECT *
        FROM uservisits
        UNION
        SELECT DISTINCT
            user_id,
            DATE('2021-01-01') AS visit_date
        FROM uservisits
    )
)

SELECT
    user_id,
    MAX(visit_window) AS biggest_window
FROM user_visit_list
GROUP BY user_id
ORDER BY user_id;
