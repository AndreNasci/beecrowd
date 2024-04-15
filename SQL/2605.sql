/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT prod.name, prov.name 
FROM products prod 
JOIN providers prov 
ON prod.id_providers = prov.id
WHERE prod.id_categories = 6;