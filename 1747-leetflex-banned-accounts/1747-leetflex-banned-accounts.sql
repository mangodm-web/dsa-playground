SELECT DISTINCT l1.account_id
FROM loginfo AS l1
LEFT JOIN loginfo AS l2
    ON
        l1.account_id = l2.account_id
        AND l1.ip_address != l2.ip_address
WHERE l1.login BETWEEN l2.login AND l2.logout;
