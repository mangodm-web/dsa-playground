WITH temp AS (
    SELECT '2019-06-23'::DATE AS today
)

SELECT
    book_id,
    name
FROM
    Books
WHERE
    available_from <= (
        SELECT today - INTERVAL '1 month'
        FROM temp
    )
    AND book_id NOT IN (
        SELECT book_id
        FROM Orders
        JOIN temp
          ON Orders.dispatch_date >= temp.today - INTERVAL '1 year'
         AND Orders.dispatch_date <= temp.today
        GROUP BY book_id
        HAVING SUM(quantity) >= 10
    );
