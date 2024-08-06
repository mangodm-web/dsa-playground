WITH match_result_list AS (
    SELECT
        host_team AS team_id,
        CASE
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS num_points
    FROM Matches
    UNION ALL
    SELECT
        guest_team AS team_id,
        CASE
            WHEN host_goals < guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS num_points
    FROM Matches    
)

SELECT
    Teams.team_id,
    Teams.team_name,
    COALESCE(SUM(num_points), 0) AS num_points
FROM Teams
LEFT JOIN match_result_list
    ON Teams.team_id = match_result_list.team_id
GROUP BY
    Teams.team_id,
    Teams.team_name
ORDER BY 
    COALESCE(SUM(num_points), 0) DESC,
    Teams.team_id;
