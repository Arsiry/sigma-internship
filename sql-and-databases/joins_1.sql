-- SELECT orders.orderid, orders.orderdate, orders.totalamount, orders.customerid, customers.state
-- FROM orders
-- INNER JOIN customers ON orders.customerid = customers.customerid 
-- WHERE customers.state = 'OH' OR customers.state = 'NY' OR customers.state = 'OR';
--
SELECT p.prod_id, p.title, i.quan_in_stock, i.sales FROM products AS p 
INNER JOIN inventory AS i ON p.prod_id = i.prod_id;