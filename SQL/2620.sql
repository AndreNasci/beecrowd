/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT c.name, o.id
FROM customers c
JOIN orders o
ON c.id = o.id_customers
WHERE o.orders_date < '2016-07-01';