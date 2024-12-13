-- 총 매출이 가장 많은 사용자 10명
SELECT
    usc.userId,
    SUM(st.amount) AS total_sales
FROM user_session_channel AS usc
LEFT JOIN session_timestamp AS sts
    ON usc.sessionId = sts.sessionId
LEFT JOIN session_transaction AS st
    ON sts.sessionId = st.sessionId
GROUP BY usc.userId
ORDER BY total_sales DESC
LIMIT 10;

-- 월별 채널별 매출과 방문자 정보
SELECT
    DATE_FORMAT(sts.ts, 'yyyy-MM') AS month,
    usc.channel,
    SUM(st.amount) AS gross_revenue,
    SUM(CASE WHEN st.refunded THEN 0 ELSE st.amount END) AS net_revenue,
    COUNT(DISTINCT usc.userId) AS unique_users,
    COUNT(DISTINCT CASE WHEN st.amount > 0 THEN usc.userId END) AS paid_users,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN st.amount > 0 THEN usc.userId END) /
        NULLIF(COUNT(DISTINCT usc.userId), 0),
        2
    ) AS conversion_rate
FROM user_session_channel AS usc
LEFT JOIN session_timestamp AS sts
    ON usc.sessionId = sts.sessionId
LEFT JOIN session_transaction AS st
    ON sts.sessionId = st.sessionId
GROUP BY
    month,
    channel;

-- 사용자별 처음, 마지막 방문 채널 조회
SELECT DISTINCT 
    usc.userId,
    FIRST_VALUE(usc.channel) OVER (
        PARTITION BY usc.userId 
        ORDER BY sts.ts ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_channel,
    LAST_VALUE(usc.channel) OVER (
        PARTITION BY usc.userId 
        ORDER BY sts.ts ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_channel
FROM user_session_channel AS usc
LEFT JOIN session_timestamp AS sts
    ON usc.sessionId = sts.sessionId;
