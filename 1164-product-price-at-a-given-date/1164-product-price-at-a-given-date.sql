WITH product_price_list AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS row_number
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT 
    DISTINCT Products.product_id,
    COALESCE(product_price_list.new_price, 10) AS price
FROM Products
LEFT JOIN product_price_list
    ON Products.product_id = product_price_list.product_id
WHERE COALESCE(product_price_list.row_number, 10) IN (1, 10);
