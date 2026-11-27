from datetime import datetime
from zimmer import zimmer, zimmer_ist_frei
from speicherung import buchung_speichern, buchungen_laden, buchungen_speichern


def calculate_number_nights():
    while True:
        try:
            check_in = input("Wann möchte der Gast einchecken? (TT.MM.JJJJ): ")
            check_out = input("Wann möchte der Gast auschecken? (TT.MM.JJJJ): ")
            check_in_datum = datetime.strptime(check_in, "%d.%m.%Y")
            check_out_datum = datetime.strptime(check_out, "%d.%m.%Y")

            anzahl_naechte = (check_out_datum - check_in_datum).days
            if anzahl_naechte <= 0:
                print("fehler: Check-out muss nach Check-in liegen")
                continue
            return anzahl_naechte, check_in, check_out
        except ValueError:
            print("ungültiges Datum! Bitte TT.MM.JJJJ verwenden")

def eingabe_personen(frage, minimum):
    while True:
        try:
            anzahl = int(input(frage))

            if anzahl < minimum:
                print ("Ungültige Anzahl! Bitte gültige Anzahl eingeben. ")
                continue
            return anzahl
        except ValueError:
            print("Fehler! Bitte eine ganze Zahl eingeben.")
        

        
def zahlungsart_waehlen():
    while True:
        print("\n--- Zahlungsart auswählen ---")
        print("1. Barzahlung")
        print("2. Karte")
        print("3. TWINT")

        auswahl = input("Bitte wählen Sie 1, 2 oder 3: ")

        if auswahl == "1":
            return "bar"
        elif auswahl == "2":
            return "karte"
        elif auswahl == "3":
            return "TWINT"
        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")    

