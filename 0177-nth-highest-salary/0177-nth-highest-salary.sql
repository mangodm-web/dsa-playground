CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT 
        DISTINCT temp.salary
    FROM (
    SELECT
        Employee.salary,
        DENSE_RANK() OVER (ORDER BY Employee.salary DESC) AS salary_rank
    FROM Employee ) AS temp
    WHERE salary_rank = N
  );
END;
$$ LANGUAGE plpgsql;