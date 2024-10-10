SELECT *
FROM Users
WHERE name ~ '^[a-zA-Z][a-zA-Z0-9_.-]*'
  AND mail ~ '^[a-zA-Z0-9][a-zA-Z0-9_.-]*@leetcode\.com';
