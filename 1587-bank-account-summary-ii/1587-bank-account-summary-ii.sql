/*
  문제에 주어진 조건("There will be no two users having the same name in the table.")을 활용한 풀이
*/
SELECT
    Users.name,
    SUM(Transactions.amount) AS balance
FROM Transactions
LEFT JOIN Users
    ON Transactions.account = Users.account
GROUP BY Users.name
HAVING SUM(Transactions.amount) > 10000;
