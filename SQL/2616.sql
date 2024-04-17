/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT id, name
FROM customers
WHERE id NOT IN (
    SELECT id_customers
    FROM locations
);