def enter_booking():
    print("willkommen bei der Hotelbuchung!")
    gebuchte_zimmer = []
    weiteres_zimmer_buchen = True
   
    
    while True:
        vorname = input("Wie lautet der Vorname des Gastes? ").strip()
        if vorname:
            break
        print("Fehler: Bitte einen Vornamen eingeben.")

    while True:
        nachname = input("Wie lautet der Nachname des Gastes? ").strip()
        if nachname:
            break
        print("Fehler: Bitte einen Nachnamen eingeben.")

    gast_name = vorname + " " + nachname
    print("Der Gast heisst:", gast_name)


    print("Der Gast heisst:", gast_name)
    anzahl_erwachsene = eingabe_personen("Wie viele Erwachsene übernachten?", 1)
    anzahl_kinder = eingabe_personen("Wiv viele Kinder übernachten?", 0)
    anzahl_personen = anzahl_erwachsene + anzahl_kinder 
    print("Gesamtanzahl der Gäste:", anzahl_personen)

    

    while True:
        anzahl_naechte, check_in, check_out = calculate_number_nights()
        print("Anzahl Übernachtungen:", anzahl_naechte, "Nächte")
        if anzahl_naechte > 0:
            print("Das Buchungsdatum ist gültig!")
            break
        else:
            print("Fehler: Das Check-out-Datum muss nach dem Check-in-Datum liegen")
        
    anzahl_einzelzimmer = 0
    anzahl_doppelzimmer = 0
    anzahl_familienzimmer = 0 

    
    print("Welche Zimmerarten stehen zur Verfügung?")
    print("1. Einzelzimmer (1 Person)")
    print("2. Doppelzimmer mit Doppelbett (2 Personen)")
    print("3. Doppelzimmer mit 2 Einzelbetten (2 Personen)")
    print("4. Familienzimmer (4 Personen)")


    
    
   
    verbleibende_personen = anzahl_personen 
    while weiteres_zimmer_buchen:
        while True:
         print("Gebuchte Zimmer:", gebuchte_zimmer)
         print("1. Einzelzimmer")
         print("2. Doppelzimmer mit Doppelbett")
         print("3. Doppelzimmer mit 2 Einzelbetten")
         print("4. Familienzimmer")

         
         zimmerartauswahl = input("Wählen Sie 1, 2, 3 oder 4: ")

         if zimmerartauswahl == '1':
            zimmerart = 'Einzelzimmer'
            betten = '1 Einzelbett'
            break

         elif zimmerartauswahl == '2':
            zimmerart = 'Doppelzimmer'
            betten = '1 Doppelbett'
            break

         elif zimmerartauswahl == '3':
            zimmerart = 'Doppelzimmer'
            betten = '2 Einzelbetten'
            break

         elif zimmerartauswahl == '4':
            zimmerart = 'Familienzimmer'
            betten = '1 Doppelbett + 2 Einzelbetten'
            break

        else:
            print("Bitte geben Sie eine Zahl zwischen 1-4 ein")

        
        anzahl_zimmer = eingabe_personen("Wie viele Zimmer dieser Art möchte der Kunde buchen? ", 1)
        passende_zimmer = []

        for nummer, daten in zimmer.items():
            if daten["zimmerart"] == zimmerart and daten["betten"] == betten:
                if nummer not in gebuchte_zimmer:
                    if zimmer_ist_frei(nummer, check_in, check_out):
                        passende_zimmer.append(nummer)

        if anzahl_zimmer > len(passende_zimmer):
            print("Fehler: Es stehen nur noch", len(passende_zimmer), "passende Zimmer zur Auswahl.")
            continue

        ausgewaehlte_zimmer = passende_zimmer[:anzahl_zimmer]
        gebuchte_zimmer.extend(ausgewaehlte_zimmer)

        print("Ausgewählte Zimmernummern:", ausgewaehlte_zimmer)


        personen_im_zimmer = 0
        for nummer in ausgewaehlte_zimmer:
            personen_im_zimmer += zimmer[nummer]["max_personen"]
        verbleibende_personen = max(0, verbleibende_personen - personen_im_zimmer)
        print("Noch ohne Zimmer:", verbleibende_personen)
        

        print("Zimmer hinzufügen:", anzahl_zimmer, "x", zimmerart)
        while True:
            weiteres_zimmer_input = input('Wollen Sie ein weiteres Zimmer buchen (J/N): ')
            if weiteres_zimmer_input == 'J':
                break
            elif weiteres_zimmer_input == 'N':
                if verbleibende_personen > 0:
                     print("Fehler: Es fehlen noch Zimmer für", verbleibende_personen, "Personen!")
                     break
                weiteres_zimmer_buchen = False
                break
            else:
                print("Fehler: Bitte nur J und N eingeben.")
    
    print("Gebuchte Zimmer:")

    for nummer in gebuchte_zimmer:
        print("Zimmer", nummer, "-", zimmer[nummer]["zimmerart"], "-", zimmer[nummer]["betten"])
   
    
    
    
    buchung = {
        "nummer": None,
        "vorname": vorname,
        "nachname": nachname,
        "gast_name": gast_name,
        "erwachsene": anzahl_erwachsene,
        "kinder": anzahl_kinder,
        "personen": anzahl_personen,
        "naechte": anzahl_naechte,
        "check_in": check_in,
        "check_out": check_out,
        "zimmer": gebuchte_zimmer,
        "zahlungsart": None,
        "verpflegung": "keine",
        "parkplatz": False,
        "wlan": False,
        "gesamtpreis": None,
        "status": "reserviert"
    }

    

    

    

        
    zusatzkosten = calculate_additional_costs(buchung)
    buchung["gesamtpreis"] = calculate_booking_cost(
        gebuchte_zimmer,
        anzahl_naechte,
        zusatzkosten
    )
    
    buchung["zahlungsart"] = zahlungsart_waehlen()
    
    buchung_speichern(buchung) 


    
                



def check_availability():
    print("\n--- Zimmerverfügbarkeit prüfen ---")

    anzahl_naechte, check_in, check_out = calculate_number_nights()

    freie_zimmer = []

    for nummer, daten in zimmer.items():
        if zimmer_ist_frei(nummer, check_in, check_out):
            freie_zimmer.append(nummer)

    if len(freie_zimmer) == 0:
        print("In diesem Zeitraum sind keine Zimmer verfügbar.")
    else:
        print("Anzahl verfügbarer Zimmer:", len(freie_zimmer))

        for nummer in freie_zimmer:
            print(f"Zimmer {nummer}: {zimmer[nummer]['zimmerart']} - {zimmer[nummer]['betten']}")



def calculate_additional_costs(buchung):
    zusatzkosten = 0
    anzahl_naechte = buchung["naechte"]
    anzahl_personen = buchung["personen"]

    if buchung["parkplatz"]:
        zusatzkosten += 15 * anzahl_naechte

    if buchung["verpflegung"].lower() == "halbpension":
        zusatzkosten += 35 * anzahl_personen * anzahl_naechte

    elif buchung["verpflegung"].lower() == "vollpension":
        zusatzkosten += 60 * anzahl_personen * anzahl_naechte

    return zusatzkosten

