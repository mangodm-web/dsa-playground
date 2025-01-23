WITH product_spend_rank_list AS (
    SELECT
        category,
        product,
        SUM(spend) AS total_spend,
        RANK() OVER (
            PARTITION BY category
            ORDER BY SUM(spend) DESC
        ) AS total_spend_ranking
      FROM product_spend
      WHERE DATE_PART('year', transaction_date) = 2022
      GROUP BY category, product
)

SELECT
    category,
    product,
    total_spend
FROM product_spend_rank_list
WHERE total_spend_ranking <= 2
ORDER BY category, total_spend_ranking;
