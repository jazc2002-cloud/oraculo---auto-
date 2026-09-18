import requests
import json
import os

API_KEY = os.getenv("ODDS_API_KEY")
SPORT = "soccer_mexico_ligamx"

URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={API_KEY}&regions=us,eu,mx,uk&markets=h2h&oddsFormat=decimal"

print("Jalando momios reales...")
r = requests.get(URL)
data = r.json()

if isinstance(data, dict) and "message" in data:
    print(f"Error API: {data}")
else:
    print(f"Listo! {len(data)} partidos reales encontrados")
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
