SELECT COUNT(policy_holder_id) AS policy_holder_count
FROM (
    SELECT policy_holder_id
    FROM callers
    GROUP BY policy_holder_id
    HAVING COUNT(DISTINCT case_id) >= 3
) AS filtered_policy_holder_ids;
