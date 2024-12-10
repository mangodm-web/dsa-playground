WITH transactions_order_list AS (
    SELECT
        *,
        ROW_NUMBER()
            OVER (PARTITION BY user_id ORDER BY transaction_date)
        AS row_num
    FROM transactions
)

SELECT
    user_id,
    spend,
    transaction_date
FROM transactions_order_list
WHERE row_num = 3;
