from booking import enter_booking, check_availability, cancel_booking, change_booking, show_booking_cost, search_booking

def main():
    while True:
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
        elif auswahl == "2":
            check_availability()
        elif auswahl == "3":
            show_booking_cost()
        elif auswahl == "4":
            print("\n--- Buchung verwalten ---")
            print("1. Buchung ändern")
            print("2. Buchung stornieren")
            print("0. Zurück")

            aktion = input("Bitte wählen Sie 0, 1 oder 2: ")

            if aktion == "1":
                change_booking()
            elif aktion == "2":
                cancel_booking()
            elif aktion == "0":
                continue
            else:
                print("Ungültige Auswahl.")

        elif auswahl == "0":
            print("Hotelbuchungssystem beendet.")
            break
        elif auswahl == "8":
            search_booking()
        elif auswahl in ["5", "6", "7"]:
            print("Diese Funktion ist noch nicht verfügbar.")

        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")


main()

 
