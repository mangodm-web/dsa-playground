SELECT
    Trips.request_at AS "Day",
    ROUND(
        1.0 * SUM(
            CASE
                WHEN Trips.status = 'completed' THEN 0
                ELSE 1
            END
        ) / COUNT(Trips.id),
        2
    ) AS "Cancellation Rate"
FROM Trips
JOIN Users AS u1
    ON Trips.client_id = u1.users_id
JOIN Users AS u2
    ON Trips.driver_id = u2.users_id
WHERE Trips.request_at >= '2013-10-01'
  AND Trips.request_at <= '2013-10-03'
  AND u1.role = 'client'
  AND u2.role = 'driver'
  AND u1.banned = 'No'
  AND u2.banned = 'No'
GROUP BY Trips.request_at;
