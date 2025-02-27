# Vul hier de naam van je programma in:
# studie vergelijkingen
#
# Vul hier jullie namen in:
#
#Elly en Isabel
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("studies.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------
# def maakTabellenAan():
#  # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS tbl_StudiePerSchool(
#             StudiePerSchoolID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             SchoolID  NOT NULL,
#             StudieID REAL NOT NULL);""")
#     print("Tabel 'tbl_pizzas' aangemaakt.")


### --------- Hoofdprogramma  ---------------

