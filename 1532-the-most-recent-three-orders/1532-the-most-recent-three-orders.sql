WITH customer_order_list AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM Orders
)

SELECT
    Customers.name AS customer_name,
    Customers.customer_id,
    customer_order_list.order_id,
    customer_order_list.order_date
FROM customer_order_list
LEFT JOIN Customers
    ON customer_order_list.customer_id = Customers.customer_id
WHERE customer_order_list.rn <= 3
ORDER BY
    Customers.name ASC,
    Customers.customer_id ASC,
    customer_order_list.order_date DESC;
