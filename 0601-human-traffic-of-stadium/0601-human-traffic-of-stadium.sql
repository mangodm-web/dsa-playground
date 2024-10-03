WITH visit_records_list AS (
    SELECT
        *,
        id - ROW_NUMBER() OVER (ORDER BY id) AS visit_group
    FROM Stadium
    WHERE people >= 100
)

SELECT
    id,
    visit_date,
    people
FROM visit_records_list
WHERE visit_group IN (
    SELECT visit_group
    FROM visit_records_list
    GROUP BY visit_group
    HAVING COUNT(visit_group) >= 3
);
