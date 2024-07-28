WITH order_list AS (
  SELECT
      Products.product_name,
      Products.product_id,
      Orders.order_id,
      Orders.order_date,
      DENSE_RANK() OVER (PARTITION BY Orders.product_id ORDER BY Orders.order_date DESC) AS rn
  FROM Orders
  LEFT JOIN Products
      ON Orders.product_id = Products.product_id
)

SELECT
    product_name,
    product_id,
    order_id,
    order_date
FROM order_list
WHERE rn = 1
ORDER BY
    product_name,
    product_id,
    order_id;
