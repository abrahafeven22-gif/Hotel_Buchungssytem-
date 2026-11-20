from datetime import datetime

zimmer_liste = [
    {"nummer": 100, "art": "Einzelzimmer", "preis": 100.00},
    {"nummer": 200, "art": "Doppelzimmer", "preis": 150.00},
    {"nummer": 300, "art": "Doppelzimmer", "preis": 150.00},
    {"nummer": 400, "art": "Familienzimmer", "preis": 220.00},
]

buchungen_liste = [
    {"nummer": "B0001", "nachname": "Müller", "zimmer": 100, "check_in": "10.10.2026", "check_out": "13.10.2026", "status": "abgeschlossen", "gesamtpreis": 311.40},
    {"nummer": "B0002", "nachname": "Schmidt", "zimmer": 200, "check_in": "11.10.2026", "check_out": "14.10.2026", "status": "eingecheckt", "gesamtpreis": 467.10},
    {"nummer": "B0003", "nachname": "Meier", "zimmer": 300, "check_in": "12.10.2026", "check_out": "15.10.2026", "status": "reserviert", "gesamtpreis": 467.10},
    {"nummer": "B0004", "nachname": "Schneider", "zimmer": 400, "check_in": "13.10.2026", "check_out": "16.10.2026", "status": "storniert", "gesamtpreis": 685.08},
]

def text_zu_datum(text):
    return datetime.strptime(text, "%d.%m.%Y").date()
   
def zimmer_status_fuer_datum(datum):
    pass
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
    pass

def hotel_statistiken():
    print("=== Hotelstatistiken ===")
    print("Test ganzer Oktober:")
    buchungsanzahl_und_wert("01.10.2026", "31.10.2026")
    print("Test 01.10. bis 11.10.:")
    buchungsanzahl_und_wert("01.10.2026", "11.10.2026")
    print("Test ganzer November:")
    buchungsanzahl_und_wert("01.11.2026", "30.11.2026")
    print("Test pruefe_zeitraum:")
    print(pruefe_zeitraum("01.10.2026", "31.10.2026"))
    print(pruefe_zeitraum("31.10.2026", "01.10.2026"))
    print(pruefe_zeitraum("31.02.2026", "10.03.2026"))
    print(pruefe_zeitraum("hallo", "31.10.2026"))
    print("Test ungültiger Zeitraum bei der Zählung")
    buchungsanzahl_und_wert("31.10.2026", "01.10.2026")
    buchungsanzahl_und_wert("31.02.2026", "10.03.2026")


    
hotel_statistiken()