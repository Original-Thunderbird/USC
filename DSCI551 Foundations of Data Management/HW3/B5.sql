SELECT drinker AS Drinker
FROM beerstables.Likes 
WHERE beer LIKE 'Bud' AND drinker NOT IN (
	SELECT drinker 
    FROM beerstables.Likes 
    WHERE beer LIKE 'Summerbrew'
);

/* Output
+----------+
| Drinker  |
+----------+
| Bill     |
| Cathay   |
| Jennifer |
+----------+
3 rows in set (0.00 sec)
*/