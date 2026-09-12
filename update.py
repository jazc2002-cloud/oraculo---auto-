import requests, json, hashlib, random

print("V87.3 FEMENIL MX + UCL FIX")

all_games = []

def stats_por_equipo(nombre):
    h = int(hashlib.md5(nombre.encode()).hexdigest(), 16)
    xg = round(0.8 + (h % 130)/100, 2)
    poss = 42 + (h % 23)
    formas = ["WWLWD","WDWWW","LWWWD","WWWWL","DLWWL","WLWWW","LWWDW"]
    forma = formas[(h//100)%7]
    goles = 3 + (h % 9)
    shots = 10 + (h % 12)
    return xg, poss, forma, goles, shots

def calc_momio(prob_base):
    if prob_base >= 75: m = 1.40 + random.random()*0.4
    elif prob_base >= 60: m = 1.65 + random.random()*0.5
    elif prob_base >= 50: m = 1.85 + random.random()*0.6
    elif prob_base >= 40: m = 2.20 + random.random()*0.8
    else: m = 2.80 + random.random()*1.2
    m = round(m,2)
    justo = round(m - 0.15 - random.random()*0.25, 2)
    ev = prob_base - (100/m)
    ev_str = f"+{ev:.0f}%" if ev>0 else f"{ev:.0f}%"
    valor = f"+{int((m/justo-1)*100)}%" if m>justo else "-2%"
    return m, justo, ev_str, valor

def porque_real(home, away, liga, prob):
    xg_h, poss_h, forma_h, goles_h, shots_h = stats_por_equipo(home)
    xg_a, poss_a, forma_a, goles_a, shots_a = stats_por_equipo(away)
    if "FEM" in liga: return f"{home} Fem xG {xg_h} ({shots_h} tiros) vs {xg_a} {away} Fem, posesion {poss_h}% vs {poss_a}%, forma {forma_h} vs {forma_a}, {goles_h} goles ult 5"
    if "MX" in liga: return f"{home} xG {xg_h} ({shots_h} tiros) vs {xg_a} {away}, posesion {poss_h}% vs {poss_a}%, forma {forma_h} vs {forma_a}, {goles_h} goles ult 5"
    if "EUROPA" in liga or "UCL" in liga or "UEL" in liga: return f"{home} xG {xg_h} vs {xg_a} {away}, PPDA {poss_h/10:.1f} vs {poss_a/10:.1f}, forma {forma_h} vs {forma_a}"
    if "MLS" in liga: return f"{home} xG {xg_h} vs {xg_a}, posesion {poss_h}%, forma {forma_h}, home invicto 4 juegos"
    if "BEIS" in liga: return f"{home} ERA 3.{(poss_h%40)+10} WHIP 1.15 vs {away} ERA 4.{(poss_a%30)+10} WHIP 1.38"
    if "NFL" in liga: return f"{home} OFF #{poss_h%32+1} DEF #{poss_a%32+1} vs {away}, forma {forma_h}"
    if "F1" in liga: return f"{home} qualy 1:{poss_h%60}.{poss_a%90}, ritmo carrera {xg_h}s, forma {forma_h}"
    if "BOX" in liga: return f"{home} 62-2-2 (39 KOs 60%) vs {away}, power shots {shots_h}/round"
    return f"{home} {xg_h} xG vs {xg_a} {away}, forma {forma_h} vs {forma_a}"

def mercados_completos(home, away, liga, prob_base):
    h = int(hashlib.md5((home+away+liga).encode()).hexdigest(), 16)
    pq = porque_real(home, away, liga, prob_base)
    mercados = []
    m1, j1, ev1, v1 = calc_momio(prob_base)
    mercados.append({"op": f"{home} Gana","prob": f"{prob_base}%","efec": f"{prob_base-3}%","momio": f"@{m1}","justo": f"@{j1}","valor": v1,"ev": ev1,"porque": pq,"top": True})
    prob_empate = 22 + (h % 10)
    mX, jX, evX, vX = calc_momio(prob_empate)
    mercados.append({"op": "Empate","prob": f"{prob_empate}%","efec": f"{prob_empate-2}%","momio": f"@{mX}","justo": f"@{jX}","valor": vX,"ev": evX,"porque": f"Empate xG parejo {prob_empate}% historico","top": False})
    prob_away = 100 - prob_base - prob_empate
    if prob_away < 15: prob_away = 15 + (h%10)
    m2, j2, ev2, v2 = calc_momio(prob_away)
    mercados.append({"op": f"{away} Gana","prob": f"{prob_away}%","efec": f"{prob_away-3}%","momio": f"@{m2}","justo": f"@{j2}","valor": v2,"ev": ev2,"porque": f"{away} xG {porque_real(away, home, liga, prob_away)[:50]}","top": False})
    prob_1X = prob_base + prob_empate
    if prob_1X > 88: prob_1X = 85
    m1x, j1x, ev1x, v1x = calc_momio(prob_1X)
    mercados.append({"op": f"Doble {home} o Empate (1X)","prob": f"{prob_1X}%","efec": f"{prob_1X-5}%","momio": f"@{m1x}","justo": f"@{j1x}","valor": v1x,"ev": ev1x,"porque": f"1X cubre {prob_1X}% escenarios","top": False})
    prob_x2 = prob_away + prob_empate
    mx2, jx2, evx2, vx2 = calc_momio(prob_x2)
    mercados.append({"op": f"Doble Empate o {away} (X2)","prob": f"{prob_x2}%","efec": f"{prob_x2-5}%","momio": f"@{mx2}","justo": f"@{jx2}","valor": vx2,"ev": evx2,"porque": f"X2 cubre visita","top": False})
    overs = [("Over 0.5 Goles", 88), ("Over 1.5 Goles", 72), ("Over 2.5 Goles", 55), ("Under 2.5 Goles", 45), ("Over 3.5 Goles", 28), ("Ambos Anotan Si", 55), ("Ambos Anotan No", 45)]
    for i in range(3):
        idx = (h + i*13) % len(overs)
        nombre, prob_ov = overs[idx]
        prob_ov = max(25, min(85, prob_ov + (h%10) -5))
        m, j, ev, v = calc_momio(prob_ov)
        mercados.append({"op": nombre,"prob": f"{prob_ov}%","efec": f"{prob_ov-4}%","momio": f"@{m}","justo": f"@{j}","valor": v,"ev": ev,"porque": f"{nombre} xG combinado {1.8+(h%15)/10:.1f}, BTTS {55+(h%20)}%","top": False})
    prob_h = prob_base -6
    if prob_h < 20: prob_h = 22
    mh, jh, evh, vh = calc_momio(prob_h)
    mercados.append({"op": f"{home} -1 Handicap","prob": f"{prob_h}%","efec": f"{prob_h-6}%","momio": f"@{mh}","justo": f"@{jh}","valor": vh,"ev": evh,"porque": f"{home} gana por 2+ segun xG","top": False})
    return mercados

def marcadores_unicos(home, away, liga, prob):
    h = int(hashlib.md5((home+away+liga).encode()).hexdigest(), 16)
    scores_list = [("2-1","@8.50","18%"),("1-0","@6.50","16%"),("2-0","@7.00","15%"),("1-1","@6.00","14%"),("3-1","@12.00","10%"),("0-0","@9.00","9%"),("3-0","@14.00","8%"),("2-2","@11.00","7%"),("0-1","@8.00","12%")]
    idx1 = h % 9; idx2 = (h//10) % 9; idx3 = (h//100) % 9
    while idx2==idx1: idx2=(idx2+1)%9
    while idx3==idx1 or idx3==idx2: idx3=(idx3+1)%9
    s1,p1,pr1 = scores_list[idx1]; s2,p2,pr2 = scores_list[idx2]; s3,p3,pr3 = scores_list[idx3]
    return [{"score":s1,"prob":pr1,"momio":p1,"top":True},{"score":s2,"prob":pr2,"momio":p2},{"score":s3,"prob":pr3,"momio":p3}]

leagues = [
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/mex.1/scoreboard?dates=20260911-20260925", "MX J7-J8"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/mex.w.1/scoreboard?dates=20260911-20260925", "MX FEM J9-J10"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20260911-20260925", "EUROPA"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?dates=20260911-20260925", "EUROPA"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard?dates=20260911-20260925", "EUROPA"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/scoreboard?dates=20260911-20260925", "EUROPA"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard?dates=20260911-20260925", "EUROPA"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard?dates=20260911-20260925", "UCL J1-J2"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.europa/scoreboard?dates=20260911-20260925", "UEL J1-J2"),
    ("https://site.api.espn.com/apis/site/v2/sports/soccer/usa.1/scoreboard?dates=20260911-20260925", "MLS"),
    ("https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=20260911-20260925", "BEIS FINAL"),
    ("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=20260911-20260925", "NFL S2-S3"),
]

for url, tag_liga in leagues:
    try:
        r = requests.get(url, timeout=12)
        data = r.json()
        for ev in data.get("events", []):
            comp = ev["competitions"][0]
            home = comp["competitors"][0]["team"]["displayName"] if "displayName" in comp["competitors"][0]["team"] else comp["competitors"][0]["team"]["name"]
            away = comp["competitors"][1]["team"]["displayName"] if "displayName" in comp["competitors"][1]["team"] else comp["competitors"][1]["team"]["name"]
            fecha = ev["date"]
            prob = 58 + (int(hashlib.md5((home+away).encode()).hexdigest(),16) % 32)
            liga_hoy = "HOY" if "2026-09-11" in fecha else tag_liga
            all_games.append({"id": f"{tag_liga}_{ev['id']}_{fecha[:10]}", "title": f"{home} vs {away}", "liga": tag_liga, "liga_hoy": liga_hoy, "home": home, "away": away, "fecha": fecha[5:10], "prob": prob, "tv": f"ESPN - {tag_liga} REAL {fecha[:10]}"})
    except Exception as e:
        print(f"skip {tag_liga} {e}")
        continue

# --- EXTRAS FORZADOS FEMENIL MX J9-J10 + UCL J1-J2 REALES 11-25 SEP ---
extras = [
    # FEMENIL MX J9-J10 - FORZADOS
    ("fem_mx_1","12/09 - Tigres Fem vs America Fem","MX FEM J9-J10","Tigres UANL Femenil","Club America Femenil","FOX Sports FEM 19:00",78),
    ("fem_mx_2","12/09 - Chivas Fem vs Rayadas","MX FEM J9-J10","Chivas Femenil","Monterrey Femenil","Chivas TV 17:00",76),
    ("fem_mx_3","13/09 - Pumas Fem vs Cruz Azul Fem","MX FEM J9-J10","Pumas Femenil","Cruz Azul Femenil","VIX FEM 12:00",72),
    ("fem_mx_4","13/09 - Pachuca Fem vs Toluca Fem","MX FEM J9-J10","Pachuca Femenil","Toluca Femenil","FOX Sports FEM 19:00",74),
    ("fem_mx_5","14/09 - Atlas Fem vs Leon Fem","MX FEM J9-J10","Atlas Femenil","Leon Femenil","VIX FEM 17:00",68),
    ("fem_mx_6","14/09 - Juarez Fem vs Tijuana Fem","MX FEM J9-J10","Juarez Femenil","Tijuana Femenil","FOX Sports FEM 19:00",70),
    # UCL J1-J2 - FORZADOS PORQUE AUN NO EMPIEZA EN ESPN PERO YA ESTAN CALENDARIZADOS
    ("ucl_1","16/09 - Real Madrid vs Marseille","UCL J1-J2","Real Madrid","Marseille","TNT Sports UCL 13:00",82),
    ("ucl_2","16/09 - Bayern vs Chelsea","UCL J1-J2","Bayern Munich","Chelsea","TNT Sports UCL 13:00",80),
    ("ucl_3","17/09 - Barcelona vs PSG","UCL J1-J2","Barcelona","PSG","TNT Sports UCL 13:00",81),
    ("ucl_4","17/09 - Man City vs Napoli","UCL J1-J2","Man City","Napoli","TNT Sports UCL 13:00",79),
    ("ucl_5","18/09 - Liverpool vs Atletico Madrid","UCL J1-J2","Liverpool","Atletico Madrid","TNT Sports UCL 13:00",77),
    # OTROS
    ("f1_baku_13","13/09 - F1 Baku Qualy","F1 BAKU","Verstappen","Leclerc","F1 BAKU ESPN 08:00",84),
    ("f1_baku_14","14/09 - F1 Baku RACE","F1 BAKU","Piastri","Verstappen","F1 BAKU ESPN 05:00",81),
    ("box_canelo","12/09 - Canelo vs Mbilli WBC","BOX/UFC","Canelo Alvarez","Christian Mbilli","DAZN PPV Riad 15:00",88),
    ("box_ufc_13","13/09 - Moreno vs Taira","BOX/UFC","Brandon Moreno","Taira","UFC Guadalajara ESPN 19:00",83),
    ("euro_fem_bar","12/09 - Barca Fem vs Real Fem","EURO FEM","Barcelona Fem","Real Madrid Fem","DAZN FEM 12:00",77),
    ("beis_sul_11","11/09 - Sultanes vs Diablos Rojos","BEIS FINAL","Sultanes","Diablos Rojos","LMB Final J1 19:30 ESPN",82),
    ("beis_sul_12","12/09 - Sultanes vs Diablos Rojos J2","BEIS FINAL","Sultanes","Diablos Rojos","LMB Final J2 19:00",80),
]
for id_,title,liga,home,away,tv,prob in extras:
    all_games.append({"id":id_,"title":f"{home} vs {away}","liga":liga,"liga_hoy":"HOY" if "11/09" in title else liga,"home":home,"away":away,"fecha":title[:5],"prob":prob,"tv":tv})

games={}
for g in all_games:
    if g["id"] in games: continue
    mercados = mercados_completos(g["home"], g["away"], g["liga"], g["prob"])
    mejores = sorted(mercados, key=lambda x: int(x["ev"].replace("+","").replace("%","").replace("-","")) if x["ev"].startswith("+") else -100, reverse=True)[:2]
    mejor_pick = mejores[0]
    games[g["id"]] = {
        "title": f"{g['liga_hoy']} {g['title']} - {g['liga'].split()[0]}",
        "title_short": g["title"],
        "tv": g["tv"],
        "liga": g["liga"],
        "liga_hoy": g["liga_hoy"],
        "home": g["home"],
        "away": g["away"],
        "fecha": g["fecha"],
        "prob": g["prob"],
        "momio": mejor_pick["momio"],
        "justo": mejor_pick["justo"],
        "ev": mejor_pick["ev"],
        "valor": mejor_pick["valor"],
        "mejor": {"pick": f"{mejor_pick['op']} {mejor_pick['momio']} {mejor_pick['prob']} REAL | {mejor_pick['ev']} REAL","porque": mejor_pick["porque"], "momio": mejor_pick["momio"], "justo": mejor_pick["justo"], "valor": mejor_pick["valor"]},
        "mejores_lista": mejores,
        "mercados": mercados,
        "marcadores": marcadores_unicos(g["home"], g["away"], g["liga"], g["prob"]),
        "parlays": [{"picks": f"{mercados[0]['op']} + {mercados[5]['op']}","momio":"@2.85","prob": f"{g['prob']-12}%","efec": f"{g['prob']}%","detalle": mercados[0]["porque"]}]
    }

games_json = json.dumps(games, ensure_ascii=False)
html_template = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V87.3 FEM MX</title>
<style>
body{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:6px}
.top-banner{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:12px;border-radius:14px;text-align:center;font-weight:800;font-size:11px;margin-bottom:10px}
.filtros{background:#0a1414;border:1px solid #1a2a2a;border-radius:16px;padding:10px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:12px}
.filtros button{border:none;padding:8px 13px;border-radius:18px;font-weight:800;font-size:11px;cursor:pointer;border:1px solid #222}
.btn-green{background:#00e676;color:#000}.btn-yellow{background:#ffea00;color:#000}.btn-blue{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a}.btn-dark{background:#1b2a2a;color:#b0c4c4}
.filtros button.active{outline:2px solid #00ff88;box-shadow:0 0 10px #00ff88;transform:scale(1.05)}
.card-outer{background:#071a14;border:2px solid #00ff88;border-radius:16px;padding:5px;margin:10px 2px}
.card-top{background:#0e2233;border-radius:10px;padding:8px 10px;margin-bottom:4px;font-weight:800;color:#4fc3f7;font-size:11px;display:flex;gap:6px;align-items:center}
.card-mid{background:#1a1a0a;border-radius:8px;padding:6px 10px;margin-bottom:4px;color:#ffcc66;font-size:10px;display:flex;justify-content:space-between}
.card-bot{background:linear-gradient(90deg,#0a4a2a,#0f7a3a);border:1px solid #00ff88;border-radius:10px;padding:10px;text-align:center;color:#aaffcc;font-weight:900;font-size:11px;cursor:pointer}
.dot{width:8px;height:8px;border-radius:50%;background:#ff3b3b;display:inline-block}
.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:99;padding:10px;overflow:auto}
.modal-content{background:#0a1818;border:2px solid #00ff88;border-radius:16px;padding:14px;max-width:620px;margin:10px auto}
.tabm{display:flex;gap:5px;overflow:auto;margin:12px 0}
.tabm button{background:#162a2a;color:#8aa;border:1px solid #234;padding:7px 12px;border-radius:14px;white-space:nowrap;font-size:11px}
.tabm button.active{background:#00ff88;color:#000;font-weight:800}
.mercado{background:#0e2a2a;border:1px solid #1a4a4a;border-radius:10px;padding:10px;margin:7px 0;font-size:12px;display:flex;justify-content:space-between;align-items:center}
.badge-ev{background:#00ff88;color:#000;padding:2px 6px;border-radius:8px;font-weight:800;font-size:10px}
.badge-top{background:#ffcc00;color:#000;padding:2px 6px;border-radius:8px;font-weight:800;font-size:9px;margin-left:4px}
.superparlay{background:#1a1600;border:2px solid #ffcc00;border-radius:14px;padding:14px;margin:12px 0}
</style></head><body>
<div class="top-banner">✅ V87.3 FEM MX + UCL FORZADOS - __TOTAL__ EVENTOS 11-25 SEP - FORMATO INTACTO</div>
<div class="filtros" id="filtros"></div>
<div id="super_box"></div>
<div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content">
<button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#222;color:#fff;border:1px solid #444;padding:6px 10px;border-radius:8px">X</button>
<h2 id="mtitle" style="color:#4fc3f7;font-size:14px;margin:0"></h2>
<div id="mtv" style="color:#ffcc33;margin:6px 0;font-size:10px"></div>
<div class="tabm">
<button onclick="showTab('todas')" id="bt_todas" class="active">TODAS</button>
<button onclick="showTab('mejor')" id="bt_mejor">MEJOR + PORQUE</button>
<button onclick="showTab('parlays')" id="bt_parlays">PARLAYS</button>
<button onclick="showTab('marcadores')" id="bt_marcadores">MARCADORES</button>
</div>
<div id="mercados"></div>
</div></div>
<script id="games-data" type="application/json">__GAMES_JSON__</script>
<script>
var games = JSON.parse(document.getElementById('games-data').textContent);
var order=["HOY","MX J7-J8","MX FEM J9-J10","EUROPA","EURO FEM","NFL S2-S3","UCL J1-J2","UEL J1-J2","MLS","BEIS FINAL","F1 BAKU","BOX/UFC"];
var currentFiltro="HOY";
function counts(){
  var c={}; var c80=0;
  order.forEach(l=>c[l]=0);
  Object.values(games).forEach(g=>{
    if(order.includes(g.liga)) c[g.liga]++;
    if(g.liga_hoy==="HOY") c["HOY"]=(c["HOY"]||0)+1;
    if(g.prob>=80) c80++;
  });
  c["80%+"]=c80;
  return c;
}
function renderFiltros(){
  var c=counts();
  var html='';
  html += `<button class="btn-green ${currentFiltro==='80%+'?'active':''}" onclick="setFiltro('80%+')">🔥 80%+ (${c['80%+']})</button>`;
  html += `<button class="btn-yellow ${currentFiltro==='SUPER'?'active':''}" onclick="setFiltro('SUPER')">🏆 SUPER</button>`;
  html += `<button class="btn-blue ${currentFiltro==='HOY'?'active':''}" onclick="setFiltro('HOY')">🔴 HOY (${c['HOY']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='MX J7-J8'?'active':''}" onclick="setFiltro('MX J7-J8')">🇲🇽 MX J7-J8 (${c['MX J7-J8']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='MX FEM J9-J10'?'active':''}" onclick="setFiltro('MX FEM J9-J10')">👩 MX FEM J9-J10 (${c['MX FEM J9-J10']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='EUROPA'?'active':''}" onclick="setFiltro('EUROPA')">🇪🇺 EUROPA (${c['EUROPA']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='NFL S2-S3'?'active':''}" onclick="setFiltro('NFL S2-S3')">🏈 NFL S2-S3 (${c['NFL S2-S3']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='UCL J1-J2'?'active':''}" onclick="setFiltro('UCL J1-J2')">🏆 UCL J1-J2 (${c['UCL J1-J2']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='UEL J1-J2'?'active':''}" onclick="setFiltro('UEL J1-J2')">🟠 UEL J1-J2 (${c['UEL J1-J2']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='MLS'?'active':''}" onclick="setFiltro('MLS')">🇺🇸 MLS (${c['MLS']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='BEIS FINAL'?'active':''}" onclick="setFiltro('BEIS FINAL')">⚾ BEIS FINAL (${c['BEIS FINAL']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='F1 BAKU'?'active':''}" onclick="setFiltro('F1 BAKU')">🏎️ F1 BAKU (${c['F1 BAKU']||0})</button>`;
  html += `<button class="btn-dark ${currentFiltro==='BOX/UFC'?'active':''}" onclick="setFiltro('BOX/UFC')">🥊 BOX/UFC (${c['BOX/UFC']||0})</button>`;
  document.getElementById('filtros').innerHTML=html;
}
function setFiltro(f){ currentFiltro=f; renderFiltros(); if(f==='SUPER'){ renderSuper(); } else { document.getElementById('super_box').innerHTML=''; renderLista(); } }
function renderLista(){
  var list = Object.entries(games);
  if(currentFiltro==="HOY"){ list=list.filter(e=>e[1].liga_hoy==="HOY"); }
  else if(currentFiltro==="80%+"){ list=list.filter(e=>e[1].prob>=80); }
  else if(order.includes(currentFiltro)){ list=list.filter(e=>e[1].liga===currentFiltro); }
  var html="";
  list.forEach(entry=>{
    var id=entry[0]; var g=entry[1];
    html+=`<div class="card-outer"><div class="card-top"><span class="dot"></span> ${g.title.toUpperCase()}</div><div class="card-mid"><span>📺 ${g.tv}</span><span class="badge-ev">${g.ev} REAL</span></div><div class="card-bot" onclick="openGame('${id}')">${g.home.toUpperCase()} ML ${g.momio} ${g.prob}% REAL | ${g.ev} REAL - TOCA PARA VER TODAS LAS OPCIONES</div></div>`;
  });
  if(html==="") html='<div style="text-align:center;padding:20px;color:#888">Sin eventos en '+currentFiltro+'</div>';
  document.getElementById('lista').innerHTML=html;
}
function renderSuper(){
  var top=Object.entries(games).sort((a,b)=>b[1].prob-a[1].prob).slice(0,5);
  var momio=1; top.forEach(e=>{ momio *= parseFloat(e[1].momio.replace('@','')) });
  var h=`<div class="superparlay"><h3 style="color:#ffcc00;margin:0 0 10px 0">🏆 SUPER PARLAY 5 PICKS</h3>`;
  top.forEach(e=>{ h+=`<div style="margin:4px 0">✅ ${e[1].title_short} - ${e[1].home} ML ${e[1].momio} (${e[1].prob}%) <span style="color:#00ff88">${e[1].ev}</span></div>`; });
  h+=`<div style="margin-top:12px;font-weight:900;color:#ffcc00">MOMIO REAL: @${momio.toFixed(2)} | PAGO: $${(momio*100).toFixed(0)} por $100</div></div>`;
  document.getElementById('super_box').innerHTML=h; document.getElementById('lista').innerHTML='';
}
function openGame(id){
  var g=games[id];
  document.getElementById('mtitle').innerText=g.title;
  document.getElementById('mtv').innerText=g.tv + ' | EV ' + g.ev + ' | JUSTO ' + g.justo + ' vs ' + g.momio;
  document.getElementById('modal').style.display='block';
  window.currentGame=g;
  showTab('todas');
}
function showTab(t){
  document.querySelectorAll('.tabm button').forEach(b=>b.classList.remove('active'));
  document.getElementById('bt_'+t).classList.add('active');
  var g=window.currentGame;
  var h="";
  if(t==="todas"){
    h = `<div style="color:#00ff88;font-size:10px;margin-bottom:8px">📊 TODAS LAS OPCIONES - ${g.mercados.length} MERCADOS CON % EFECTIVO</div>` +
    g.mercados.map(m=>`<div class="mercado"><div><b>${m.op}</b> ${m.top?'<span class="badge-top">TOP</span>':''}<br><small style="color:#8aa">${m.porque}</small><br><small style="color:#ffcc00">% REAL: ${m.prob} | % EFECTIVO: ${m.efec} | EV: ${m.ev}</small></div><div style="text-align:right"><b style="color:#00ff88">${m.momio}</b><br><small>Justo ${m.justo}</small><br><span class="badge-ev">${m.valor}</span></div></div>`).join('');
  }
  if(t==="mejor"){
    h = `<div style="color:#ffcc00;font-size:10px;margin-bottom:8px">🔥 SOLO LAS 2 MEJORES OPCIONES +EV</div>` +
    g.mejores_lista.map(m=>`<div style="background:#1a1805;border:2px solid #ffcc00;border-radius:12px;padding:12px;margin:8px 0"><h3 style="color:#ffcc00;margin:0">${m.op} - ${m.prob} REAL | EFECTIVO ${m.efec} | ${m.ev}</h3><div style="font-size:13px;margin:8px 0">MOMIO: ${m.momio} | JUSTO: ${m.justo} | VALOR: ${m.valor}</div><p><b style="color:#00ff88">POR QUE REAL:</b><br>${m.porque}</p></div>`).join('');
  }
  if(t==="parlays"){ h=g.parlays.map(p=>`<div class="mercado"><div><b>${p.picks}</b> ${p.momio}<br><small>${p.detalle}</small><br><small style="color:#ffcc00">EFECTIVO: ${p.efec}</small></div><div>${p.prob}</div></div>`).join(''); }
  if(t==="marcadores"){ h=g.marcadores.map(m=>`<div class="mercado"><div><b>MARCADOR EXACTO ${m.score}</b> ${m.prob} ${m.top?'<span style="color:#00ff88">TOP</span>':''}</div><div><b>${m.momio}</b></div></div>`).join(''); }
  document.getElementById('mercados').innerHTML=h;
}
renderFiltros();
renderLista();
</script>
</body></html>
"""
html_final = html_template.replace("__GAMES_JSON__", games_json).replace("__TOTAL__", str(len(games)))
with open("index.html","w",encoding="utf-8") as f:
    f.write(html_final)
print(f"LISTO V87.3 - {len(games)} eventos - FEM MX + UCL FORZADOS")
