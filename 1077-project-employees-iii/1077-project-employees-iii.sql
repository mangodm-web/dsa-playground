WITH project_list AS (
  SELECT
      Project.project_id,
      Project.employee_id,
      DENSE_RANK() OVER (PARTITION BY Project.project_id ORDER BY Employee.experience_years DESC) AS rn
  FROM Project
  LEFT JOIN Employee
      ON Project.employee_id = Employee.employee_id
)

SELECT 
    project_id,
    employee_id
FROM project_list
WHERE rn = 1;
