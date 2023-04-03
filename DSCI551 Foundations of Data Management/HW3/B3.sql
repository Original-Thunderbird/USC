SELECT ba.name AS Bar, COALESCE(inn.total, 0) AS Total 
FROM beerstables.Bars AS ba 
	LEFT JOIN (
		SELECT bar, COUNT(price) AS total 
        FROM beerstables.Sells 
        WHERE price >= 2 GROUP BY bar
	) inn 
    ON ba.name = inn.bar;
    
/* Output
+--------------+-------+
| Bar          | Total |
+--------------+-------+
| Bob's bar    |     2 |
| Darwin's bar |     0 |
| Haal's bar   |     0 |
| Joe's bar    |     4 |
| Mary's bar   |     4 |
+--------------+-------+
5 rows in set (0.00 sec)
*/