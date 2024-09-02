-- Show TIMEZONE;
-- Select AGE(date '1982-03-26')
-- SELECT *, DATE_TRUNC('month', orderdate) FRom orders;
SELECT COUNT(orderid)
FROM orders
WHERE DATE_TRUNC('month', orderdate) = date '2004-01-01';