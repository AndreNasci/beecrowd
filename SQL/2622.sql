/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT name
FROM costumers 
WHERE id IN (
    SELECT id_customers
    FROM legal_person
);