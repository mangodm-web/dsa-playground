SELECT
    Players.player_id,
    Players.player_name,
    COUNT(*) AS grand_slams_count
FROM (
    SELECT Wimbledon AS player_id
    FROM Championships
    UNION ALL
    SELECT Fr_open AS player_id
    FROM Championships
    UNION ALL
    SELECT US_open AS player_id
    FROM Championships
    UNION ALL
    SELECT Au_open AS player_id
    FROM Championships
) AS tmp
LEFT JOIN Players
    ON tmp.player_id = Players.player_id
GROUP BY
    Players.player_id,
    Players.player_name;
