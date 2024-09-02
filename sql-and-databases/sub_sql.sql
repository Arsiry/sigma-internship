SELECT city.countrycode, city.district, "name", max_population
FROM city
INNER JOIN
(SELECT countrycode, district, max(population) AS max_population
FROM city
GROUP BY countrycode, district) AS city_group 
ON city.countrycode=city_group.countrycode AND city.district=city_group.district AND city.population=city_group.max_population
ORDER BY city.countrycode, city.district, "name"
