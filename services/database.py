import sqlite3
import os
from config.config import db_database, db_path


def get_connection():
    full_db_path = os.path.join(db_path, db_database)  # volledig pad naar het DB-bestand
    os.makedirs(os.path.dirname(full_db_path), exist_ok=True)  # zorg dat de map bestaat
    is_new_db = not os.path.exists(full_db_path)  # check of de DB nieuw is (bestand nog niet aanwezig)

    # Connectie naar database. Deze wordt gecreëerd wanneer onbestaande.
    conn = sqlite3.connect(full_db_path)
    # Creëer Tables wanneer DB niet aanwezig
    if is_new_db:
        initialize_database(conn)

    return conn


def initialize_database(conn):
    # Maakt tabellen aan als ze nog niet bestaan 
    cursor = conn.cursor()
    # cursor.executescript() kan meerdere SQL-statements uitvoeren --> aanmaken 2 tabellen
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS Synth (
            Id INTEGER PRIMARY KEY,
            naam TEXT NOT NULL,
            merk TEXT NOT NULL,
            prijs INTEGER,
            uitgavejaar INTEGER
        );

        CREATE TABLE IF NOT EXISTS Eigenschappen (
            Id INTEGER PRIMARY KEY,
            synthId INTEGER NOT NULL,
            naam TEXT NOT NULL,
            FOREIGN KEY (synthId) REFERENCES Synth(Id)
        );
        """
    )
    conn.commit()  #conn.commit() schrijft de wijzingen naar de database
