SELECT
    Orders.Customer_id,
    Customers.Customer_name
FROM Orders
LEFT JOIN Customers
    ON Orders.Customer_id = Customers.Customer_id
GROUP BY
    Orders.Customer_id,
    Customers.Customer_name
HAVING
    ARRAY_AGG(Orders.Product_name)::TEXT LIKE '%A,B%'
    AND ARRAY_AGG(Orders.Product_name)::TEXT NOT LIKE '%C%'
ORDER BY Orders.Customer_id;
