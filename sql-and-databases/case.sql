SELECT prod_id, title, price, 
    CASE   
      WHEN  price > 20 THEN 'expensive'
      WHEN  price <= 10 THEN  'cheap'
      WHEN  price BETWEEN 10 AND 20  THEN 'average'
    END AS "price class"
FROM products