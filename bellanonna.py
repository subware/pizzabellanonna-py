from bottle import route, run, static_file
from pathlib import Path

# diese Funktion wird aufgerufen, wenn jemand die Startseite besucht
# also ... http://localhost in die Adresszeile eingibt.
@route("/")
def index():
    # lese Template-Datei ein
    template = Path("menu_template.html").read_text(encoding = "utf-8")
    return template


# liefere statische Dateien direkt aus (nur CSS und Hintergrundbild)
@route("/<filename:re:styles\.css|hintergrund\.jpg>")
def styles(filename):
    return static_file(filename, "")


run(host = "localhost", port = 80)