/*
  Valid only under the condition that exactly one customer has placed more orders than any other customer.
*/
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
