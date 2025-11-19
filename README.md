# SynthMind
A Python TUI application for managing synth devices stored in a SQLite database (in dutch)


## Installatie (tester/user)

```powershell
git clone <repo-url>
cd <repo-map>
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH
py main.py