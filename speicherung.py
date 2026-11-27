
import json
import os


def buchungen_laden():
    buchungen = []

    if os.path.exists("buchungen.json"):
        with open("buchungen.json", "r", encoding="utf-8") as datei:
            inhalt = datei.read().strip()

            if inhalt:
                buchungen = json.loads(inhalt)

                if isinstance(buchungen, dict):
                    buchungen = [buchungen]

                if not isinstance(buchungen, list):
                    raise ValueError("Ungültiges Buchungsformat.")

    return buchungen


def buchungen_speichern(buchungen):
    with open("buchungen.json", "w", encoding="utf-8") as datei:
        json.dump(buchungen, datei, ensure_ascii=False, indent=4)
    with open("buchungen.txt", "w", encoding="utf-8") as datei:
        for buchung in buchungen:
            datei.write(
                f"Buchungsnummer: {buchung['nummer']}\n"
                f"Gast: {buchung['gast_name']}\n"
                f"Personen: {buchung['personen']}\n"
                f"Check-in: {buchung['check_in']}\n"
                f"Check-out: {buchung['check_out']}\n"
                f"Zimmer: {', '.join(map(str, buchung['zimmer']))}\n"
                f"Zahlungsart: {buchung['zahlungsart']}\n"
                f"Verpflegung: {buchung['verpflegung']}\n"
                f"Gesamtpreis: CHF {buchung['gesamtpreis']:.2f}\n"
                f"Status: {buchung['status']}\n"
                f"------------------------------\n"
            )

def buchung_speichern(buchung):
    buchungen = buchungen_laden()

    hoechste_nummer = 0

    for alte_buchung in buchungen:
        nummer = alte_buchung.get("nummer")

        if nummer:
            zahl = int(nummer[1:])

            if zahl > hoechste_nummer:
                hoechste_nummer = zahl

    buchung["nummer"] = f"B{hoechste_nummer + 1:04d}"

    buchungen.append(buchung)
    buchungen_speichern(buchungen)

    print("Die Buchung wurde erfolgreich gespeichert!")
    print("Buchungsnummer:", buchung["nummer"])