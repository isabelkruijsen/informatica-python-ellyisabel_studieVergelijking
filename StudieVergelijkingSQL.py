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
    cursor = db.cursor()

### ---------  Functie definities  -----------------
def maakTabellenAan():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_StudiePerSchool(
            StudiePerSchoolID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            SchoolID INTEGER NOT NULL,
            StudieID INTEGER NOT NULL,
            ProcentGeslaagd INTEGER,
            Duur INTEGER NOT NULL,
            AantalStudenten INTEGER, 
            Studententevredenheid REAL,
            Numerusfixus INTEGER,      
            FOREIGN KEY (StudieID) REFERENCES tbl_Studies(StudieID),
            FOREIGN KEY (SchoolID) REFERENCES tbl_Scholen(SchoolID) );""")
    print("Tabel 'tbl_StudiePerSchool' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_Studies(
            StudieID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Studienaam TEXT NOT NULL,
            Profiel TEXT );""")
    print("Tabel 'tbl_Studies' aangemaakt.")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_Scholen(
            SchoolID INTEGER PRIMARY KEY AUTOINCREMENT,
            Schoolnaam TEXT NOT NULL,
            Duur_Auto INTEGER,
            Duur_OV INTEGER,
            OV_Methode TEXT,
            Prijs_OV REAL,
            Stad TEXT,
            Postcode TEXT,
            Huisnummer INTEGER );""")
    print("Tabel 'tbl_Scholen' aangemaakt.")

def voegStudieperschoolToe(nieuw_schoolID, nieuw_studieID, nieuw_procentgeslaagd, nieuw_duur, nieuw_aantalstudenten, nieuw_studententevredenheid, nieuw_numerusfixus):
    cursor.execute("INSERT INTO tbl_StudiePerSchool (SchoolID, StudieID, ProcentGeslaagd, Duur, AantalStudenten, Studententevredenheid, Numerusfixus) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                   (nieuw_schoolID, nieuw_studieID, nieuw_procentgeslaagd, nieuw_duur, nieuw_aantalstudenten, nieuw_studententevredenheid, nieuw_numerusfixus))
    db.commit()
    print("Studie per school toegevoegd.")

def voegStudieToe(nieuw_studienaam, nieuw_profiel):
    cursor.execute("INSERT INTO tbl_Studies (Studienaam, Profiel) VALUES(?, ?)", 
                   (nieuw_studienaam, nieuw_profiel))
    db.commit()
    print("Studie toegevoegd.")

def voegSchoolToe(nieuw_schoolnaam, nieuw_duur_auto, nieuw_duur_OV, nieuw_OV_methode, nieuw_prijs_OV, nieuw_stad, nieuw_Postcode, nieuw_Huisnummer):
    cursor.execute("INSERT INTO tbl_Scholen (Schoolnaam, Duur_Auto, Duur_OV, OV_Methode, Prijs_OV, Stad, Postcode, Huisnummer) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
                   (nieuw_schoolnaam, nieuw_duur_auto, nieuw_duur_OV, nieuw_OV_methode, nieuw_prijs_OV, nieuw_stad, nieuw_Postcode, nieuw_Huisnummer))
    db.commit()
    print("School toegevoegd.")

### --------- Hoofdprogramma  ---------------
maakTabellenAan()

# eerste studie toevoegen, biologie op het RU
voegStudieperschoolToe(21, 1, 71, 3, 200, 4.3, 250)
voegStudieToe("Biologie", "N&G")
voegSchoolToe("RU", 8, 39, "bus-bus", 2.78, "Nijmegen", "6525 XZ", 4)
# tweede studie, economie in utrecht

#derde studie, geneeskunde TU/E