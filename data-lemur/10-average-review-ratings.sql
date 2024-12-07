SELECT
    product_id AS product,
    EXTRACT(MONTH FROM submit_date) AS mth,
    ROUND(AVG(stars), 2) AS avg_stars
FROM reviews
GROUP BY
    mth,
    product
ORDER BY
    mth,
    product;
