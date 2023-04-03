SELECT manf AS Manufacturer 
FROM beerstables.Beers 
GROUP BY manf 
HAVING COUNT(DISTINCT NAME) >= 3;

/* Output
+----------------+
| Manufacturer   |
+----------------+
| 555            |
| Anheuser-Busch |
+----------------+
2 rows in set (0.00 sec)
*/