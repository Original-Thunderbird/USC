SELECT manufacturer AS Manufacturer, AVG(price) AS Average 
FROM beerstables.Beers2Bars 
GROUP BY manufacturer;

/* Output
+----------------+--------------------+
| Manufacturer   | Average            |
+----------------+--------------------+
| Anheuser-Busch | 2.4444444444444446 |
| Pete's         | 3.6666666666666665 |
| Heineken       |                  2 |
+----------------+--------------------+
3 rows in set (0.01 sec)
*/