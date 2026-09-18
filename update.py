import requests, json, os, sys
API_KEY = os.getenv("ODDS_API_KEY")
if not API_KEY:
    print("No hay API_KEY"); sys.exit(0)

URL = f"https://api.the-odds-api.com/v4/sports/soccer_mexico_ligamx/odds/?apiKey={API_KEY}&regions=us,eu,mx,uk&markets=h2h&oddsFormat=decimal"
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
    titulo = f"{fecha} - {local} vs {visita} LIGA MX REAL"
    detalle = f"{local} REAL ODDS {fecha}"
    lista.append([g["id"], titulo, "MX REAL", local, visita, detalle, conf])

# si no hay juegos hoy, no borres el viejo
if len(lista) == 0:
    print("No hay juegos, no sobreescribo")
    sys.exit(0)

with open("data.json","w",encoding="utf-8") as f:
    json.dump(lista, f, indent=2, ensure_ascii=False)
print("data.json actualizado")
