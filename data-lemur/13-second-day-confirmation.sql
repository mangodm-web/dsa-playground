SELECT emails.user_id
FROM emails
INNER JOIN texts
    ON
        emails.email_id = texts.email_id
        AND texts.signup_action = 'Confirmed'
        AND emails.signup_date + interval '1 day' = texts.action_date;
