/*
  Histogram of Tweets(Twitter)
  Given a table Twitter tweet data,
  write a query to obtain a histogram of tweets posted per user in 2022.
  Group the users by the number of tweets they posted in 2022,
  and count the number of users in each group.
*/
WITH tweet_bucket_list AS (
    SELECT
        user_id,
        COUNT(tweet_id) AS tweet_bucket
    FROM tweets
    WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
    GROUP BY user_id
)

SELECT
    tweet_bucket,
    COUNT(user_id) AS users_num
FROM tweet_bucket_list
GROUP BY tweet_bucket
ORDER BY tweet_bucket;
