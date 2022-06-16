from bottle import route, run, static_file, request, abort
from pathlib import Path
import sqlite3


# diese Funktion wird aufgerufen, wenn jemand die Startseite besucht
# also ... http://localhost in die Adresszeile eingibt.
@route("/")
def index():
    # Prüfen, ob eine Suche angefordert wurde, oder ob alle Pizzen angezeigt werden sollen
    if request.query.search != "":
        sql_statement = "SELECT pizza.name, pizza.ingredients, diet.name, pizza.cost, pizza.id FROM pizza LEFT JOIN diet ON pizza.'diet-id' = diet.id WHERE pizza.name LIKE :search;"
        sql_parameters = {"search": "%" + request.query.search + "%"}
    else:
        sql_statement = "SELECT pizza.name, pizza.ingredients, diet.name, pizza.cost, pizza.id FROM pizza LEFT JOIN diet ON pizza.'diet-id' = diet.id;"
        sql_parameters = {}
    
    # lese Template-Datei für die Speisekarte ein
    template = Path("menu_template.html").read_text(encoding = "utf-8")
    
    db_connection = create_db_connection()
    cursor = db_connection.cursor()
    
    cursor.execute(sql_statement, sql_parameters) # Schutz vor SQL Injection durch "parametrisierte Query", d.h. das DBMS escaped alle Eingabezeichen korrekt.
    #dbms_execute(cursor, db_connection, sql_statement)
    
    results = cursor.fetchall()
    
    
    tabelle = "" # in dieser Variablen bauen wir das HTML für unsere Tabelle auf
    for pizza in results:
        tabelle = tabelle + "<tr>"
        tabelle = tabelle + "<td>" + str(pizza[0]) + "</td>"
        
        # Falls eine Pizza keine Zutaten hat, soll nicht "None" auf der Webseite erscheinen
        if pizza[1] == None:
            tabelle = tabelle + "<td></td>"
        else:
            tabelle = tabelle + "<td>" + str(pizza[1]) + "</td>"
            
        # Manche Leute können mit dem Begriff "onmivor" nichts anfangen, also lassen wir den Fall weg (das ist "normales Essen")
        if str(pizza[2]) == "omnivor":
            tabelle = tabelle + "<td></td>"
        else:
            tabelle = tabelle + "<td>" + str(pizza[2]) + "</td>"
        
        # Der Preis soll "hübsch" formatiert sein (z.B. "8,00 €" statt "8.0")
        tabelle = tabelle + "<td>" + format_cost(pizza[3]) + "</td>"
        
        # Hier kommt der Link zum Bestellen, übertragen wird nur die id der bestellten Pizza
        tabelle = tabelle + "<td><a href=\"order.html?pizzaid=" + str(pizza[4]) + "\">bestellen</a></td>"
        
        tabelle = tabelle + "</tr>"
    
    template = template.replace("$TABELLE", tabelle) # ersetze den Platzhalter im HTML durch unsere Tabelle
    return template


# die Bestellseite
@route("/order.html")
def order():
    # Welche Parameter wurden an unsere Webseite übergeben? (Das Zeug hinter dem "?" in der URL.)
    pizza_id = int(request.query.pizzaid)
    
    # Daten zur bestellten Pizza aus Datenbank holen
    db_connection = create_db_connection()
    cursor = db_connection.cursor()
    sql_statement = "SELECT name, cost FROM pizza WHERE id = " + str(pizza_id) + ";"
    cursor.execute(sql_statement)
    results = cursor.fetchall()
    
    if len(results) > 0:
        pizza_name = results[0][0] # Aus dem ersten Ergebnis wollen wir den ersten Wert -> der Name der Pizza
        pizza_cost = results[0][1] # Aus dem ersten Ergebnis wollen wir den zweiten Wert -> der Preis
    else:
        # Hier sollte eine Fehlerbehandlung stattfinden ;)
        pizza_name = "zufällige Pizza"
        pizza_cost = 42
    
    # lese Template-Datei für Bestellungen ein
    template = Path("order_template.html").read_text(encoding = "utf-8")
    template = template.replace("$PIZZA", pizza_name)
    template = template.replace("$PREIS", format_cost(pizza_cost))

    return template


# liefere statische Dateien direkt aus (nur CSS und Hintergrundbild)
@route("/<filename:re:styles\.css|hintergrund\.jpg>")
def styles(filename):
    return static_file(filename, "")


# Hilfsfunktionen
def create_db_connection():
    connection = sqlite3.connect("pizzas.sqlite")
    return connection


def format_cost(cost):
    vor_komma = int(cost) # alle Nachkommastellen abschneiden
    nach_komma = int((cost - vor_komma) * 100) # zwei Nachkommastellen vor das Komma ziehen, Rest abschneiden
    
    if nach_komma < 10: # es gab nur eine Nachkommastelle oder nur die 0, also noch eine "0" anhängen
        nach_komma = str(nach_komma) + "0"
        
    return str(vor_komma) + "," + str(nach_komma) + " €"


# Diese Methode simuliert das Verhalten anderer DBMS (SQLite kann nicht mehrere Befehle in einem execute() ausführen!)
def dbms_execute(cursor, dbcon, sql):
    print("\n" + sql + "\n")
    cursor.executescript(sql)
    dbcon.commit()
    
    # cleanup query (remove all but first SQL statement)
    # sql = sql.split(";", 1)[0]
    
    # bei einer SQL Injection mit mehreren Befehlen wird hier ein Fehler auftreten:
    try:
        cursor.execute(sql)
    except:
        abort(500)
        



run(host = "localhost", port = 80)