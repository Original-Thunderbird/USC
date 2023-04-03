SELECT name as Drinker 
FROM beerstables.Drinkers 
WHERE name NOT IN (
	SELECT drinker 
    FROM beerstables.Frequents
);

/* Output
+---------+
| Drinker |
+---------+
| Cathay  |
| Mahaan  |
+---------+
2 rows in set (0.01 sec)
*/