# pizzabellanonna-py

Eine Demo-Webanwendung mit Python (Bottle) und Datenbank (SQLite). Es handelt sich um die Bestell-Webseite der fiktiven Pizzeria "*Bella Nonna*". Man kann alle verfügbaren Pizzen anzeigen, durchsuchen und jeweils eine einzelne Pizza zur Lieferung bestellen.

Über die Releases hinweg wird die Webanwendung iterativ entwickelt und es werden auch auch Themen wie Query String Injection sowie SQL Injections behandelt.


### Didaktische Überlegungen

Entwickelt für den Informatik-Grundkurs der Unterrichtsstufe Q2 an der [St. Ursula-Schule Geisenheim](https://st-ursula-schule.de/).

Dieses Projekt ist die Neuauflage von [https://github.com/digitalvolk/PizzaBellaNonna] mit Python und SQLite. Ziel war es, eine Umgebung zu schaffen, in der Schülerinnen und Schüler ohne Installation und Konfiguration von Web- und Datenbankservern direkt sichtbar Ergebnisse erzielen können. Das Python-Framework [Bottle](https://bottlepy.org/docs/dev/) bringt direkt einen Webserver mit und besteht nur aus einer Datei. [SQLite](https://www.sqlite.org/) als DBMS beschränkt sich ebenfalls auf eine Datei und ist bereits Bestandteil aktueller Python-Installationen ([sqlite3](https://docs.python.org/3/library/sqlite3.html)), ohne dass weitere Software installiert werden muss.


## Warning

This repository contains teaching material and is **not fit for production environments**! Especially, parts of this code are intentionally insecure or employ disencouraged programming techniques.
