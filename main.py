from booking import enter_booking

def main():
    print("1. Buchung erfassen")
    print("2. Zimmerverfügbarkeit prüfen")
    print("3. Gesamtpreis berechnen")
    print("4. Buchung ändern oder stornieren")
    print("5. Zusatzleistungen auswählen")
    print("6. Hotelstatistiken anzeigen")
    print("7. Check-in / Check-out")
    print("8. Buchungen suchen")
    print ("0. Programm beenden")
    auswahl = input("Bitte wähle eine Zahl von 0 bis 8: ")
    if auswahl == "1":
        print("Du hast Buchung erfassen ausgewählt.")
        enter_booking()
    elif auswahl == "0":
        print("Hotelbuchungssystem beendet.")
        
main()

 
