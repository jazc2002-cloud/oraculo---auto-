import requests
import json
import os

API_KEY = os.getenv("ODDS_API_KEY") or "2b6a83e8d8e4b1e8b8e4b1e8b8e4b1e8b8e4b1e8b8e4b1e8" # pon aquí tu key nueva si quieres
SPORT = "soccer_mexico_ligamx"
URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={API_KEY}&regions=us,eu,mx&markets=h2h&oddsFormat=decimal"

r = requests.get(URL)
data = r.json()

# Guardamos solo lo necesario para tu formato
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Listo! {len(data)} partidos guardados")
