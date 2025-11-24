# SynthMind
A Python TUI application for managing synth devices stored in a SQLite database (in dutch)
<img width="527" height="192" alt="SynthMind1BW" src="https://github.com/user-attachments/assets/bd8c202e-6412-4433-824a-7789e8135cb7" />

## Vereisten

- Python 3.11 of hoger geïnstalleerd
- Maak een `.env` aan op basis van `.env.example` (vul `DB_DATABASE` en `DATABASE_PATH` in)

## Installatie (tester/user)

### Windows (PowerShell)
```powershell
git clone <repo-url>
cd <repo-map>
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH om de voorbeeldconfig te gebruiken
py main.py
```

### Windows (CMD)
```cmd
git clone <repo-url>
cd <repo-map>
py -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH om de voorbeeldconfig te gebruiken
py main.py
```

### Linux/macOS
```bash
git clone <repo-url>
cd <repo-map>
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH
python main.py
```

### CSV Export

Wanneer je kiest voor optie 5 in het menu – Export naar CSV, wordt er een CSV-bestand aangemaakt in de map die je instelt via `DATABASE_PATH` (bv. `./database`).

Als je een bestandsnaam invoert, wordt het bestand opgeslagen als:
`<DATABASE_PATH>/<bestandsnaam>.csv`

Als er geen bestandsnaam wordt ingevoerd (alleen op Enter drukt), wordt het bestand automatisch `synths.csv` genoemd:
`<DATABASE_PATH>/synths.csv`

### Voorbeeld Database



--------------------------------------------------------------------
Created as part of the [Micro Degree program in Infrastructure/Cybersecurity](https://www.vives.be/nl/handelswetenschappen-en-bedrijfskunde/microdegree-cybersecurity-infrastructure-via) at Vives Kortrijk.


