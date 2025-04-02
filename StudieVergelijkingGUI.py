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
from PIL import ImageTk, Image

fotoPad= ""

## voor de functie voor het zoeken van een ingevoerde studie
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

## voor het tonen van alle studies in de listbox
def toonAlleStudieInListbox():
    listboxStudieSchoolStad.delete(0, END) #maakt de listbox leeg
    resultaten = StudieVergelijkingSQL.vraagOpGegevensStudiesTabel()
    for studie in resultaten:
        resultaat = studie 
        listboxStudieSchoolStad.insert(END, resultaat)
    listboxStudieSchoolStad.insert(0, "studie - school - stad")

# studie info tonen
def geefstudieinfo():
    listboxstudieinfo.delete(0, END) #maakt de listbox leeg
    geselecteerde_regel = listboxStudieSchoolStad.curselection() # Haalt de geselecteerde studie op uit de listbox
    if not geselecteerde_regel:  #als er geen studie in de vorige listbox geselecteerd is
        listboxstudieinfo.insert(END, "Geen studie geselecteerd!")
        return  
    geselecteerde_tekst = listboxStudieSchoolStad.get(geselecteerde_regel[0])  # De studienaam staat op de eerste positie
    studienaam1 = geselecteerde_tekst[0] 
    resultatenstudieinfo = StudieVergelijkingSQL.vraagOpGegevensstudieinfo(studienaam1) # Haalt studie-info op basis van de studienaam
    listboxstudieinfo.insert(END, "Procent Geslaagd - Duur - Aantal Studenten - Tevredenheid - Numerus Fixus")
    for resultaat in resultatenstudieinfo:
        listboxstudieinfo.insert(END, resultaat)


# reis info tonen
def geefreisinfo():
    listboxreisinfo.delete(0, END) #maakt de listbox leeg
    geselecteerde_regel = listboxStudieSchoolStad.curselection()     # Haalt de geselecteerde studie op uit de listbox
    if not geselecteerde_regel:  #als er geen studie in de vorige listbox geselecteerd is
        listboxreisinfo.insert(END, "Geen studie geselecteerd!")
        return  
    geselecteerde_tekst = listboxStudieSchoolStad.get(geselecteerde_regel[0]) # De schoolnaam staat op de eerste positie
    print(geselecteerde_tekst)
    Schoolnaam = geselecteerde_tekst[1] # Haalt studie-info op basis van de schoolnaam
    print(Schoolnaam)
    resultatenreisinfo = StudieVergelijkingSQL.vraagOpGegevensreisinfo(Schoolnaam)
    listboxreisinfo.insert(END, "duur met auto-duur met OV-OV methode-prijs OV-Stad-postcode-huisnummer ")
    for resultaat in resultatenreisinfo:
        listboxreisinfo.insert(END, resultaat)
        print(resultaat)

#voor het weergeven plaatjes van geselcteerde school
def haalGeselecteerdeRijOp(event):
    geselecteerdeRegelInLijst = listboxStudieSchoolStad.curselection()[0] #bepaal op welke regel er geklikt is
    geselecteerdeTekst = listboxStudieSchoolStad.get(geselecteerdeRegelInLijst)     #haal tekst uit die regel
    invoerVeldZoekStudie.delete(0, END)      #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerVeldZoekStudie.insert(0, geselecteerdeTekst)     #zet tekst in veld

    regel = listboxStudieSchoolStad.get(geselecteerdeRegelInLijst)
    print("regel:" , regel)
    global fotoPad
    Schoolnaam= regel[1]
    print('schoolnaam;', Schoolnaam)
    if Schoolnaam == 'RU':
        fotoPad = "radboudlogo.png"
        nieuwPhotoPad = PhotoImage(file=fotoPad)
        fotoSchool.configure(image=nieuwPhotoPad)
        fotoSchool.image = nieuwPhotoPad
    elif Schoolnaam == 'TU/E':
        fotoPad = "tuelogo.png"
        nieuwPhotoPad = PhotoImage(file=fotoPad)
        fotoSchool.configure(image=nieuwPhotoPad)
        fotoSchool.image = nieuwPhotoPad
    elif Schoolnaam == "UU":
        fotoPad = "utrechtlogo.png"
        nieuwPhotoPad = PhotoImage(file=fotoPad)
        fotoSchool.configure(image=nieuwPhotoPad)
        fotoSchool.image = nieuwPhotoPad

