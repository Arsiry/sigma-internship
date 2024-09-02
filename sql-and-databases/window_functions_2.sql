SELECT 
DISTINCT r.id, r."name", 
         COUNT(t.id) OVER (
                     PARTITION BY r.id
                     ORDER BY r."name"
) AS "# of towns"
FROM regions AS r
JOIN departments AS d ON r.code = d.region 
JOIN towns AS t ON d.code = t.department
ORDER BY r.id;