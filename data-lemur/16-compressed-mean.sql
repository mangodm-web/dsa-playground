SELECT
    ROUND(
        (SUM(item_count * order_occurrences) / SUM(order_occurrences))::numeric,
        1
    ) AS mean
FROM items_per_order;
