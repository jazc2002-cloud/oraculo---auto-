import requests, json, os, sys

API_KEY = os.getenv("ODDS_API_KEY")
if not API_KEY:
    print("No hay API_KEY"); sys.exit(0)

SPORT = "soccer_mexico_ligamx"
URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={API_KEY}&regions=us&markets=h2h&oddsFormat=decimal"

print(f"Key termina en:...{API_KEY[-4:]}")
r = requests.get(URL)
print(f"Status: {r.status_code}")

data = r.json()

if isinstance(data, dict):
    print(f"Error API: {data}")
    sys.exit(0)

print(f"API trajo {len(data)} juegos")
lista = []
for g in data:
    fecha = g.get("commence_time","")[:10]
    local = g.get("home_team","")
    visita = g.get("away_team","")
    try:
        price = g["bookmakers"][0]["markets"][0]["outcomes"][0]["price"]
        conf = max(55, min(85, int(50 + (2.5-price)*10)))
    except:
        conf = 60
    lista.append({"fecha": fecha, "local": local, "visita": visita, "conf": conf})

with open("data.json", "w") as f:
    json.dump(lista, f, indent=2)
print("data.json actualizado")
