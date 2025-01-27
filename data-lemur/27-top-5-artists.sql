WITH top_5_ranked_artist_list AS (
    SELECT
        artists.artist_name,
        DENSE_RANK() OVER (
            ORDER BY COUNT(songs.song_id) DESC
        ) AS artist_rank
    FROM global_song_rank
    INNER JOIN songs
        ON global_song_rank.song_id = songs.song_id
    INNER JOIN artists
        ON songs.artist_id = artists.artist_id
    WHERE global_song_rank.rank <= 10
    GROUP BY artists.artist_name
)

SELECT
    artist_name,
    artist_rank
FROM top_5_ranked_artist_list
WHERE artist_rank <= 5
ORDER BY artist_rank;
