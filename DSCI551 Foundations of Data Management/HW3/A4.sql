SELECT DISTINCT d.dept_no as dept_no 
FROM employees.dept_manager d JOIN (
	SELECT dept_no, COUNT(DISTINCT emp_no) AS mngrs 
    FROM employees.dept_manager 
    GROUP BY dept_no
) cnt 
ON d.dept_no = cnt.dept_no 
WHERE cnt.mngrs >= 3;

/* Output
+---------+
| dept_no |
+---------+
| d004    |
| d006    |
| d009    |
+---------+
3 rows in set (0.00 sec)
*/