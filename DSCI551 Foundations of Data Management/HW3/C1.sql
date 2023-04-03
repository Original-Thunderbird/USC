DROP VIEW IF EXISTS beerstables.Beers2Bars;
CREATE VIEW beerstables.Beers2Bars AS
SELECT be.manf AS manufacturer, se.beer, se.bar, se.price 
FROM beerstables.Beers AS be, beerstables.Sells AS se 
WHERE se.beer = be.name;

/* Output
Query OK, 0 rows affected (0.02 sec)
Query OK, 0 rows affected (0.00 sec)
*/