/*
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
*/

SELECT prod.name, prov.name
FROM providers prov
JOIN products prod
ON prod.id_providers = prov.id
WHERE prov.name = 'Ajax SA';