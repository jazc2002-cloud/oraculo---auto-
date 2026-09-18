import requests
import json
import os

API_KEY = os.getenv("ODDS_API_KEY")
SPORT = "soccer_mexico_ligamx"
URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={API_KEY}&regions=us,eu,uk,au&markets=h2h&oddsFormat=decimal"

r = requests.get(URL)
data = r.json()

bonito = []
for m in data:
    book = m.get("bookmakers", [{}])[0]
    outcomes = book.get("markets", [{}])[0].get("outcomes", [])
    # sacar momios
    local = next((o["price"] for o in outcomes if o["name"] == m["home_team"]), 0)
    visita = next((o["price"] for o in outcomes if o["name"] == m["away_team"]), 0)
    empate = next((o["price"] for o in outcomes if o["name"] == "Draw"), 0)

    bonito.append({
        "liga": m.get("sport_title"),
        "partido": f'{m["home_team"]} vs {m["away_team"]}',
        "hora": m.get("commence_time"),
        "local": local,
        "empate": empate,
        "visita": visita,
        "bookie": book.get("title", "real")
    })

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(bonito, f, indent=2, ensure_ascii=False)

print(f"Listo! {len(bonito)} partidos reales guardados")
