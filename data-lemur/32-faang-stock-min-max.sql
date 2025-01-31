WITH stock_agg_list AS (
    SELECT
        ticker,
        MIN(open) AS lowest_open,
        MAX(open) AS highest_open
    FROM stock_prices
    GROUP BY ticker
)

SELECT
    sa.ticker,
    TO_CHAR(s1.date, 'Mon-yyyy') AS highest_mth,
    sa.highest_open,
    TO_CHAR(s2.date, 'Mon-yyyy') AS lowest_mth,
    sa.lowest_open
FROM stock_agg_list AS sa
LEFT JOIN stock_prices AS s1
    ON sa.highest_open = s1.open
LEFT JOIN stock_prices AS s2
    ON sa.lowest_open = s2.open
ORDER BY sa.ticker;
