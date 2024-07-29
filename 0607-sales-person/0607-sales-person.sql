SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    LEFT JOIN Company
        ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
);
