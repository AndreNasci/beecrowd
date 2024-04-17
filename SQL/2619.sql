/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT prod.name, prov.name, prod.price
FROM products prod
JOIN providers prov
ON prod.id_providers = prov.id
JOIN categories cat
ON cat.id = prod.id_categories
WHERE prod.price > 1000.0
AND cat.name = 'Super Luxury';