# voor ophalen studieinfo
def haalGeselecteerdeRijOpstudieinfo(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxstudieinfo.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxstudieinfo.get(geselecteerdeRegelInLijst) 
    #zet tekst in veld
    listboxstudieinfo.insert(0, geselecteerdeTekst)

# voor ophalen reisinfo
def haalGeselecteerdeRijOpreisinfo(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxreisinfo.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxreisinfo.get(geselecteerdeRegelInLijst) 
    #zet tekst in veld
    listboxreisinfo.insert(0, geselecteerdeTekst)



## -----------HOOFDPROGRAMMA---------------- ##
venster = Tk()
venster.iconbitmap("studie_logo.ico")  
venster.wm_title("StudieVergelijking")
venster.config(bg= "#C1CFD6") # wij hebben de kleuren van ons logo opgezocht en deze als kleur van de achtergrond en kleur van knopjes genomen


iconimg = ImageTk.PhotoImage(Image.open("studie_logo.ico")) 
venster.iconphoto(False, iconimg)

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

KnopZoekStudies = Button(venster, text="Zoek", width=12, bg= "#1E73BE", fg="snow" ,command=zoekStudies)
KnopZoekStudies.grid(row=1, column=3)


listboxStudieSchoolStad = Listbox(venster, height=6, width=50)
listboxStudieSchoolStad.grid(row=3, column=1, rowspan=6, columnspan=2, sticky="W")
listboxStudieSchoolStad.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=3, column=2, rowspan=6, sticky="E")
listboxStudieSchoolStad.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxStudieSchoolStad.yview)


knopToonstudies = Button(venster, text="Toon alle studies", width=12 , bg= "#1E73BE", fg="snow", command=toonAlleStudieInListbox)
knopToonstudies.grid(row=4, column=3)

labelGeselecteerdeStudie = Label(venster, text="Geselecteerde studie:")
labelGeselecteerdeStudie.grid(row = 10, column= 0, sticky= "W")

# logo scholen in pagina zetten
padFotoGeselecteerdeSchool = PhotoImage(file=fotoPad)
fotoSchool = Label(venster, width=100, height=100, bg="#C1CFD6", image=padFotoGeselecteerdeSchool)
fotoSchool.grid(row=13, column=3) 

ingevoerde_geselecteerdeStudie = StringVar()
invoerveldGeselecteerdeStudie = Entry(venster, textvariable= zoek_studieNaam ) 
invoerveldGeselecteerdeStudie.grid(row=10, column= 1, sticky= "W")

#studie informatie knop en listbox
knopstudieinfo = Button(venster, text="Geef studie info", width=12 , bg= "#1E73BE", fg="snow", command= geefstudieinfo)
knopstudieinfo.grid(row=12, column=1)

listboxstudieinfo = Listbox(venster, height=6, width=50)
listboxstudieinfo.grid(row=13, column=1, rowspan=6, columnspan=2, sticky="W")
listboxstudieinfo.bind('<<ListboxSelect>>', haalGeselecteerdeRijOpstudieinfo)

#reisinfo
knopreisinfo = Button(venster, text="Geef reisinfo", width=12 , bg= "#1E73BE", fg="snow", command= geefreisinfo)
knopreisinfo.grid(row=24, column=1)

listboxreisinfo = Listbox(venster, height=6, width=50)
listboxreisinfo.grid(row=26, column=1, rowspan=6, columnspan=2, sticky="W")
listboxreisinfo.bind('<<ListboxSelect>>', haalGeselecteerdeRijOpreisinfo)

knopSluit = Button(venster, text= "Sluiten", width= 12 , bg= "#1E73BE", fg="snow", command= venster.destroy)
knopSluit.grid(row= 29, column= 4)

venster.mainloop()