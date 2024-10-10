SELECT
    Products.product_name,
    SUM(Orders.unit) AS unit
FROM Orders
INNER JOIN Products
    ON Orders.product_id = Products.product_id
WHERE SUBSTRING(Orders.order_date::TEXT, 1, 7) = '2020-02'
GROUP BY 
    Products.product_name
HAVING SUM(Orders.unit) >= 100;
