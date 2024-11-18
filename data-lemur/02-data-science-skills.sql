/*
  Data Science Skills(LinkedIn)
  Given a table of candidates and their skills,
  write a query to list the candidates who possess
  all of the required skills(proficient in Python, Tableau, and PostgreSQL).
  Sort the output by candidate ID in ascending order.
*/
WITH required_skills_list AS (
    SELECT 'Python' AS skill
    UNION
    SELECT 'Tableau' AS skill
    UNION
    SELECT 'PostgreSQL' AS skill
)

SELECT candidates.candidate_id
FROM candidates
INNER JOIN required_skills_list
    ON candidates.skill = required_skills_list.skill
GROUP BY candidates.candidate_id
HAVING
    COUNT(DISTINCT candidates.skill)
    = (SELECT COUNT(*) FROM required_skills_list)
ORDER BY candidates.candidate_id;
