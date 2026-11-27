from datetime import datetime
from speicherung import buchungen_laden


def zimmer_ist_frei(zimmernummer, check_in, check_out, ignorierte_buchung=None):
    buchungen = buchungen_laden()

    neuer_check_in = datetime.strptime(check_in, "%d.%m.%Y")
    neuer_check_out = datetime.strptime(check_out, "%d.%m.%Y")

    for buchung in buchungen:
        if buchung.get("status") == "storniert":
            continue
        if ignorierte_buchung is not None and buchung.get("nummer") == ignorierte_buchung:
            continue

        if zimmernummer in buchung["zimmer"]:
            alter_check_in = datetime.strptime(buchung["check_in"], "%d.%m.%Y")
            alter_check_out = datetime.strptime(buchung["check_out"], "%d.%m.%Y")

            if neuer_check_in < alter_check_out and neuer_check_out > alter_check_in:
                return False

    return True


#Alle Zimmer unseres Hotels
zimmer = {}

# 16 Einzelzimmer: 100 bis 115
for nummer in range(100,116):
    zimmer[nummer] = {
        "zimmerart": "Einzelzimmer",
        "max_personen": 1,
        "betten": "1 Einzelbett",
        "preis": 100.00
    }
#11 Doppelzimmer mit Doppelbett: Zimmer 200 bis 210
for nummer in range(200,211):
    zimmer[nummer] = {
        "zimmerart": "Doppelzimmer",
        "max_personen": 2,
        "betten": "1 Doppelbett",
        "preis": 150.00
    }
# 11 Doppelzimmer mit Einzelbetten: 300 bis 310
for nummer in range(300,311):
    zimmer[nummer] = {
        "zimmerart": "Doppelzimmer",
        "max_personen": 2,
        "betten": "2 Einzelbetten",
        "preis": 150.00
    }
# 11 Familienzimmer: Zimmer 400 bis 410
for nummer in range(400,411):
    zimmer[nummer] = {
        "zimmerart": "Familienzimmer",
        "max_personen": 4,
        "betten": "1 Doppelbett + 2 Einzelbetten",
        "preis": 220.00
    }

def freie_zimmer_nach_art(zimmerart):
    freie_zimmer = []

    for nummer, daten in zimmer.items():
        if daten["zimmerart"] == zimmerart:
            freie_zimmer.append(nummer)
    return freie_zimmer

