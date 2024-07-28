SELECT
    Department.name AS Department,
    Employee.name AS Employee,
    Employee.salary AS Salary
FROM Employee
LEFT JOIN Department
    ON Employee.departmentId = Department.id
WHERE (Employee.salary, Employee.departmentId) IN (
  SELECT
      MAX(salary),
      departmentId
  FROM Employee
  GROUP BY departmentId
);
