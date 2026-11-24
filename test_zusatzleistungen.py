from zusatzleistungen import *


def tests_ausfuehren():
    print("Tests 1: Halbpension, 2 Gäste, 2 Nächte")
    zusatzkosten_anzeigen(zusatzkosten_berechnen("halbpension", False, False, 2, 2))
    print("Tests 2: nur WLAN, 2 Gäste, 2 Nächte")
    zusatzkosten_anzeigen(zusatzkosten_berechnen("keine", False, True, 2, 3))
    print("Test 3: Vollpension, Parkplatz, WLAN, 1 Gast, 3 Nächte")
    zusatzkosten_anzeigen(zusatzkosten_berechnen("vollpension", True, True, 1, 3))


tests_ausfuehren()