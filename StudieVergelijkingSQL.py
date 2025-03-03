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
    cursor = db.cursor() #cursor is object waarmee je data uit de database kan halen

    # Functie om de tabellen aan te maken
    def maakTabellenAan():
        # Tabel voor koppeling studie en school
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
                FOREIGN KEY (SchoolID) REFERENCES tbl_Scholen(SchoolID)
            );
        """)
        print("Tabel 'tbl_StudiePerSchool' aangemaakt.")

        # Tabel voor studies
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tbl_Studies(
                StudieID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Studienaam TEXT NOT NULL,
                Profiel TEXT
            );
        """)
        print("Tabel 'tbl_Studies' aangemaakt.")

        # Tabel voor scholen
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
                Huisnummer INTEGER
            );
        """)
        print("Tabel 'tbl_Scholen' aangemaakt.")

    # Functie om een studie toe te voegen en de gegenereerde ID terug te geven
    def voegStudieToe(nieuw_studienaam, nieuw_profiel):
        cursor.execute("""
            INSERT INTO tbl_Studies (Studienaam, Profiel)
            VALUES (?, ?)""", (nieuw_studienaam, nieuw_profiel))
        db.commit()
        print("Studie toegevoegd:", nieuw_studienaam)
        return cursor.lastrowid #geeft automatisch gegenererde sleutel van een ingevoegde rij MAG DIT???

    # Functie om een school toe te voegen en de gegenereerde ID terug te geven
    def voegSchoolToe(nieuw_schoolnaam, nieuw_duur_auto, nieuw_duur_OV, nieuw_OV_methode, nieuw_prijs_OV, nieuw_stad, nieuw_Postcode, nieuw_Huisnummer):
        cursor.execute("""
            INSERT INTO tbl_Scholen (Schoolnaam, Duur_Auto, Duur_OV, OV_Methode, Prijs_OV, Stad, Postcode, Huisnummer)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (nieuw_schoolnaam, nieuw_duur_auto, nieuw_duur_OV, nieuw_OV_methode, nieuw_prijs_OV, nieuw_stad, nieuw_Postcode, nieuw_Huisnummer))
        db.commit()
        print("School toegevoegd:", nieuw_schoolnaam)
        return cursor.lastrowid

    # Functie om een koppeling tussen studie en school toe te voegen
    def voegStudieperschoolToe(nieuw_schoolID, nieuw_studieID, nieuw_procentgeslaagd, nieuw_duur, nieuw_aantalstudenten, nieuw_studententevredenheid, nieuw_numerusfixus):
        cursor.execute("""
            INSERT INTO tbl_StudiePerSchool (SchoolID, StudieID, ProcentGeslaagd, Duur, AantalStudenten, Studententevredenheid, Numerusfixus)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (nieuw_schoolID, nieuw_studieID, nieuw_procentgeslaagd, nieuw_duur, nieuw_aantalstudenten, nieuw_studententevredenheid, nieuw_numerusfixus))
        db.commit()
        print("Studie per school toegevoegd.")
        return cursor.lastrowid

    # Functie om studies te zoeken met een gedeeltelijke match op de studienaam
    def zoekStudiesInTabel(ingevoerde_studieNaam):
        # Voeg joker toe zodat er gezocht wordt naar studie als er fout wordt getypt
        fout_getypt = "%" + ingevoerde_studieNaam + "%"  ### WERKT DIT??? biologiey herkent hij niet
        cursor.execute("""
            SELECT tbl_Studies.Studienaam, tbl_Scholen.Schoolnaam, tbl_Scholen.Stad
            FROM tbl_Studies
            JOIN tbl_StudiePerSchool ON tbl_Studies.StudieID = tbl_StudiePerSchool.StudieID
            JOIN tbl_Scholen ON tbl_StudiePerSchool.SchoolID = tbl_Scholen.SchoolID
            WHERE tbl_Studies.Studienaam LIKE ?
        """, (fout_getypt,))
        zoek_resultaat = cursor.fetchall()
        if not zoek_resultaat:
            print("Geen Studie gevonden met Studienaam:", ingevoerde_studieNaam)
        return zoek_resultaat

 
   # Functie om alle studies in tbl_Studies op te vragen (optioneel)
    def vraagOpGegevensStudiesTabel():
        cursor.execute("SELECT tbl_Studies.Studienaam, tbl_Scholen.Schoolnaam, tbl_Scholen.Stad FROM tbl_Studies JOIN tbl_StudiePerSchool ON tbl_Studies.StudieID = tbl_StudiePerSchool.StudieID JOIN tbl_Scholen ON tbl_StudiePerSchool.SchoolID = tbl_Scholen.SchoolID")
        resultaat = cursor.fetchall()
        print("Tabel tbl_Studies:", resultaat)
        return resultaat
    ### Hoofdprogramma

    maakTabellenAan()

    # Eerste studie: Biologie op RU
    studieID = voegStudieToe("Biologie", "N&G")
    schoolID = voegSchoolToe("RU", 8, 39, "bus-bus", 2.78, "Nijmegen", "6525 XZ", 4)
    voegStudieperschoolToe(schoolID, studieID, 71, 3, 200, 4.3, 250)

    # Tweede studie: economie op RU
    studieID2 = voegStudieToe("Economie", "E&M")
    voegStudieperschoolToe(schoolID, studieID2, 66, 3, 150, 3.9, 160)

    # Derde studie: geneeskunde op UU
    studieID3 = voegStudieToe("Geneeskunde", "N&G")
    schoolID2 = voegSchoolToe("UU", 64, 115, "bus-trein-tram", 17.30, "Utrecht", "3584 CS", 8)
    voegStudieperschoolToe(schoolID2, studieID3, 70, 4, 60, 4.6, 400)

    # Extra school toevoegen, TU/E
    voegSchoolToe("TU/E", 58, 114, "bus-trein-trein", 16.90, "Eindhoven", "5612 AZ", 3)

   # Optioneel: toon de inhoud van tbl_Studies
    vraagOpGegevensStudiesTabel()