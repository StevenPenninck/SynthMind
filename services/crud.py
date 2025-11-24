#CLI menu om CRUD statements uit te voeren

import sys
from services.database import get_connection
from models.synths import Synth, Eigenschap,eigenschap_from_row

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


# Toon alle eigenschappen (namen) die horen bij een geselecteerde synth.
def toon_eigenschappen_van_synth():
    synth_id = _prompt_int("Geef het Id van de synth: ")
    conn = get_connection()
    try:
        cursor = conn.execute(
            "SELECT Id, synthId, naam FROM Eigenschappen WHERE synthId = ? ORDER BY naam",
            (synth_id,),
        )
        rows = cursor.fetchall()
        # Meld wanneer er geen eigenschappen zijn
        if not rows:
            print("Geen eigenschappen gevonden voor deze synth.")
            return
        print("Naam")
        for r in rows:
            e = eigenschap_from_row(r)
            print(f"{e.naam}")
    finally:
        conn.close()


# Voeg een eigenschap toe aan een synth. Als de eigenschap al bestaat, optie om de naam te wijzigen.
def voeg_eigenschap_toe():
    print("Eigenschap toevoegen")
    synth_id = _prompt_int("Synth Id: ")
    naam = input("Eigenschap naam: ").strip()
    conn = get_connection()
    try:
        # Controle: bestaat deze eigenschap al voor deze synth?
        row = conn.execute(
            "SELECT Id FROM Eigenschappen WHERE synthId = ? AND naam = ?",
            (synth_id, naam),
        ).fetchone()
        if row:
            print("Eigenschap bestaat al voor deze synth.")
            keuze = input("Wil je de naam wijzigen? (j/n): ").strip().lower()
            if keuze == 'j':
                nieuwe_naam = input("Nieuwe eigenschap naam: ").strip()
                if nieuwe_naam:
                    conn.execute(
                        "UPDATE Eigenschappen SET naam = ? WHERE Id = ?",
                        (nieuwe_naam, row[0]),
                    )
                    conn.commit()
                    print("Eigenschapnaam bijgewerkt.")
                else:
                    print("Geen wijziging doorgevoerd (lege naam).")
            else:
                print("Geen wijziging doorgevoerd.")
        else:
            # Nog niet bestaand: invoegen
            eig = Eigenschap(id=None, synth_id=synth_id, naam=naam)
            conn.execute(
                "INSERT INTO Eigenschappen (synthId, naam) VALUES (?, ?)",
                eig.insert_params(),
            )
            conn.commit()
            print("Eigenschap toegevoegd.")
    finally:
        conn.close()

<<<<<<< HEAD
=======
# Exporteer alle synths naar een CSV-bestand (met ';' als delimiter, geschikt voor EU-Excel).
def exporteer_synths_naar_csv():
    pad = input("Bestandsnaam voor export (bv. synths.csv): ").strip() or "synths.csv"
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT s.Id,
                   s.naam,
                   s.merk,
                   s.prijs,
                   s.uitgavejaar,
                   GROUP_CONCAT(e.naam, ' | ') AS eigenschappen
            FROM Synth s
            LEFT JOIN Eigenschappen e ON e.synthId = s.Id
            GROUP BY s.Id, s.naam, s.merk, s.prijs, s.uitgavejaar
            ORDER BY s.Id ASC
            """
        ).fetchall()
        # Bouw volledig pad binnen de geconfigureerde db_path
        full_path = os.path.join(db_path, pad)
        # Zorg dat de map bestaat voor we wegschrijven
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", newline="") as f:
            # Gebruik ';' als scheidingsteken omdat Excel in veel EU-locales
            # Hierdoor worden kolommen correct opgesplitst in Excel.
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Id", "Naam", "Merk", "Prijs", "Uitgavejaar", "Eigenschappen"])
            for r in rows:
                id_, naam, merk, prijs, jaar, eig = r
                writer.writerow([id_, naam, merk, prijs, jaar, eig or ""])
        print(f"{len(rows)} synth(s) geëxporteerd naar {full_path}.")
    finally:
        conn.close()
>>>>>>> 8efc0a5 (toevoeging CSV conversie)

# Sluit het programma af.
def programma_verlaten():
    sys.exit(0)


# Simpel CLI-menu om functionaliteiten aan te roepen op basis van keuze 1..5.
def menu():
    while True:
        print(
            """
1. Toon alle synths
2. Voeg een synth toe
3. Toon eigenschappen van een synth
4. Voeg of wijzig een eigenschap
5. Verlaat het programma
"""
        )
        try:
            # Parseer keuze en stuur door naar de juiste functie
            keuze = int(input("Geef het nummer van je keuze: "))
        except ValueError:
            print("Je moet een geheel getal van 1 tot 5 ingeven.")
            continue

        if keuze == 1:
            toon_alle_synths()
        elif keuze == 2:
            voeg_synth_toe()
        elif keuze == 3:
            toon_eigenschappen_van_synth()
        elif keuze == 4:
            voeg_eigenschap_toe()
        elif keuze == 5:
            programma_verlaten()
        else:
            print("Je moet een getal van 1 tot 5 ingeven.")
