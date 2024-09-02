-- SELECT
--   DISTINCT continent,
--   SUM(population) OVER w1 as "continent population"
-- FROM country 
-- WINDOW w1 AS ( PARTITION BY continent );
--
--
SELECT
  DISTINCT continent,
  SUM(population) OVER w1 AS"continent population",
  CONCAT( 
      ROUND( 
          ( 
            SUM( population::float4 ) OVER w1 / 
            SUM( population::float4 ) OVER() 
          ) * 100    
      ),'%' ) AS "percentage of population"
FROM country 
WINDOW w1 AS( PARTITION BY continent );
