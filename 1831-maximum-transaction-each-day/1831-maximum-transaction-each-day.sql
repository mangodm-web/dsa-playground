SELECT transaction_id
FROM Transactions
WHERE (DATE(day), amount) IN (
    SELECT
        DATE(day) AS transaction_date,
        MAX(amount) AS max_amount
    FROM Transactions
    GROUP BY DATE(day)
)
ORDER BY transaction_id;
