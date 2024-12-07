WITH duplicate_companies_list AS (
    SELECT
        company_id,
        title,
        description
    FROM job_listings
    GROUP BY
        company_id,
        title,
        description
    HAVING COUNT(*) >= 2
)

SELECT COUNT(DISTINCT company_id) AS duplicate_companies
FROM duplicate_companies_list;
