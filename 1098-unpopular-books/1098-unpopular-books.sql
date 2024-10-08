WITH temp AS (
    SELECT '2019-06-23'::DATE AS today
)

SELECT
    book_id,
    name
FROM Books
WHERE available_from <= (
        SELECT today - INTERVAL '1 month'
        FROM temp
    )
    AND book_id NOT IN (
        SELECT book_id
        FROM Orders
        WHERE dispatch_date BETWEEN (SELECT today - INTERVAL '1 year' FROM temp) AND (SELECT today FROM temp)
        GROUP BY book_id
        HAVING SUM(quantity) >= 10
    );
