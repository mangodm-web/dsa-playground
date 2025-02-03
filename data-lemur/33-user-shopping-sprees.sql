SELECT DISTINCT t1.user_id
FROM transactions AS t1
INNER JOIN transactions AS t2
  ON DATE(t2.transaction_date) = DATE(t1.transaction_date) + 1
INNER JOIN transactions AS t3
  ON DATE(t3.transaction_date) = DATE(t1.transaction_date) + 2
ORDER BY t1.user_id;
