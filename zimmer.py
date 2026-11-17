#Alle Zimmer unseres Hotels
zimmer = {}

# 15 Einzelzimmer: 100 bis 114
for nummer in range(100,115):
    zimmer[nummer] = {
        "zimmerart": "Einzelzimmer",
        "max_personen": 1,
        "betten": "1 Einzelbett",
        "preis": 100.00
    }
#15 Doppelzimmer: Zimmer 200 bis 214
for nummer in range(200,215):
    zimmer[nummer] = {
        "zimmerart": "Doppelzimmer",
        "max_personen": 2,
        "betten": "1 Doppelbett",
        "preis": 150.00
    }

# 10 Familienzimmer: Zimmer 300 bis 309
for nummer in range(300,310):
    zimmer[nummer] = {
        "zimmerart": "Familienzimmer",
        "max_personen": 4,
        "betten": "1 Doppelbett + 2 Einzelbetten",
        "preis": 220.00
    }

