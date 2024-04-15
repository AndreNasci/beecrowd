/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT m.id, m.name
FROM movies m
JOIN genres g
ON m.id_genres = g.id
WHERE g.description = 'Action';