def calculate_booking_cost(gebuchte_zimmer, anzahl_naechte, zusatzkosten=0):
    zimmerkosten = 0

    for nummer in gebuchte_zimmer:
        zimmerkosten += zimmer[nummer]["preis"] * anzahl_naechte

    nettobetrag = zimmerkosten + zusatzkosten
    mwst_zimmer = zimmerkosten * 0.038
    mwst_zusatz = zusatzkosten * 0.081
    mwst = mwst_zimmer + mwst_zusatz
    gesamtpreis = round(nettobetrag + mwst, 2)

    print("\n--- Preisübersicht ---")
    print(f"Zimmerkosten: CHF {zimmerkosten:.2f}")
    print(f"Zusatzkosten: CHF {zusatzkosten:.2f}")
    print(f"MWST Zimmer (3.8%): CHF {mwst_zimmer:.2f}")
    print(f"MWST Zusatzleistungen (8.1%): CHF {mwst_zusatz:.2f}")
    print(f"MWST Total: CHF {mwst:.2f}")
    print(f"Gesamtpreis: CHF {gesamtpreis:.2f}")

    return gesamtpreis

def show_booking_cost():
    print("\n--- Gesamtpreis berechnen ---")

    buchungsnummer = input("Buchungsnummer eingeben: ").strip().upper()
    buchungen = buchungen_laden()

    for buchung in buchungen:
        if buchung["nummer"] == buchungsnummer:

            if buchung["status"] == "storniert":
                print("Diese Buchung wurde storniert.")
                return

            print("Gast:", buchung["gast_name"])
            print("Zimmer:", buchung["zimmer"])
            print("Übernachtungen:", buchung["naechte"])

            zusatzkosten = calculate_additional_costs(buchung)

            calculate_booking_cost(
                buchung["zimmer"],
                buchung["naechte"],
                zusatzkosten
            )
            return

    print("Keine Buchung gefunden.")
def change_booking():
    print("\n--- Buchung ändern ---")

    buchungsnummer = input("Buchungsnummer eingeben: ").strip().upper()
    buchungen = buchungen_laden()

    for buchung in buchungen:
        if buchung["nummer"] == buchungsnummer:
            if buchung["status"] != "reserviert":
                print("Nur reservierte Buchungen können geändert werden.")
                return

            print("Gast:", buchung["gast_name"])
            print("Zimmer:", buchung["zimmer"])
            print("Check-in:", buchung["check_in"])
            print("Check-out:", buchung["check_out"])
            print("Gesamtpreis:", buchung["gesamtpreis"])
            print("\nWas möchten Sie ändern?")
            print("1. Vor- und Nachname")
            print("2. Aufenthaltszeitraum")
            print("3. Zimmer")
            print("4. Zahlungsart")
            print("0. Zurück")

            auswahl = input("Bitte wählen Sie 0 bis 4: ")

            if auswahl == "1":
                vorname = input("Neuer Vorname: ").strip()
                nachname = input("Neuer Nachname: ").strip()

                if not vorname or not nachname:
                    print("Der Name darf nicht leer sein.")
                    return

                buchung["vorname"] = vorname
                buchung["nachname"] = nachname
                buchung["gast_name"] = vorname + " " + nachname

                buchungen_speichern(buchungen)
                print("Der Name wurde erfolgreich geändert!")

            elif auswahl == "4":
                buchung["zahlungsart"] = zahlungsart_waehlen()

                buchungen_speichern(buchungen)
                print("Die Zahlungsart wurde erfolgreich geändert!")

            elif auswahl == "0":
                return

            elif auswahl == "2":
                anzahl_naechte, check_in, check_out = calculate_number_nights()

                for nummer in buchung["zimmer"]:
                    if not zimmer_ist_frei(nummer, check_in, check_out, buchungsnummer):
                        print(f"Zimmer {nummer} ist im neuen Zeitraum nicht verfügbar.")
                        return

                print("Alle gebuchten Zimmer sind im neuen Zeitraum verfügbar.")
                buchung["check_in"] = check_in
                buchung["check_out"] = check_out
                buchung["naechte"] = anzahl_naechte
                zusatzkosten = calculate_additional_costs(buchung)
                buchung["gesamtpreis"] = calculate_booking_cost(
                    buchung["zimmer"],
                    anzahl_naechte,
                    zusatzkosten
                )


                
                
                buchungen_speichern(buchungen)
                print("Der Aufenthaltszeitraum wurde erfolgreich geändert!")
                
            elif auswahl == "3":
                check_in = buchung["check_in"]
                check_out = buchung["check_out"]

                freie_zimmer = []

                for nummer, daten in zimmer.items():
                    if zimmer_ist_frei(nummer, check_in, check_out, buchungsnummer):
                        freie_zimmer.append(nummer)

                if len(freie_zimmer) == 0:
                    print("Keine Zimmer verfügbar.")
                    return

                print("\n--- Verfügbare Zimmer ---")

                for nummer in freie_zimmer:
                    print(f"Zimmer {nummer}: {zimmer[nummer]['zimmerart']} - {zimmer[nummer]['betten']}")
                    neue_zimmer = []
                kapazitaet = 0

                while kapazitaet < buchung["personen"]:
                    nummer = eingabe_personen("Neue Zimmernummer eingeben: ", 0)

                    if nummer == 0:
                        print("Zimmeränderung abgebrochen.")
                        return

                    if nummer not in freie_zimmer:
                        print("Dieses Zimmer ist nicht verfügbar.")
                        continue

                    if nummer in neue_zimmer:
                        print("Dieses Zimmer wurde bereits ausgewählt.")
                        continue

                    neue_zimmer.append(nummer)
                    kapazitaet += zimmer[nummer]["max_personen"]

                    print("Ausgewählte Zimmer:", neue_zimmer)
                    print("Kapazität:", kapazitaet)
                    print("Benötigte Plätze:", buchung["personen"])

                buchung["zimmer"] = neue_zimmer

                zusatzkosten = calculate_additional_costs(buchung)
                buchung["gesamtpreis"] = calculate_booking_cost(
                    neue_zimmer,
                    buchung["naechte"],
                    zusatzkosten
                )

                buchungen_speichern(buchungen)

                print("Die Zimmer wurden erfolgreich geändert!")
            else:
                print("Ungültige Auswahl.")

            return

    print("Keine Buchung gefunden.")


