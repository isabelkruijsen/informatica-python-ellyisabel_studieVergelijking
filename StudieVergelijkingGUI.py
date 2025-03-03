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

# hij toont de studie stad en school in de listbox
def toonStudieSchoolStadInListbox():
    listboxStudieSchoolStad.delete(0, END)  # maak de listbox leeg
    studie_naam = ingevoerde_studieNaam.get()
    gevonden_Studies = StudieVergelijkingSQL.zoekStudiesInTabel(studie_naam)
    if gevonden_Studies:  # als er resultaten zijn
        listboxStudieSchoolStad.insert(END, "Studie - School - Stad")
        for studie, school, stad in gevonden_Studies:
            # Voeg de drie waarden samen in één string
            resultaat = f"{studie} - {school} - {stad}" # van internet kan dit?????
            listboxStudieSchoolStad.insert(END, resultaat)
    else:
        listboxStudieSchoolStad.insert(END, "Geen resultaten gevonden")

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
studieNaam.grid(row=1, column=0)

ingevoerde_studieNaam = StringVar()
invoerVeldStudieNaam = Entry(venster, textvariable= ingevoerde_studieNaam)
invoerVeldStudieNaam.grid(row=1, column=1, sticky="W")

#stadNaam = Label(venster, text="Stad:")
#stadNaam.grid(row=3, column=0)

# ingevoerde_stadNaam = StringVar ()   (VOOR UITBREIDING!!!!!!)
# invoerVeldStadNaam = Entry(venster, textvariable= ingevoerde_stadNaam)
# invoerVeldStadNaam.grid(row=3, column=1, sticky="W")

KnopZoekStudies = Button(venster, text="Zoek", width= 12, command= zoekStudies)
KnopZoekStudies.grid(row=1, column=3) # knop die gekoppeld is met def: zoekstudies


#listbox met studie stad en school
listboxStudieSchoolStad = Listbox(venster, height= 6, width= 50)
listboxStudieSchoolStad.grid(row=3, column=1, rowspan= 6, columnspan= 2, sticky= "W")
listboxStudieSchoolStad.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

#scroller bij de listbox
scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=3, column=2, rowspan=6, sticky="E")
listboxStudieSchoolStad.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxStudieSchoolStad.yview)






#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
