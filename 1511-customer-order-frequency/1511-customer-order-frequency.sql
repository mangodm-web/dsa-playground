SELECT
    customer_id,
    name
FROM (
    SELECT
        Orders.customer_id,
        Customers.name,
        TO_CHAR(Orders.order_date, 'YYYY-MM') AS ym,
        SUM(Orders.quantity * Product.price) AS total_spent
    FROM Orders
    LEFT JOIN Product
        ON Orders.product_id = Product.product_id
    LEFT JOIN Customers
        ON Orders.customer_id = Customers.customer_id
    WHERE
        Orders.order_date >= '2020-06-01'
        AND Orders.order_date < '2020-08-01'
    GROUP BY
        Orders.customer_id,
        Customers.name,
        TO_CHAR(Orders.order_date, 'YYYY-MM')
    HAVING SUM(Orders.quantity * Product.price) >= 100
) AS filtered_order_list
GROUP BY
    customer_id,
    name
HAVING COUNT(*) >= 2;
