SELECT DISTINCT s.bar AS Bar 
FROM beerstables.Sells AS s 
	JOIN (
		SELECT MAX(price) as maxPrice 
		FROM beerstables.Sells
	) inn 
	ON s.price = inn.maxPrice;
    
/* Output
+------------+
| Bar        |
+------------+
| Joe's bar  |
| Mary's bar |
+------------+
2 rows in set (0.00 sec)
*/