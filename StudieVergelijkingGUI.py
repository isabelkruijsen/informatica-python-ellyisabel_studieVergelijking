# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#Studie vergelijkingen
#
# Vul hier jullie namen in:
#Elly en Isabel
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import StudieVergelijkingSQL

def zoekStudies():
    zoekstudie = zoek_studieNaam.get() 
    gevonden_Studies = StudieVergelijkingSQL.zoekStudiesInTabel(zoekstudie)
    print("Gevonden studies:", gevonden_Studies)
    toonStudieSchoolStadInListbox(gevonden_Studies)


def toonStudieSchoolStadInListbox(resultaten):
    listboxStudieSchoolStad.delete(0, END)
    if resultaten:
        listboxStudieSchoolStad.insert(END, "Studie - School - Stad")
        for studie, school, stad in resultaten:
            resultaat = studie, school, stad 
            listboxStudieSchoolStad.insert(END, resultaat)
    else:
        listboxStudieSchoolStad.insert(END, "Geen resultaten gevonden")

def toonAlleStudieInListbox():
    listboxStudieSchoolStad.delete(0, END) #maak de listbox leeg
    resultaten = StudieVergelijkingSQL.vraagOpGegevensStudiesTabel()
    for studie in resultaten:
        resultaat = studie 
        listboxStudieSchoolStad.insert(END, resultaat)
    listboxStudieSchoolStad.insert(0, "studie - school - stad")

def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxStudieSchoolStad.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxStudieSchoolStad.get(geselecteerdeRegelInLijst) 
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerVeldStudieNaam.delete(0, END) 
    #zet tekst in veld
    invoerVeldStudieNaam.insert(0, geselecteerdeTekst)



## -----------HOOFDPROGRAMMA---------------- ##
venster = Tk()
venster.iconbitmap("MC_icon.ico")  # op een Mac uitcommentariëren
venster.wm_title("StudieVergelijking")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

# Hier maken we twee aparte variabelen aan:
zoek_studieNaam = StringVar()   # voor de zoekterm (studienaam)
resultaatVar = StringVar()       # voor het tonen van de schoolnaam

# Invoerveld voor het zoekcriterium (studienaam)
invoerVeldStudieNaam = Label(venster, text="Zoek Studie:")
invoerVeldStudieNaam.grid(row=1, column=0, sticky="W")

invoerVeldZoekStudie = Entry(venster, textvariable=zoek_studieNaam)
invoerVeldZoekStudie.grid(row=1, column=1, sticky="W")

KnopZoekStudies = Button(venster, text="Zoek", width=12, command=zoekStudies)
KnopZoekStudies.grid(row=1, column=3)


listboxStudieSchoolStad = Listbox(venster, height=6, width=50)
listboxStudieSchoolStad.grid(row=3, column=1, rowspan=6, columnspan=2, sticky="W")
listboxStudieSchoolStad.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)


# # Invoerveld voor het tonen van het resultaat (schoolnaam)  UITBREIDING!!!!!!!
# schoollabel = Label(venster, text="School:")
# schoollabel.grid(row=2, column=0, sticky="W")

# schoolinvoer = Entry(venster, textvariable=resultaatVar)
# schoolinvoer.grid(row=2, column=1, sticky="W")

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=3, column=2, rowspan=6, sticky="E")
listboxStudieSchoolStad.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxStudieSchoolStad.yview)

knopToonstudies = Button(venster, text="Toon alle studies", width=12, command=toonAlleStudieInListbox)
knopToonstudies.grid(row=4, column=3)

labelGeselecteerdeStudie = Label(venster, text="Geselecteerde studie:")
labelGeselecteerdeStudie.grid(row = 10, column= 0, sticky= "W")

ingevoerde_geselecteerdeStudie = StringVar()
invoerveldGeselecteerdeStudie = Entry(venster, textvariable= invoerVeldStudieNaam)
invoerveldGeselecteerdeStudie.grid(row=10, column= 1, sticky= "W")





knopSluit = Button(venster, text= "Sluiten", width= 12, command= venster.destroy)
knopSluit.grid(row= 17, column= 4)

venster.mainloop()