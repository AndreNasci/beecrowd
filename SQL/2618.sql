/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT prod.name, prov.name, cat.name
FROM products prod
JOIN providers prov 
ON prod.id_providers = prov.id
JOIN categories cat
ON cat.id = prod.id_categories
WHERE prov.name = 'Sansul SA' 
AND cat.name = 'Imported';