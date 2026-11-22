from suche import *


def tests_ausfuehren():
    print("Test: B0003")
    nummer_suche_und_anzeigen("B0003")
    print("Test: b0003 (klein geschrieben)")
    nummer_suche_und_anzeigen("b0003")
    print("Test: B9999 (gibt es nicht)")
    nummer_suche_und_anzeigen("B9999")
    print("Test: Müller")
    nachname_suche_und_anzeigen("Müller")
    print("Test: meier (klein geschrieben)")
    nachname_suche_und_anzeigen("meier")
    print("Test: Huber (gibt es nicht)")
    nachname_suche_und_anzeigen("Huber")


tests_ausfuehren()