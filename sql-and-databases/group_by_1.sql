-- SELECT hire_date, COUNT(emp_no) as "amount"
-- FROM employees
-- GROUP BY hire_date
-- ORDER BY "amount" DESC;
---
-- SELECT e.emp_no, count(t.title) as "amount of titles"
-- FROM employees as e
-- JOIN titles as t USING(emp_no)
-- WHERE EXTRACT (YEAR FROM e.hire_date) > 1991
-- GROUP BY e.emp_no
-- ORDER BY e.emp_no;
-- 
SELECT e.emp_no, de.from_date, de.to_date
FROM employees AS e
JOIN dept_emp AS de USING(emp_no)
WHERE de.dept_no = 'd005'
GROUP BY e.emp_no, de.from_date, de.to_date
ORDER BY e.emp_no, de.to_date;