
#CLI menu om CRUD statements uit te voeren

import sys

from services.database import get_connection

from models.synths import Synth

# Hulpfunctie: vraag steeds om een geheel getal en blijf herhalen tot de invoer correct is.
def _prompt_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Geef een geheel getal aub.")


# Toon alle synths uit de database met basisvelden, ascending op Id.
def toon_alle_synths():
    conn = get_connection()
    try:
        cursor = conn.execute(
            "SELECT Id, naam, merk, prijs, uitgavejaar FROM Synth ORDER BY Id ASC"
        )
        rows = cursor.fetchall()
        # wanneer geen resultaten gevonden:
        if not rows:
            print("Geen synths gevonden.")
            return
        # Header en per rij netjes afdrukken; None-waarden leeg tonen
        print("Id | Naam | Merk | Prijs | Uitgavejaar")
        for r in rows:
            id_, naam, merk, prijs, jaar = r
            if prijs is None:
                prijs = ""
            if jaar is None:
                jaar = ""
            print(f"{id_} | {naam} | {merk} | {prijs} | {jaar}")
    finally:
        # Altijd verbinding sluiten
        conn.close()


# Voeg een nieuwe synth toe op basis van gebruikersinvoer.
def voeg_synth_toe():
    print("Nieuwe synth toevoegen")
    naam = input("Naam: ").strip()  # whitespaces verwijderen
    merk = input("Merk: ").strip()
    prijs_str = input("Prijs (geheel getal, leeg laten indien onbekend): ").strip()
    jaar_str = input("Uitgavejaar (geheel getal, leeg laten indien onbekend): ").strip()

    # Converteer lege invoer naar None zodat de DB NULL krijgt
    prijs = int(prijs_str) if prijs_str else None
    jaar = int(jaar_str) if jaar_str else None

    conn = get_connection()
    try:
        # Maak een Synth-model en voer de insert uit
        nieuw = Synth(id=None, naam=naam, merk=merk, prijs=prijs, uitgavejaar=jaar)
        conn.execute(
            "INSERT INTO Synth (naam, merk, prijs, uitgavejaar) VALUES (?, ?, ?, ?)",
            nieuw.insert_params(),
        )
        conn.commit()
        print("Synth toegevoegd.")
    finally:
        conn.close()
        
# Sluit het programma netjes af.
def programma_verlaten():
    sys.exit(0)
    
    
# Simpel CLI-menu om functionaliteiten aan te roepen op basis van keuze 1..3.
def menu():
    while True:
        print(
            """
1. Toon alle synths
2. Voeg een synth toe
3. Verlaat het programma
"""
        )
        try:
            #lees ingevoerde keuze en stuur door naar de juiste functie
            keuze = int(input("Geef het nummer van je keuze: "))
        except ValueError:
            print("Je moet een geheel getal van 1 tot 3 ingeven.")
            continue

        if keuze == 1:
            toon_alle_synths()
        elif keuze == 2:
            voeg_synth_toe()

        elif keuze == 3:
            programma_verlaten()
        else:
            print("Je moet een getal van 1 tot 3 ingeven.")

        