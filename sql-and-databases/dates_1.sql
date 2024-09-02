-- SELECT *, AGE(birth_date) FROM employees
-- WHERE EXTRACT(YEAR FROM AGE(birth_date)) > 60;
SELECT COUNT(*) FROM employees
-- WHERE EXTRACT(MONTH FROM hire_date) = 2;
WHERE EXTRACT(MONTH FROM birth_date) = 11;
-- SELECT MAX(AGE(birth_date)) FROM employees;
