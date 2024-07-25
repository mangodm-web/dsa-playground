WITH call_list AS (
  SELECT
      caller_id AS person_id,
      duration
  FROM Calls
  UNION ALL
  SELECT
      callee_id AS person_id,
      duration
  FROM Calls
)

SELECT
    Country.name AS country
FROM call_list
LEFT JOIN Person
    ON call_list.person_id = Person.id
LEFT JOIN Country
    ON SUBSTRING(Person.phone_number, 1, 3) = Country.country_code
GROUP BY Country.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM call_list);