def search_booking():
    print("\n--- Buchungen suchen ---")

    suchbegriff = input("Buchungsnummer oder Gastname eingeben: ").strip().lower()

    if not suchbegriff:
        print("Bitte einen Suchbegriff eingeben.")
        return

    buchungen = buchungen_laden()
    gefunden = False

    for buchung in buchungen:
        if suchbegriff in str(buchung["nummer"]).lower() or suchbegriff in buchung["gast_name"].lower():

            gefunden = True

            print("\n--- Buchung gefunden ---")
            print("Buchungsnummer:", buchung["nummer"])
            print("Gast:", buchung["gast_name"])
            print("Personen:", buchung["personen"])
            print("Zimmer:", ", ".join(map(str, buchung["zimmer"])))
            print("Check-in:", buchung["check_in"])
            print("Check-out:", buchung["check_out"])
            print("Übernachtungen:", buchung["naechte"])
            print("Zahlungsart:", (buchung["zahlungsart"] or "Nicht angegeben").capitalize() if buchung["zahlungsart"] != "TWINT" else "TWINT")
            print(f"Gesamtpreis: CHF {buchung['gesamtpreis']:.2f}")
            print("Status:", buchung["status"])

    if not gefunden:
        print("Keine passende Buchung gefunden.")

def cancel_booking():
    print("\n--- Buchung stornieren ---")

    buchungsnummer = input("Buchungsnummer eingeben: ").strip().upper()
    buchungen = buchungen_laden()

    for buchung in buchungen:
        if buchung["nummer"] == buchungsnummer:
            print("Gast:", buchung["gast_name"])
            print("Zimmer:", buchung["zimmer"])
            print("Status:", buchung["status"])

            if buchung["status"] != "reserviert":
                print("Nur reservierte Buchungen können storniert werden.")
                return

            while True:
                bestaetigung = input("Buchung wirklich stornieren? (J/N): ").strip().upper()

                if bestaetigung == "J":
                    buchung["status"] = "storniert"
                    buchungen_speichern(buchungen)
                    print("Die Buchung wurde erfolgreich storniert!")
                    return

                elif bestaetigung == "N":
                    print("Stornierung abgebrochen.")
                    return

                else:
                    print("Bitte J oder N eingeben.")

    print("Keine Buchung gefunden.")