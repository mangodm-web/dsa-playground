SELECT customer_id
FROM customer_contracts
INNER JOIN products
    ON customer_contracts.product_id = products.product_id
GROUP BY customer_id
HAVING COUNT(DISTINCT products.product_category) = (
           SELECT COUNT(DISTINCT product_category)
           FROM products
       );
