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


### ---------  Functie definities  -----------------
def zoekStudies():
    studie_naam = ingevoerde_studieNaam.get() 
    gevonden_Studies = StudieVergelijkingSQL.zoekStudiesInTabel(studie_naam)
    print("gevonden studies", gevonden_Studies)
    invoerVeldStudieNaam.delete(0, END) #invoerveld voor naam leeg maken
    for rij in gevonden_Studies: #voor elke rij dat de query oplevert
         #toon studienaam, de tweede kolom uit het resultaat in de invoerveld
        invoerVeldStudieNaam.insert(END, rij[1])
    toonStudieSchoolStadInListbox()

def toonStudieSchoolStadInListbox():
    listboxStudieSchoolStad.delete(0, END) #maak de listbox leeg
    Studie_tabel = StudieVergelijkingSQL.vraagOpGegevensStudiesTabel()
    for regel in Studie_tabel:
        listboxStudieSchoolStad.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu
    listboxStudieSchoolStad.insert(0, "school studie stad")

### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxStudieSchoolStad.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxStudieSchoolStad.get(geselecteerdeRegelInLijst) 
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerVeldStudieNaam.delete(0, END) 
    #zet tekst in veld
    invoerVeldStudieNaam.insert(0, geselecteerdeTekst)


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("StudieVergelijking")

labelIntro = Label(venster, text="Welkom!")
#Vul hieronder een of meerdere zoektermen in, vervolgens zul je alle opties met jouw ingevulde eisen zien. Als je een studie selecteert, kun je vervolgens meer studie info of reisinformatie opvragen.
labelIntro.grid(row=0, column=0, sticky="W")

# schoolNaam = Label(venster, text="School:")
# schoolNaam.grid(row=1, column=0)

# ingevoerde_schoolNaam = StringVar () (VOOR UITBREIDING!!!!!!)
# invoerVeldSchoolNaam = Entry(venster, textvariable= ingevoerde_schoolNaam)
# invoerVeldSchoolNaam.grid(row=1, column=1, sticky="W")

studieNaam = Label(venster, text="Studie:")
studieNaam.grid(row=2, column=0)

ingevoerde_studieNaam = StringVar()
invoerVeldStudieNaam = Entry(venster, textvariable= ingevoerde_studieNaam)
invoerVeldStudieNaam.grid(row=2, column=1, sticky="W")

#stadNaam = Label(venster, text="Stad:")
#stadNaam.grid(row=3, column=0)

# ingevoerde_stadNaam = StringVar ()   (VOOR UITBREIDING!!!!!!)
# invoerVeldStadNaam = Entry(venster, textvariable= ingevoerde_stadNaam)
# invoerVeldStadNaam.grid(row=3, column=1, sticky="W")

KnopZoekStudies = Button(venster, text="Zoek", width= 12, command= zoekStudies)
KnopZoekStudies.grid(row=1, column=3) ## gekoppeld worden met defenitie 'zoekStudies'!!!!!!!!



listboxStudieSchoolStad = Listbox(venster, height= 6, width= 50)
listboxStudieSchoolStad.grid(row=4, column=0, rowspan= 6, columnspan= 2, sticky= "W")
listboxStudieSchoolStad.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=4, column=2, rowspan=6, sticky="E")
listboxStudieSchoolStad.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxStudieSchoolStad.yview)






#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
