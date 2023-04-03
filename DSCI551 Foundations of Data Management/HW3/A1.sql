SELECT emp_no
FROM employees.employees 
WHERE first_name LIKE '%mary%' 
	AND last_name LIKE '%o_';
    
/* Output
+--------+
| emp_no |
+--------+
|  16021 |
|  21756 |
|  52983 |
|  73998 |
|  78783 |
|  88698 |
| 101753 |
| 216534 |
| 263268 |
| 410311 |
| 423386 |
| 459548 |
| 491899 |
+--------+
13 rows in set (0.13 sec)
*/