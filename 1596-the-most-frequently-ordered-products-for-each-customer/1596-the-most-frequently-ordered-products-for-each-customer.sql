WITH order_rank_list AS (
    SELECT
        Orders.customer_id,
        Orders.product_id,
        Products.product_name,
        RANK() OVER (PARTITION BY Orders.customer_id ORDER BY COUNT(*) DESC) AS order_rank
    FROM Orders
    LEFT JOIN Products
        ON Orders.product_id = Products.product_id
    GROUP BY
        Orders.customer_id,
        Orders.product_id,
        Products.product_name
)

SELECT
    customer_id,
    product_id,
    product_name
FROM order_rank_list
WHERE order_rank = 1;
