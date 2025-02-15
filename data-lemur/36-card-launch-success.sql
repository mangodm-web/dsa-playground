WITH card_launch_list AS (
    SELECT
        card_name,
        issued_amount,
        RANK() OVER (
            PARTITION BY card_name
            ORDER BY
                issue_year,
                issue_month
        ) AS launch_rank
    FROM
    monthly_cards_issued
)

SELECT
    card_name,
    issued_amount
FROM card_launch_list
WHERE launch_rank = 1
ORDER BY issued_amount DESC;
