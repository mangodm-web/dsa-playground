WITH measurements_with_rn_list AS (
    SELECT
        measurement_time::DATE AS measurement_day,
        measurement_value,
        ROW_NUMBER() OVER (
            PARTITION BY measurement_time::DATE
            ORDER BY measurement_time
        ) AS rn
    FROM measurements
)

SELECT
    measurement_day,
    SUM(measurement_value) FILTER (WHERE rn % 2 = 1) AS odd_sum,
    SUM(measurement_value) FILTER (WHERE rn % 2 = 0) AS even_sum
FROM measurements_with_rn_list
GROUP BY measurement_day
ORDER BY measurement_day;
