buchungen_liste = [
    {"nummer": "B0001", "vorname": "Anna", "nachname": "Müller", "zimmer": 100, "check_in": "10.10.2026", "check_out": "13.10.2026", "status": "abgeschlossen", "gesamtpreis": 311.40},
    {"nummer": "B0002", "vorname": "Peter", "nachname": "Schmidt", "zimmer": 200, "check_in": "11.10.2026","check_out": "14.10.2026", "status": "eingecheckt", "gesamtpreis": 467.10},
    {"nummer": "B0003", "vorname": "Laura", "nachname": "Meier", "zimmer": 300, "check_in": "12.10.2026", "check_out": "15.10.2026","status": "reserviert", "gesamtpreis": 467.10},
    {"nummer": "B0004", "vorname": "Marco", "nachname": "Schneider", "zimmer": 400, "check_in": "13.10.2026","check_out": "16.10.2026", "status": "storniert", "gesamtpreis": 685.08},
    {"nummer": "B0005", "vorname": "Thomas", "nachname": "Müller", "zimmer": 205, "check_in": "20.10.2026","check_out": "22.10.2026", "status": "reserviert", "gesamtpreis": 311.40},
]

def buchung_anzeigen(buchung):
    print(f"Buchung {buchung['nummer']}")
    print(f"  Name: {buchung['vorname']} {buchung['nachname']}")
    print(f"  Zimmer: {buchung['zimmer']}")
    print(f"  Check-in: {buchung['check_in']}, check-out: {buchung['check_out']}")
    print(f"  Status: {buchung['status']}")
    print(f"  Gesamtpreis: CHF {buchung['gesamtpreis']:.2f}")

def suche_nach_nummer(nummer):
    for buchung in buchungen_liste:
        if buchung["nummer"] == nummer.upper():
            return buchung
    return None

def nummer_suche_und_anzeigen(nummer):
    buchung = suche_nach_nummer(nummer)
    if buchung is None:
        print(f"Keine Buchung gefunden.")
    else:
        buchung_anzeigen(buchung)

def suche_nach_nachname(nachname):
    treffer = []
    for buchung in buchungen_liste:
        if buchung["nachname"].lower() == nachname.lower():
            treffer.append(buchung)
    return treffer

def nachname_suche_und_anzeigen(nachname):
    treffer = suche_nach_nachname(nachname)
    if len(treffer) == 0:
        print("Keine Buchung gefunden.")
    else:
        print(f"{len(treffer)} Buchung(en) gefunden:")
        for buchung in treffer:
            buchung_anzeigen(buchung)

def buchungen_suchen():
    print("=== Buchungssuche ===")
    while True:
        print("\nSuchoptionen:")
        print("1. Nach Buchungsnummer suchen")
        print("2. Nach Nachname suchen")
        print("0. Zurück")
        wahl = input("Auswahl: ")
        if wahl == "1":
            nummer = input("Buchungsnummer: ")
            nummer_suche_und_anzeigen(nummer)
        elif wahl == "2":
            nachname = input("Nachnamen: ")
            nachname_suche_und_anzeigen(nachname)
        elif wahl == "0":
            break
        else:
            print("Ungültige Auswahl. Bitte 0, 1 oder 2 wählen.")

if __name__ == "__main__":
        buchungen_suchen()

