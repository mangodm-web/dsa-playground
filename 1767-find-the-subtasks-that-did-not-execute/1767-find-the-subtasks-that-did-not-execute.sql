WITH subtask_list AS (
  SELECT
      task_id,
      GENERATE_SERIES(1, subtasks_count) AS subtask_id
  FROM Tasks
)

SELECT *
FROM subtask_list
WHERE (task_id, subtask_id) NOT IN (
  SELECT *
  FROM Executed
);
