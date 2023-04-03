SELECT DISTINCT e.first_name, e.last_name, inn.title 
FROM employees.employees as e JOIN (
	SELECT emp_no, title 
    FROM employees.titles 
	WHERE from_date = '2000-03-23' 
		AND title LIKE '%engineer%') inn
ON e.emp_no = inn.emp_no;

/* Output
+------------+---------------+-----------------+
| first_name | last_name     | title           |
+------------+---------------+-----------------+
| Nahla      | Silva         | Engineer        |
| Uli        | Lichtner      | Senior Engineer |
| Matk       | Schlegelmilch | Senior Engineer |
| Mayuko     | Luff          | Engineer        |
| Masami     | Panienski     | Senior Engineer |
| Tzvetan    | Brodie        | Senior Engineer |
| Kerhong    | Pappas        | Senior Engineer |
| Xiaoshan   | Keirsey       | Senior Engineer |
| Jiakeng    | Baaleh        | Senior Engineer |
| Fox        | Begiun        | Senior Engineer |
+------------+---------------+-----------------+
10 rows in set (0.16 sec)
*/