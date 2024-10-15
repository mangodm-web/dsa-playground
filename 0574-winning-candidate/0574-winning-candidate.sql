SELECT name
FROM Candidate
WHERE id IN (
    SELECT candidateId
    FROM Vote
    GROUP BY candidateId
    ORDER BY COUNT(id) DESC
    LIMIT 1
);
