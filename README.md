# SynthMind
A Python TUI application for managing synth devices stored in a SQLite database (in dutch)
<img width="527" height="192" alt="SynthMind1BW" src="https://github.com/user-attachments/assets/bd8c202e-6412-4433-824a-7789e8135cb7" />

## Installatie (tester/user)

```powershell
git clone <repo-url>
cd <repo-map>
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# kopieer .env.example naar .env en vul DB_DATABASE/DATABASE_PATH
py main.py
