import requests, json, os
API_KEY = os.getenv("ODDS_API_KEY")
URL = f"https://api.the-odds-api.com/v4/sports/soccer_mexico_ligamx/odds/?apiKey={API_KEY}&regions=us,eu,mx,uk&markets=h2h&oddsFormat=decimal"
r = requests.get(URL)
data = r.json()
if isinstance(data, dict):
    print(f"Error: {data}"); exit(0)
lista = []
for g in data:
    fecha = g.get("commence_time","")[:10]
    local = g.get("home_team","")
    visita = g.get("away_team","")
    try:
        momio = g["bookmakers"][0]["markets"][0]["outcomes"][0]["price"]
        conf = int(50 + (2.5 - momio)*10)
        conf = max(55, min(conf, 85))
    except:
        conf = 60
    titulo = f"{fecha} - {local} vs {visita} LIGA MX REAL"
    detalle = f"{local} {fecha} REAL ODDS"
    lista.append([g["id"], titulo, "MX REAL", local, visita, detalle, conf])
print(f"Listo {len(lista)} partidos")
with open("data.json","w",encoding="utf-8") as f:
    json.dump(lista, f, indent=2, ensure_ascii=False)
