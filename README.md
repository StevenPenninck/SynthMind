# SynthMind
A Python TUI application for managing synth devices stored in a SQLite database (in dutch)
<img width="527" height="192" alt="SynthMind1BW" src="https://github.com/user-attachments/assets/bd8c202e-6412-4433-824a-7789e8135cb7" />

## Installatie (tester/user)

```
powershell
git clone <repo-url>
cd <repo-map>
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH om de voorbeeldconfig te gebruiken
py main.py
<<<<<<< HEAD
=======
```
```
linux
git clone <repo-url>
cd <repo-map>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH
python main.py
```


Wanneer je kiest voor optie 5 – Export naar CSV, wordt er automatisch een CSV-bestand aangemaakt in de map /database/.

Als je wel een bestandsnaam invoert, wordt het bestand opgeslagen als:
/database/<bestandsnaam>.csv

Als er geen bestandsnaam wordt ingevoerd (alleen op Enter drukt), wordt het bestand automatisch synths.csv genoemd:
/database/synths.csv



Created as part of the [Micro Degree program in Infrastructure/Cybersecurity](https://www.vives.be/nl/handelswetenschappen-en-bedrijfskunde/microdegree-cybersecurity-infrastructure-via) at Vives Kortrijk.


