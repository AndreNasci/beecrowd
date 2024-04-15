/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT p.id, p.name 
FROM products p
JOIN categories c
ON p.id_categories = c.id
WHERE c.name LIKE 'super%';