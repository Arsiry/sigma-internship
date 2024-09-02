SELECT countrycode, district, "name",
  MAX(population) OVER w1 AS "max population",
  LAST_VALUE("name") OVER w1
FROM city 
WINDOW w1 AS( PARTITION BY countrycode, district ORDER BY "name" ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING);
