SELECT 
    id,
    CASE
      WHEN p_id IS NULL THEN 'Root' 
      WHEN NOT EXISTS (SELECT 1
                       FROM Tree AS t2
                       WHERE t1.id = t2.p_id) THEN 'Leaf'
      ELSE 'Inner'
    END AS type
FROM Tree AS t1;
