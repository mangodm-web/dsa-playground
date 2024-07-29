SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE page_id NOT IN (
    SELECT page_id
    FROM Likes
    WHERE user_id = 1
) AND user_id IN (
    SELECT
        CASE
          WHEN user1_id = 1 THEN user2_id
          ELSE user1_id
        END
    FROM Friendship
    WHERE user1_id = 1 OR user2_id = 1  
);
