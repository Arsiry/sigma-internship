SELECT emp_no, first_name, last_name
FROM employees
WHERE emp_no IN (
    SELECT emp_no
    FROM dept_emp
    WHERE dept_no = (
        SELECT dept_no 
        FROM dept_manager
        WHERE emp_no = 110183
    )
)
ORDER BY emp_no

-- Written with JOIN
-- SELECT e.emp_no, first_name, last_name
-- FROM employees as e
-- JOIN dept_emp as de USING (emp_no)
-- JOIN dept_manager as dm USING (dept_no)
-- WHERE dm.emp_no = 110183