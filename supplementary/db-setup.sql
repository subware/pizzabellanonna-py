BEGIN TRANSACTION;
DROP TABLE IF EXISTS "diet";
CREATE TABLE IF NOT EXISTS "diet" (
	"id"	INTEGER UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "pizza";
CREATE TABLE IF NOT EXISTS "pizza" (
	"id"	INTEGER UNIQUE,
	"name"	TEXT,
	"cost"	REAL,
	"ingredients"	TEXT,
	"diet-id"	INTEGER,
	FOREIGN KEY("diet-id") REFERENCES "diet"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "diet" ("id","name") VALUES (1,'vegan'),
 (2,'vegetarisch'),
 (3,'omnivor'),
 (4,'frutarisch');
INSERT INTO "pizza" ("id","name","cost","ingredients","diet-id") VALUES (1,'Salami',6.5,'Salami',3),
 (2,'Hawaii',8.0,'Ananas, Hinterschinken, Käse',3),
 (3,'Margharita',8.0,'Mozzarella, frische Tomaten, frisches Basilikum',2),
 (4,'4-Jahreszeiten',8.0,'Salami, Hinterschinken, frische Champignons, Ei und Zwiebeln',3),
 (5,'Frutti di Mare',8.5,'Muscheln, Thunfisch, Sardellen und Calamares',3),
 (6,'Piccante',7.5,'Pepperoniwurst und grüne Pepperoni',3),
 (7,'Prosciutto',8.0,'Parmaschinken und Mozzarella',2),
 (8,'Julia',8.5,'Rucola, Ricotta, Kirschtomaten und Mozzarella',2),
 (9,'Romeo',8.5,'Rucola, Parmesankäse, Kirschtomaten und Mozzarella',2),
 (10,'Provence',7.5,'Frische Champignons und Knoblauchsoße',1),
 (11,'Spinaci',8.0,'Spinat, Mozzarella und frischer Knoblauch',2),
 (12,'Vegetaria',8.0,'Alte Socken, Mais, frische Champignons, Zwiebeln, Ananas (mit Käse überbacken)',2),
 (13,'Mykene',8.0,'Schafskäse, frische Champignons und Oliven',2),
 (14,'Spezial',8.5,'Paperoniwurst, Hinterschinken, Salami, frische Champignons und frische Paprika',3),
 (15,'Delphi',8.5,'Schafskäse, frischer Lauch, Speck, Ananas (mit Käse überbacken)',3),
 (16,'Curry',7.5,'Hähnchenbrustfilet, Currysoße',3),
 (17,'Salmone',9.5,'Lachsfilet, Mozzarella, frischer Lauch, rote Pfefferkörner und Créme fraîche',3),
 (18,'Al Capone',8.5,'Parmaschinken, Calamares, Mozzarella und Knoblauchsoße',3),
 (19,'Pepone',8.5,'Ruccola, Parmesankäse, getrocknete Tomaten, Mozzarella',2),
 (20,'Pizzabrot',3.0,NULL,1);
COMMIT;
