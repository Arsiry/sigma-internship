-- SELECT e.emp_no, count(t.title) as "amount of titles"
-- FROM employees as e
-- JOIN titles as t USING(emp_no)
-- WHERE EXTRACT (YEAR FROM e.hire_date) > 1991
-- GROUP BY e.emp_no
-- HAVING count(t.title) > 2
-- ORDER BY e.emp_no;
-- 
-- SELECT e.emp_no, count(s.from_date) as "amount of raises"
-- FROM employees as e
-- JOIN salaries as s USING(emp_no)
-- JOIN dept_emp AS de USING(emp_no)
-- WHERE de.dept_no = 'd005'
-- GROUP BY e.emp_no
-- HAVING count(s.from_date) > 15
-- ORDER BY e.emp_no;
--
SELECT e.emp_no, count(de.dept_no) AS "worked for # departments"
FROM employees AS e
JOIN dept_emp AS de USING(emp_no)
GROUP BY e.emp_no
HAVING count(de.dept_no) > 1
ORDER BY e.emp_no;
