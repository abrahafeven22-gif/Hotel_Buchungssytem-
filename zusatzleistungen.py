PREISE_VERPFLEGUNG = {"keine":0.00, "halbpension": 35.00, "vollpension": 60.00}
PARKPLATZ_PRO_NACHT = 15.00
WLAN_PREIS = 0.00


def zusatzkosten_berechnen(verpflegung, parkplatz, wlan, gaeste, naechte):
    kosten_verpflegung = PREISE_VERPFLEGUNG[verpflegung] * gaeste * naechte
    kosten_parkplatz = 0.00
    if parkplatz:
        kosten_parkplatz = PARKPLATZ_PRO_NACHT * naechte
    kosten_wlan = 0.00
    if wlan:
        kosten_wlan = WLAN_PREIS
    total = kosten_verpflegung + kosten_parkplatz + kosten_wlan
    return {
        "verpflegung": kosten_verpflegung,
        "parkplatz": kosten_parkplatz,
        "wlan": kosten_wlan,
        "total": total,
    }

def zusatzkosten_anzeigen(kosten):
    print("Kosten Zusatzleistungen (netto):")
    print(f"  Verpflegung: CHF {kosten['verpflegung']:.2f}")
    print(f"  Parkplatz: CHF {kosten['parkplatz']:.2f}")
    print(f"  WLAN: CHF {kosten['wlan']:.2f}")
    print(f"  Total: CHF {kosten['total']:.2f}")

def verpflegung_waehlen():
    while True:
        print("Verpflegung:")
        print("1. Keine (CHF 0.00)")
        print("2. Halbpension (CHF 35.00 pro Person und Nacht)")
        print("3. Vollpension (CHF 60.00 pro Person und Nacht)")
        wahl = input("Auswahl: ")
        if wahl == "1":
            return "keine"
        elif wahl == "2":
            return "halbpension"
        elif wahl == "3":
            return "vollpension"
        else:
            print("Ungültige Auswahl. Bitte 1, 2 oder 3 eingeben.")

def ja_nein_fragen(frage):
    while True:
        antwort = input(f"{frage} (j/n): ").lower()
        if antwort == "j":
            return True
        elif antwort == "n":
            return False
        else:
            print("Ungültige Eingabe. Bitte 'j' oder 'n' eingeben.")

def zusatzleistungen_waehlen(gaeste, naechte):
    while True:
        verpflegung = verpflegung_waehlen()
        parkplatz = ja_nein_fragen("Parkplatz gewünscht?")
        wlan = ja_nein_fragen("WLAN gewünscht?")
        kosten = zusatzkosten_berechnen(verpflegung, parkplatz, wlan, gaeste, naechte)
        zusatzkosten_anzeigen(kosten)
        if ja_nein_fragen("Zusatzleistungen bestätigen?"):
            return {
                "verpflegung": verpflegung,
                "parkplatz": parkplatz,
                "wlan": wlan,
                "zusatzkosten": kosten["total"],
            }
        print("Bitte Zusatzleistungen neu wählen.")

if __name__ == "__main__":
    auswahl = zusatzleistungen_waehlen(2, 3)
    print(auswahl)
   

# US-05: Zusatzleistungen und Verpflegung
