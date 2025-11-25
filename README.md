# SynthMind
A Python TUI application for managing synth devices stored in a SQLite database (in dutch)
<img width="527" height="192" alt="SynthMind1BW" src="https://github.com/user-attachments/assets/bd8c202e-6412-4433-824a-7789e8135cb7" />

## Vereisten

- Python 3.11 of hoger geïnstalleerd
- Maak een `.env` aan op basis van `.env.example` (vul `DB_DATABASE` en `DATABASE_PATH` in) in \config\ .env
<img width="501" height="102" alt="example_env" src="https://github.com/user-attachments/assets/aea330ed-de39-44e0-9f19-658bd6bcdb0e" />


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
### Voorbeeld Database

Database wordt automatisch aangemaakt bij het kiezen van een optie in het menu.

<img width="347" height="233" alt="example_db_synths" src="https://github.com/user-attachments/assets/7161317f-adc6-4fcc-8485-a655d1b2fab0" />
<img width="374" height="181" alt="example_db_eigenschappen" src="https://github.com/user-attachments/assets/a5c30b32-e1df-4bc0-8bac-7d20a96e5996" />

### CSV Export

Wanneer je kiest voor optie 5 in het menu – Export naar CSV, wordt er een CSV-bestand aangemaakt in de map die je instelt via `DATABASE_PATH` (bv. `./database`).

<img width="782" height="246" alt="image" src="https://github.com/user-attachments/assets/fa83e7fe-7339-4303-b45b-366f96402844" />


Als je een bestandsnaam invoert, wordt het bestand opgeslagen als:
`<DATABASE_PATH>/<bestandsnaam>.csv`

Als er geen bestandsnaam wordt ingevoerd (alleen op Enter drukt), wordt het bestand automatisch `synths.csv` genoemd:
`<DATABASE_PATH>/synths.csv`

<img width="763" height="218" alt="example_csv" src="https://github.com/user-attachments/assets/8d8aca3b-3852-408c-bdb0-a1935f1c1af8" />




--------------------------------------------------------------------
Created as part of the [Micro Degree program in Infrastructure/Cybersecurity](https://www.vives.be/nl/handelswetenschappen-en-bedrijfskunde/microdegree-cybersecurity-infrastructure-via) at Vives Kortrijk.


