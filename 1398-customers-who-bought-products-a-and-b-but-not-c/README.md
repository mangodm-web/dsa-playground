<h2><a href="https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c">1398. Customers Who Bought Products A and B but Not C</a></h2><h3>Medium</h3><hr><p>Table: <code>Customers</code></p>

<pre>
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id is the column with unique values for this table.
customer_name is the name of the customer.</pre>

<p>&nbsp;</p>

<p>Table: <code>Orders</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id is the column with unique values for this table.
customer_id is the id of the customer who bought the product &quot;product_name&quot;.
</pre>

<p>&nbsp;</p>

<p>Write a solution&nbsp;to report the customer_id and customer_name of customers who bought products <strong>&quot;A&quot;</strong>, <strong>&quot;B&quot;</strong> but did not buy the product <strong>&quot;C&quot;</strong> since we want to recommend them to purchase this product.</p>

<p>Return the result table <strong>ordered</strong> by <code>customer_id</code>.</p>

<p>The&nbsp;result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+
Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+
<strong>Output:</strong> 
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
<strong>Explanation:</strong> Only the customer_id with id 3 bought the product A and B but not the product C.
</pre>
