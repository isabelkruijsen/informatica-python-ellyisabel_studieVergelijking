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
def maakTabellenAan():
 # Maak een nieuwe tabel met 8 kolommen: studie per school id, school id, studie id, procentgeslaagd, duur, aantalstudenten, studententeverdenheid,numerusfixus
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_StudiePerSchool(
            StudiePerSchoolID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            SchoolID  INTEGER NOT NULL ,
            StudieID INTEGER NOT NULL,
            ProcentGeslaagd INTEGER,
            Duur INTEGER NOT NULL,
            AantalStudenten INTEGER, 
            Studententevredenheid REAL,
            Numerusfixus INTEGER,      
            FOREIGN KEY (StudieID) REFERENCES tbl_Studies(StudieID),
            FOREIGN KEY (SchoolID) REFERENCES tbl_Scholen(SchoolID) );""")
    print("Tabel 'tbl_Studieperschool' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_Studies(
            StudieID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Studienaam TEXT NOT NULL,
            Profiel TEXT );""")
    print("Tabel 'tbl_studie' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_Scholen(
            SchoolID INTEGER PRIMARY KEY AUTOINCREMENT,
            Schoolnaam TEXT NOT NULL,
            Duur_Auto INTEGER,
            Duur_OV INTEGER,
            OV_Methode TEXT,
            Prijs_OV REAL
            Stad TEXT,
            Huisnummer INTEGER );""")
    print("Tabel 'tbl_winkelWagen' aangemaakt.")



### --------- Hoofdprogramma  ---------------

maakTabellenAan()