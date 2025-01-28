WITH user_count_list AS (
    SELECT
        COUNT(DISTINCT emails.user_id) AS total_users,
        COUNT(DISTINCT CASE
            WHEN texts.text_id IS NOT NULL
                AND signup_action = 'Confirmed'
            THEN emails.user_id
        END) AS confirmed_users
    FROM emails
    LEFT JOIN texts
        ON emails.email_id = texts.email_id
)

SELECT ROUND(confirmed_users::DECIMAL / total_users, 2) AS confirm_rate
FROM user_count_list;
