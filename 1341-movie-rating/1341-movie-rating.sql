(SELECT Users.name AS results
FROM MovieRating
INNER JOIN Users
    ON MovieRating.user_id = Users.user_id
GROUP BY MovieRating.user_id
ORDER BY COUNT(MovieRating.movie_id) DESC, Users.name
LIMIT 1)
UNION
(
SELECT Movies.title AS results
FROM MovieRating
INNER JOIN Movies
    ON MovieRating.movie_id = Movies.movie_id
WHERE LEFT(MovieRating.created_at, 7) = '2020-02'
GROUP BY MovieRating.movie_id
ORDER BY AVG(MovieRating.rating) DESC, Movies.title
LIMIT 1
);