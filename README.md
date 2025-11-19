# SynthMind
A Python TUI application for managing synth devices stored in a SQLite database (in dutch)
<img width="567" height="378" alt="SynthMind1BW" src="https://github.com/user-attachments/assets/63af5166-19b7-459d-be25-ca640c5ee830" />

## Installatie (tester/user)

```powershell
git clone <repo-url>
cd <repo-map>
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH
py main.py
