WITH point_pairs_list AS (
    SELECT SQRT(POWER((p1.x - p2.x), 2) + POWER((p1.y - p2.y), 2)) AS distance
    FROM Point2D p1
    CROSS JOIN Point2D p2
    WHERE p1.x != p2.x OR p1.y != p2.y
)

SELECT MIN(ROUND(distance::numeric, 2)) AS shortest
FROM point_pairs_list;
