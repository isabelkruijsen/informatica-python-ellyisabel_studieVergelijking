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

# studie info tonen

def geefstudieinfo():
    listboxstudieinfo.delete(0, END) #maak de listbox leeg
    # Haal de geselecteerde studie op uit de listbox
    geselecteerde_regel = listboxStudieSchoolStad.curselection()
    if not geselecteerde_regel:  #als er geen studie in de vorige listbox geselecteerd is
        listboxstudieinfo.insert(END, "Geen studie geselecteerd!")
        return  
    geselecteerde_tekst = listboxStudieSchoolStad.get(geselecteerde_regel[0])
    # De studienaam staat op de eerste positie
    studienaam1 = geselecteerde_tekst[0] 
     # Haal studie-info op basis van de studienaam
    resultatenstudieinfo = StudieVergelijkingSQL.vraagOpGegevensstudieinfo(studienaam1)
    listboxstudieinfo.insert(END, "Procent Geslaagd - Duur - Aantal Studenten - Tevredenheid - Numerus Fixus")
    for resultaat in resultatenstudieinfo:
        listboxstudieinfo.insert(END, resultaat)


# voor reis info

def geefreisinfo():
    listboxreisinfo.delete(0, END) #maak de listbox leeg
    # Haal de geselecteerde studie op uit de listbox
    geselecteerde_regel = listboxStudieSchoolStad.curselection()
    if not geselecteerde_regel:  #als er geen studie in de vorige listbox geselecteerd is
        listboxreisinfo.insert(END, "Geen studie geselecteerd!")
        return  
    geselecteerde_tekst = listboxStudieSchoolStad.get(geselecteerde_regel[0])
    print(geselecteerde_tekst)
    # De schoolnaam staat op de eerste positie
    Schoolnaam = geselecteerde_tekst[1] 
     # Haal studie-info op basis van de schoolnaam
    print(Schoolnaam)
    resultatenreisinfo = StudieVergelijkingSQL.vraagOpGegevensreisinfo(Schoolnaam)
    listboxreisinfo.insert(END, "duur met auto-duur met OV-OV methode-prijs OV-Stad-postcode-huisnummer ")
    for resultaat in resultatenreisinfo:
        listboxreisinfo.insert(END, resultaat)
        print(resultaat)

#voor studie school stad
def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxStudieSchoolStad.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxStudieSchoolStad.get(geselecteerdeRegelInLijst) 
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerVeldZoekStudie.delete(0, END) 
    #zet tekst in veld
    invoerVeldZoekStudie.insert(0, geselecteerdeTekst)

    regel = listboxStudieSchoolStad.get(geselecteerdeRegelInLijst)
    print("regel:" , regel)
    global fotoPad
    Schoolnaam= regel[1]
    print('schoolnaam;', Schoolnaam)
    if Schoolnaam == 'RU':
        print("hallo")
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



# voor studieinfo

def haalGeselecteerdeRijOpstudieinfo(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxstudieinfo.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxstudieinfo.get(geselecteerdeRegelInLijst) 
    #zet tekst in veld
    listboxstudieinfo.insert(0, geselecteerdeTekst)

# voor reisinfo
def haalGeselecteerdeRijOpreisinfo(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxreisinfo.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxreisinfo.get(geselecteerdeRegelInLijst) 
    #zet tekst in veld
    listboxreisinfo.insert(0, geselecteerdeTekst)



## -----------HOOFDPROGRAMMA---------------- ##
venster = Tk()
venster.iconbitmap("studie_logo.ico")  # op een Mac uitcommentariëren
venster.wm_title("StudieVergelijking")
venster.config(bg= "silver")


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

KnopZoekStudies = Button(venster, text="Zoek", width=12, bg= "midnightblue", fg="snow" ,command=zoekStudies)
KnopZoekStudies.grid(row=1, column=3)


listboxStudieSchoolStad = Listbox(venster, height=6, width=50)
listboxStudieSchoolStad.grid(row=3, column=1, rowspan=6, columnspan=2, sticky="W")
listboxStudieSchoolStad.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)



scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=3, column=2, rowspan=6, sticky="E")
listboxStudieSchoolStad.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxStudieSchoolStad.yview)



knopToonstudies = Button(venster, text="Toon alle studies", width=12 , bg= "midnightblue", fg="snow", command=toonAlleStudieInListbox)
knopToonstudies.grid(row=4, column=3)

labelGeselecteerdeStudie = Label(venster, text="Geselecteerde studie:")
labelGeselecteerdeStudie.grid(row = 10, column= 0, sticky= "W")

# logo scholen in pagina zetten
padFotoGeselecteerdeSchool = PhotoImage(file=fotoPad)
fotoSchool = Label(venster, width=100, height=100, bg="silver", image=padFotoGeselecteerdeSchool)
fotoSchool.grid(row=13, column=3) 

ingevoerde_geselecteerdeStudie = StringVar()
invoerveldGeselecteerdeStudie = Entry(venster, textvariable= zoek_studieNaam ) 
invoerveldGeselecteerdeStudie.grid(row=10, column= 1, sticky= "W")

#studie informatie knop en listbox
knopstudieinfo = Button(venster, text="Geef studie info", width=12 , bg= "midnightblue", fg="snow", command= geefstudieinfo)
knopstudieinfo.grid(row=12, column=1)

listboxstudieinfo = Listbox(venster, height=6, width=50)
listboxstudieinfo.grid(row=13, column=1, rowspan=6, columnspan=2, sticky="W")
listboxstudieinfo.bind('<<ListboxSelect>>', haalGeselecteerdeRijOpstudieinfo)


#reisinfo

knopreisinfo = Button(venster, text="Geef reisinfo", width=12 , bg= "midnightblue", fg="snow", command= geefreisinfo)
knopreisinfo.grid(row=24, column=1)

listboxreisinfo = Listbox(venster, height=6, width=50)
listboxreisinfo.grid(row=26, column=1, rowspan=6, columnspan=2, sticky="W")
listboxreisinfo.bind('<<ListboxSelect>>', haalGeselecteerdeRijOpreisinfo)

knopSluit = Button(venster, text= "Sluiten", width= 12 , bg= "midnightblue", fg="snow", command= venster.destroy)
knopSluit.grid(row= 29, column= 4)

venster.mainloop()