-- International Call Percentage
SELECT
    ROUND(
        100.0 * SUM(
            CASE 
                WHEN p1.country_id != p2.country_id THEN 1 
                ELSE 0 
            END
        ) / COUNT(*), 
        1
    ) AS international_calls_pct
FROM phone_calls
LEFT JOIN phone_info AS p1
    ON phone_calls.caller_id = p1.caller_id
LEFT JOIN phone_info AS p2
    ON phone_calls.receiver_id = p2.caller_id;
