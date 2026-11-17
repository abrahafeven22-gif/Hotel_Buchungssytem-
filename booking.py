from datetime import datetime
from zimmer import zimmer 

def enter_booking():
    print("willkommen bei der Hotelbuchung!")
    gast_name = input("wie heisst der Gast?")
    print("Der Gast heisst:", gast_name)
    anzahl_erwachsene = int(input("wie viele Erwachsene übernachten?"))
    anzahl_kinder = int(input("Wie viele Kinder übernachten?"))
    anzahl_personen = anzahl_erwachsene + anzahl_kinder
    print("Gesamtanzahl der Gäste:", anzahl_personen)
    while True:
        check_in = input("Wann möchte der Gast einchecken? (TT.MM.JJJJ): ")
        check_out = input("Wann möchte der Gast auschecken? (TT.MM.JJJJ): ")
        check_in_datum = datetime.strptime(check_in, "%d.%m.%Y")
        check_out_datum = datetime.strptime(check_out, "%d.%m.%Y")
        anzahl_naechte = (check_out_datum - check_in_datum).days
        print("Anzahl Übernachtungen: ", anzahl_naechte)
        if anzahl_naechte <= 0:
            print("Fehler: Das Check-out-Datum muss nach dem Check-in-Datum liegen")
            continue
        
        print("Das Buchungsdatum ist gültig!")
        break
    print("Welche Zimmerart möchte der Gast buchen?")
    print("1. Einzelzimmer")
    print("2. Doppelzimmer")
    print("3. Familienzimmer")
    verbleibende_personen = anzahl_personen
    gebuchte_zimmer = []
    while verbleibende_personen > 0:
        zimmer_auswahl = input("Bitte wähle eine Zimmerart (1-3): ")

        if zimmer_auswahl == "1":
            zimmerart = "Einzelzimmer"
            

        elif zimmer_auswahl == "2":
             zimmerart = "Doppelzimmer"
             
        elif zimmer_auswahl == "3":
             zimmerart = "Familienzimmer"
             
        else:
            print("Ungültige Auswahl. Bitte wähle 1,2 oder 3.")
            continue
        print("Gewähltes Zimmerart", zimmerart)
        if zimmerart == "Einzelzimmer":
                max_personen = 1
        elif zimmerart == "Doppelzimmer":
                    max_personen = 2
        else:
                    max_personen = 4
        personen_im_zimmer = min(verbleibende_personen, max_personen)
        gebuchte_zimmer.append(zimmerart)
        verbleibende_personen -= personen_im_zimmer

        print("Zimmer hinzugefügt:", zimmerart)
        print("Personen in diesem Zimmer:", personen_im_zimmer)
        print("Noch verbleibende Personen:", verbleibende_personen)
    print("Alle Gäste wurden auf Zimmer verteilt!")
    print("Gebuchte Zimmer:", gebuchte_zimmer)
                



def check_availability():
    pass
def calculate_booking_cost():
    pass
def change_booking():
    pass
def cancel_booking():
    pass
