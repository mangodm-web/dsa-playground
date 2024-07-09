DELETE FROM Person
WHERE (id, email) NOT IN (
    SELECT 
        MIN(id) AS id,
        email
    FROM Person
    GROUP BY email
);
