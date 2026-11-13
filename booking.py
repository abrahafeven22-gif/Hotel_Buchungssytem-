from datetime import datetime

def enter_booking():
    print("willkommen bei der Hotelbuchung!")
    gast_name = input("wie heisst der Gast?")
    print("Der Gast heisst:", gast_name)
    anzahl_erwachsene = int(input("wie viele Erwachsene übernachten?"))
    anzahl_kinder = int(input("Wie viele Kinder übernachten?"))
    anzahl_personen = anzahl_erwachsene + anzahl_kinder
    print("Gesamtanzahl der Gäste:", anzahl_personen)
    check_in = input("Wann möchte der Gast einchecken? (TT.MM.JJJJ): ")
    check_out = input("Wann möchte der Gast auschecken? (TT.MM.JJJJ): ")

def check_availability():
    pass
def calculate_booking_cost():
    pass
def change_booking():
    pass
def cancel_booking():
    pass
