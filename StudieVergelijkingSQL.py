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
    #studies per school aangemaakt
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
#tabel studies aangemaakt
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_Studies(
            StudieID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Studienaam TEXT NOT NULL,
            Profiel TEXT );""")
    print("Tabel 'tbl_Studies' aangemaakt.")
#tabel scholen aanmaken
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
#nieuwe studie per school toevoegen
def voegStudieperschoolToe(nieuw_schoolID, nieuw_studieID, nieuw_procentgeslaagd, nieuw_duur, nieuw_aantalstudenten, nieuw_studententevredenheid, nieuw_numerusfixus):
    cursor.execute("INSERT INTO tbl_StudiePerSchool (SchoolID, StudieID, ProcentGeslaagd, Duur, AantalStudenten, Studententevredenheid, Numerusfixus) VALUES(?, ?, ?, ?, ?, ?, ?)", 
                   (nieuw_schoolID, nieuw_studieID, nieuw_procentgeslaagd, nieuw_duur, nieuw_aantalstudenten, nieuw_studententevredenheid, nieuw_numerusfixus))
    db.commit()
    print("Studie per school toegevoegd.")
#nieuwe studie toevoegen
def voegStudieToe(nieuw_studienaam, nieuw_profiel):
    cursor.execute("INSERT INTO tbl_Studies (Studienaam, Profiel) VALUES(?, ?)", 
                   (nieuw_studienaam, nieuw_profiel))
    db.commit()
    print("Studie toegevoegd.")
#nieuwe school toevoegen
def voegSchoolToe(nieuw_schoolnaam, nieuw_duur_auto, nieuw_duur_OV, nieuw_OV_methode, nieuw_prijs_OV, nieuw_stad, nieuw_Postcode, nieuw_Huisnummer):
    cursor.execute("INSERT INTO tbl_Scholen (Schoolnaam, Duur_Auto, Duur_OV, OV_Methode, Prijs_OV, Stad, Postcode, Huisnummer) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
                   (nieuw_schoolnaam, nieuw_duur_auto, nieuw_duur_OV, nieuw_OV_methode, nieuw_prijs_OV, nieuw_stad, nieuw_Postcode, nieuw_Huisnummer))
    db.commit()
    print("School toegevoegd.")
#hij zoekt studies in tabel en als hij gevonden is dat plakt hij met left join gelijk de school en stad er bij aan
def zoekStudiesInTabel(ingevoerde_studieNaam):
    cursor.execute("""
        SELECT tbl_Studies.Studienaam, tbl_Scholen.Schoolnaam, tbl_Scholen.Stad 
        FROM tbl_Studies
        JOIN tbl_StudiePerSchool ON tbl_Studies.StudieID = tbl_StudiePerSchool.StudieID
        JOIN tbl_Scholen ON tbl_StudiePerSchool.SchoolID = tbl_Scholen.SchoolID
        WHERE tbl_Studies.Studienaam LIKE ?""", (ingevoerde_studieNaam, ))
    zoek_resultaat = cursor.fetchall()
    if zoek_resultaat == []: #resultaat is leeg, geen studie gevonden
        print("Geen Studie gevonden met Studienaam:", ingevoerde_studieNaam)
    return zoek_resultaat

def vraagOpGegevensStudiesTabel():
    cursor.execute("SELECT * FROM tbl_Studies")
    resultaat = cursor.fetchall()
    print("Tabel tbl_Studies:", resultaat)
    return resultaat
### --------- Hoofdprogramma  ---------------
maakTabellenAan()

# eerste studie toevoegen, biologie op het RU
voegStudieToe("Biologie", "N&G")
voegSchoolToe("RU", 8, 39, "bus-bus", 2.78, "Nijmegen", "6525 XZ", 4)
voegStudieperschoolToe(21, 1, 71, 3, 200, 4.3, 250)

# tweede studie, economie in RU
voegStudieToe("Economie", "E&M")
voegStudieperschoolToe(21, 2, 66, 3, 150, 3.9, 160)

#derde studie, geneeskunde UU
voegStudieToe("Geneeskunde", "N&G")
voegSchoolToe("UU", 64, 115, "bus-trein-tram", 17.30, "Utrecht", "3584 CS", 8)
voegStudieperschoolToe(22, 3, 70, 4, 60, 4.6, 400)

#schooltoevoegen
voegSchoolToe("TU/E", 58, 114, "bus-trein-trein", 16.90, "Eindhoven", "5612 AZ", 3)