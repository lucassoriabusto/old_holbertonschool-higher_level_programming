--
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre_name
FROM tv_shows
LEFT JOIN show_genres ON tv_shows.id = show_genres.show_id
LEFT JOIN tv_genres ON show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre_name ASC;
