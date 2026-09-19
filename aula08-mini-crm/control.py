from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREAT / READ / UPDATE / DELETE

# READ
def read_leads():
    return json.loads(DB_PATH.read_text(encoding="utf-8")) # desafio: try/except

# CREAT
def create_lead(lead_dict):
    leads = read_leads() #DESAFIO... resolver como ele nao reescreve todos os usuarios de novo, ao criar um novo usuario
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")