SELECT MIN(distance) AS shortest
FROM (
    SELECT x - LAG(x) OVER (ORDER BY x) AS distance
    FROM Point
);
