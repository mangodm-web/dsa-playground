WITH consecutive_seat_list AS (
    SELECT
        c1.seat_id AS seat1,
        c2.seat_id AS seat2
    FROM Cinema AS c1
    LEFT JOIN Cinema AS c2
        ON c1.seat_id + 1 = c2.seat_id
    WHERE c1.free + c2.free = 2
)
(
    SELECT seat1 AS seat_id
    FROM consecutive_seat_list
    UNION
    SELECT seat2 AS seat_id
    FROM consecutive_seat_list
)
ORDER BY seat_id;
