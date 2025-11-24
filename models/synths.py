class Synth:
    
    """
    Deze klasse stelt één rij uit de tabel "Synth" voor.
    Het doel is ruwe database-data (tuples) om te zetten naar objecten,
    en vanuit objecten weer makkelijk waarden te geven voor SQL-statements.
    """
    #Constructor van de klasse. Hiermee maken we een nieuw Synth-object aan.
    #De parameters hebben standaardwaardes zodat je ook met minder info kan starten.
    
    def __init__(self, id=None, naam="", merk="", prijs=None, uitgavejaar=None):
        self.id = id                # Unieke sleutel uit de database (INTEGER PRIMARY KEY)
        self.naam = naam            # Naam van de synthesizer (bv. "SoftPop")
        self.merk = merk            # Merk/fabrikant (bv. "Bastl")
        self.prijs = prijs          # Prijs in hele euro's (mag ook None zijn als onbekend)
        self.uitgavejaar = uitgavejaar  # Jaar van uitgave (mag ook None zijn als onbekend)


    def insert_params(self):
        # Geeft een tuple terug met waarden in de juiste volgorde voor een INSERT-query.
        # Deze volgorde moet overeenkomen met de kolommen in SQL:
        #   INSERT INTO Synth (naam, merk, prijs, uitgavejaar) VALUES (?, ?, ?, ?)
        # Zo kan er makkelijk parametrized queries gebruiken zonder handmatig strings te bouwen.
        return (self.naam, self.merk, self.prijs, self.uitgavejaar)

    def __str__(self):
        # Handige voor debug/print: toont velden in één regel.
        return f"Synth(id={self.id}, naam='{self.naam}', merk='{self.merk}', prijs={self.prijs}, uitgavejaar={self.uitgavejaar})"


class Eigenschap:
    """
    Deze klasse stelt één rij uit de tabel "Eigenschappen" voor.
    Elke eigenschap is gekoppeld aan precies één synth via het veld "synthId".
    """
    def __init__(self, id=None, synth_id=0, naam=""):
        self.id = id              # Unieke sleutel uit de database (INTEGER PRIMARY KEY)
        self.synth_id = synth_id  # Verwijzing naar Synth.Id (FOREIGN KEY)
        self.naam = naam          # Naam van de eigenschap (bv. "Analoge filter")


    def insert_params(self):
        # Geeft de waarden terug in dezelfde volgorde als de kolommen in de INSERT.
        #   INSERT INTO Eigenschappen (synthId, naam) VALUES (?, ?)
        return (self.synth_id, self.naam)

    def __str__(self):
        # Handige debug/print: toont de velden in één regel.
        return f"Eigenschap(id={self.id}, synth_id={self.synth_id}, naam='{self.naam}')"


# Eenvoudige helperfuncties om tuples naar objecten om te zetten

def eigenschap_from_row(row):
    # Volgorde verwacht: Id, synthId, naam
    return Eigenschap(
        id=row[0],
        synth_id=row[1],
        naam=row[2],
    )
<<<<<<< HEAD
    
=======

""" evt voor toekomstig gebruik :
def synth_from_row(row):
    # Volgorde verwacht: Id, naam, merk, prijs, uitgavejaar
    return Synth(
        id=row[0],
        naam=row[1],
        merk=row[2],
        prijs=row[3],
        uitgavejaar=row[4],
    )
"""    

>>>>>>> 8efc0a5 (toevoeging CSV conversie)
if __name__ == "__main__":
    # Klein voorbeeld om te tonen hoe de klassen gebruikt worden of om te testen.
    # Dit wordt alleen uitgevoerd als je dit bestand direct runt (py synths.py in de directory /models),
    # niet als het geïmporteerd wordt vanuit andere modules.
    s = Synth(id=None, naam="SoftPop", merk="Bastl", prijs=300, uitgavejaar=2017)
    print(s)
    print("INSERT params:", s.insert_params())
    e = Eigenschap(id=None, synth_id=1, naam="Experimenteel/Modulair")
    print(e)
    print("INSERT params:", e.insert_params())