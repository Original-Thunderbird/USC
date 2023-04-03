SELECT e.first_name, e.last_name
FROM employees.employees AS e 
	JOIN (
		SELECT emp_no, MAX(salary) AS peak 
		FROM employees.salaries 
		GROUP BY emp_no 
			HAVING peak > 150000
	) inn 
    ON e.emp_no = inn.emp_no;

/* Output
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Tokuyasu   | Pesch     |
| Ibibia     | Junet     |
| Xiahua     | Whitcomb  |
| Lansing    | Kambil    |
| Willard    | Baca      |
| Tsutomu    | Alameldin |
| Charmane   | Griswold  |
| Weicheng   | Hatcliff  |
| Mitsuyuki  | Stanfel   |
| Sanjai     | Luders    |
| Honesty    | Mukaidono |
| Weijing    | Chenoweth |
| Shin       | Birdsall  |
| Mohammed   | Moehrke   |
| Lidong     | Meriste   |
+------------+-----------+
15 rows in set (1.99 sec)
*/