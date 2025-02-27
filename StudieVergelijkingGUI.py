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


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("StudieVergelijking")

labelIntro = Label(venster, text="Welkom! Vul hieronder een of meerdere zoektermen in, vervolgens zul je alle opties met jouw ingevulde eisen zien. Als je een studie selecteert, kun je vervolgens meer studie info of reisinformatie opvragen.")
labelIntro.grid(row=0, column=0, sticky="W")


schoolNaam = Label(venster, text="School:")
schoolNaam.grid(row=1, column=0)


ingevoerde_schoolNaam = StringVar ()
invoerVeldSchoolNaam = Entry(venster, textvariable= ingevoerde_schoolNaam)
invoerVeldSchoolNaam.grid(row=1, column=1, sticky="W")


studieNaam = Label(venster, text="Studie:")
studieNaam.grid(row=2, column=0)


ingevoerde_studieNaam = StringVar ()
invoerVeldStudieNaam = Entry(venster, textvariable= ingevoerde_studieNaam)
invoerVeldStudieNaam.grid(row=2, column=1, sticky="W")



stadNaam = Label(venster, text="Stad:")
stadNaam.grid(row=3, column=0)


ingevoerde_stadNaam = StringVar ()
invoerVeldStadNaam = Entry(venster, textvariable= ingevoerde_stadNaam)
invoerVeldStadNaam.grid(row=3, column=1, sticky="W")

KnopZoek = Button(venster, text="Zoek", width= 12, command= zoekStudies)
KnopZoek.grid(row=1, column=3)









#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
