from datetime import datetime

zimmer_liste = []

for nummer in range(100, 116):
    zimmer_liste.append({"nummer": nummer, "art": "Einzelzimmer", "betten": "1 Einzelbett", "max_gaeste": 1, "preis":100.00})

for nummer in range(200, 211):
    zimmer_liste.append({"nummer": nummer, "art": "Doppelzimmer", "betten": "1 Doppelbett", "max_gaeste": 2, "preis":150.00})

for nummer in range(300, 311):
    zimmer_liste.append({"nummer": nummer, "art": "Doppelzimmer", "betten": "2 Einzelbetten", "max_gaeste": 2, "preis":150.00})   

for nummer in range(400, 411):
    zimmer_liste.append({"nummer": nummer, "art": "Familienzimmer", "betten": "1 Doppelbett + 2 Einzelbetten", "max_gaeste": 4, "preis":220.00})


buchungen_liste = [
    {"nummer": "B0001", "nachname": "Müller", "zimmer": 100, "check_in": "10.10.2026", "check_out": "13.10.2026", "status": "abgeschlossen", "gesamtpreis": 311.40},
    {"nummer": "B0002", "nachname": "Schmidt", "zimmer": 200, "check_in": "11.10.2026", "check_out": "14.10.2026", "status": "eingecheckt", "gesamtpreis": 467.10},
    {"nummer": "B0003", "nachname": "Meier", "zimmer": 300, "check_in": "12.10.2026", "check_out": "15.10.2026", "status": "reserviert", "gesamtpreis": 467.10},
    {"nummer": "B0004", "nachname": "Schneider", "zimmer": 400, "check_in": "13.10.2026", "check_out": "16.10.2026", "status": "storniert", "gesamtpreis": 685.08},
]

def text_zu_datum(text):
    return datetime.strptime(text, "%d.%m.%Y").date()

def zimmerart_von(zimmernummer):
    for zimmer in zimmer_liste:
        if zimmer["nummer"] == zimmernummer:
            return zimmer["art"]
    return None


def status_von_zimmer(zimmernummer, datum):
    for buchung in buchungen_liste:
        if buchung["zimmer"] == zimmernummer:
            check_in = text_zu_datum(buchung["check_in"])
            check_out = text_zu_datum(buchung["check_out"])
            if check_in <= datum < check_out:
                if buchung["status"] == "eingecheckt":
                    return "belegt"
                if buchung["status"] == "reserviert":
                    return "reserviert"
    return "frei"
  
   
def zimmer_status_fuer_datum(datum):
    if not pruefe_zeitraum(datum, datum):
        return
    tag = text_zu_datum(datum)
    frei = []
    reserviert = []
    belegt = []
    for zimmer in zimmer_liste:
        status = status_von_zimmer(zimmer["nummer"], tag)
        if status == "frei":
            frei.append(str(zimmer["nummer"]))
        elif status == "reserviert":
            reserviert.append(str(zimmer["nummer"]))
        else:
            belegt.append(str(zimmer["nummer"]))

    print(f"Zimmerstatus am {datum}:")
    print(f"Frei ({len(frei)}): {', '.join(frei) or 'keine'}")
    print(f"Reserviert ({len(reserviert)}): {', '.join(reserviert) or 'keine'}")
    print(f"Belegt ({len(belegt)}): {', '.join(belegt) or 'keine'}")


def pruefe_zeitraum(von, bis):
    try:
        von_datum = text_zu_datum(von)
        bis_datum = text_zu_datum(bis)
    except ValueError:
        print("Fehler: Ungültiges Datum. Bitte im Format TT.MM.JJJJ eingeben.")
        return False
    if bis_datum < von_datum:
        print("Fehler: Das Bis-Datum liegt vor dem Von-Datum.")
        return False
    return True


def buchungsanzahl_und_wert(von, bis):
    if not pruefe_zeitraum(von, bis):
        return
    von_datum = text_zu_datum(von)
    bis_datum = text_zu_datum(bis)
    anzahl = 0
    wert = 0.00
    for buchung in buchungen_liste:
        check_in = text_zu_datum(buchung["check_in"])
        if buchung["status"] != "storniert" and von_datum <= check_in <= bis_datum:
            anzahl += 1
            wert += buchung["gesamtpreis"]
    print(f"Anzahl aktiver Buchungen: {anzahl}")
    print(f"Buchungswert CHF: {wert:.2f}")


def meistgebuchte_zimmerart(von, bis):
    if not pruefe_zeitraum(von, bis):
        return
    von_datum = text_zu_datum(von)
    bis_datum = text_zu_datum(bis)
    zaehler = {}
    for buchung in buchungen_liste:
        check_in = text_zu_datum(buchung["check_in"])
        if buchung["status"] != "storniert" and von_datum <= check_in <= bis_datum:
            art = zimmerart_von(buchung["zimmer"])
            if art in zaehler:
                zaehler[art] += 1
            else:
                zaehler[art] = 1
    if len(zaehler) == 0:
        print("Meistgebuchte Zimmerart: keine Buchungen im Zeitraum")
        return
    hoechste_anzahl = max(zaehler.values())
    meistgebuchte = []
    for art in zaehler:
        if zaehler[art] == hoechste_anzahl:
            meistgebuchte.append(art)
    print(f"Meistgebuchte Zimmerart: {', '.join(meistgebuchte)} (Anzahl Buchungen: {hoechste_anzahl})")


def hotel_statistiken():
    while True:
        print("\n=== Hotelstatistiken ===")
        print("1. Zimmerstatus an einem Datum")
        print("2. Anzahl Buchungen und Buchungswert im Zeitraum")
        print("3. Meistgebuchte Zimmerart in Zeitraum")
        print("0. Zurück")
        wahl = input("Auswahl: ")
        if wahl == "1":
            datum = input("Datum (TT.MM.JJJJ): ")
            zimmer_status_fuer_datum(datum)
        elif wahl == "2":
            von = input("Von (TT.MM.JJJJ): ")
            bis = input("Bis (TT.MM.JJJJ): ")
            buchungsanzahl_und_wert(von, bis)
        elif wahl == "3":
            von = input("Von (TT.MM.JJJJ): ")
            bis = input("Bis (TT.MM.JJJJ): ")
            meistgebuchte_zimmerart(von, bis)
        elif wahl == "0":
            break
        else:
            print("Ungültige Auswahl. Bitte 0, 1, 2 oder 3 wählen.")



if __name__ == "__main__":
    hotel_statistiken()