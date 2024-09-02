SELECT prod_id, title, price, NULLIF(special, 0) AS "special"
FROM products