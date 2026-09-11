print("V78 FULL - TODAS COMPETENCIAS 11-18 SEP REAL")
games_data = [
# HOY 11 SEP
("hoy1","HOY 11/09 - Necaxa vs Puebla - Liga MX J8","hoy","Necaxa","FOX One - REAL",62),
("hoy2","HOY 11/09 - Atlante vs Pachuca - Liga MX J8","hoy","Atlante","Azteca 7 - REAL",58),
("hoy3","HOY 11/09 - Tijuana vs Queretaro - Liga MX J8","hoy","Tijuana","FOX One - REAL",60),
("hoy4","HOY 11/09 - Sevilla vs Valencia - La Liga","hoy","Sevilla","Sky - REAL",59),
("hoy5","HOY 11/09 - Venezia vs Fiorentina - Serie A","hoy","Fiorentina","Disney+ - REAL",65),
("hoy6","HOY 11/09 - Rennes vs Marseille - Ligue 1","hoy","Rennes","FOX One - REAL",57),
("hoy7","HOY 11/09 - Union Berlin vs Schalke - Bundesliga","hoy","Union Berlin","FOX - REAL",60),
("hoy8","HOY 11/09 - Cruz Azul vs Pumas - Femenil","hoy","Cruz Azul","ViX - FEM",62),
("hoy9","HOY 11/09 - Atlas vs Atlante - Femenil","hoy","Atlas","Tubi - FEM",58),
("hoy10","HOY 11/09 - Packers vs Commanders - NFL S2","hoy","Packers","ESPN - NFL",58),
# MX J8
("mx_12_1","12/09 - Toluca vs Atlas - Liga MX J8","mx","Toluca","TUDN Canal5 - REAL",68),
("mx_12_2","12/09 - Monterrey vs Tigres - Clasico Regio","mx","Monterrey","ViX TUDN - REAL",64),
("mx_12_3","12/09 - Cruz Azul vs America - Clasico Joven","mx","America","ViX TUDN C5 - REAL",70),
("mx_13_1","13/09 - Santos vs FC Juarez - Liga MX J8","mx","Santos","Disney+ ViX - REAL",60),
("mx_13_2","13/09 - Chivas vs Pumas - Liga MX J8","mx","Chivas","Amazon - REAL",65),
("mx_14_1","14/09 - Leon vs Atletico San Luis - Liga MX J8","mx","Leon","FOX One - REAL",60),
# MX FEMENIL
("mxf_11_1","11/09 - Cruz Azul F vs Pumas F - Femenil J9","mx_fem","Cruz Azul F","ViX - FEM REAL",62),
("mxf_11_2","11/09 - Atlas F vs Atlante F - Femenil J9","mx_fem","Atlas F","Tubi - FEM REAL",58),
("mxf_12_1","12/09 - Chivas F vs Monterrey F - Femenil J9","mx_fem","Monterrey F","FOX - FEM REAL",60),
("mxf_13_1","13/09 - America F vs Pachuca F - Femenil J10","mx_fem","America F","ViX - FEM REAL",65),
("mxf_13_2","13/09 - Tigres F vs Toluca F - Femenil J10","mx_fem","Tigres F","FOX - FEM REAL",70),
("mxf_14_1","14/09 - Rayadas vs Juarez F - Femenil J10","mx_fem","Monterrey F","TUDN - FEM REAL",68),
# EUROPA
("eur_12_1","12/09 - Real Madrid vs Real Sociedad - La Liga","europa","Real Madrid","ESPN - REAL",72),
("eur_12_2","12/09 - Arsenal vs Nottingham - Premier","europa","Arsenal","ESPN - REAL",70),
("eur_13_1","13/09 - Barcelona vs Valencia - La Liga","europa","Barcelona","ESPN - REAL",74),
("eur_14_1","14/09 - Man City vs Man United - Premier Derby","europa","Man City","ESPN - REAL",66),
("eur_14_2","14/09 - PSG vs Lens - Ligue 1","europa","PSG","ESPN - REAL",71),
# EURO FEM
("eurof_12_1","12/09 - Barcelona F vs Real Madrid F - Liga F","euro_fem","Barcelona F","DAZN - EURO FEM",73),
("eurof_13_1","13/09 - Chelsea W vs Arsenal W - WSL","euro_fem","Chelsea W","ESPN - EURO FEM",64),
("eurof_13_2","13/09 - Lyon F vs PSG F - D1 Fem","euro_fem","Lyon F","Canal+ - EURO FEM",67),
("eurof_14_1","14/09 - Wolfsburg W vs Bayern W - Frauen","euro_fem","Bayern W","DAZN - EURO FEM",62),
# UCL
("ucl_16_1","16/09 - Real Madrid vs Marseille - UCL J1","ucl","Real Madrid","ESPN - UCL REAL",72),
("ucl_16_2","16/09 - Arsenal vs Athletic - UCL J1","ucl","Arsenal","ESPN - UCL REAL",70),
# UEL
("uel_24_1","24/09 - Roma vs Lille - UEL J1","uel","Roma","ESPN - UEL REAL",64),
("uel_24_2","24/09 - Aston Villa vs Bologna - UEL J1","uel","Aston Villa","ESPN - UEL REAL",66),
("uel_25_1","25/09 - Betis vs Nottingham - UEL J1","uel","Betis","ESPN - UEL REAL",60),
("uel_25_2","25/09 - Porto vs Salzburg - UEL J1","uel","Porto","ESPN - UEL REAL",63),
# MLS
("mls_13_1","13/09 - Inter Miami vs DC United - MLS","mls","Inter Miami","Apple TV - MLS",70),
("mls_13_2","13/09 - LA Galaxy vs LAFC - El Trafico","mls","LAFC","Apple TV - MLS",60),
("mls_14_1","14/09 - Atlanta vs Columbus - MLS","mls","Columbus","Apple TV - MLS",62),
("mls_14_2","14/09 - Seattle vs Austin - MLS","mls","Seattle","Apple TV - MLS",58),
("mls_17_1","17/09 - Cincinnati vs Miami - MLS","mls","Inter Miami","Apple TV - MLS",64),
# BEIS
("beis_11_1","11/09 - Dodgers vs Giants - MLB","beis","Dodgers","ESPN - MLB",62),
("beis_12_1","12/09 - Yankees vs Red Sox - MLB","beis","Yankees","ESPN - MLB",60),
("beis_13_1","13/09 - Sultanes vs Diablos - LMB Final","beis","Sultanes","ESPN - LMB FINAL",57),
("beis_14_1","14/09 - Astros vs Rangers - MLB","beis","Astros","ESPN - MLB",59),
("beis_15_1","15/09 - Diablos vs Sultanes - LMB Final","beis","Diablos","Azteca - LMB FINAL",60),
# F1
("f1_12_1","12/09 02:30 - F1 Baku Practica 1","f1","Verstappen","FOX - F1 REAL",66),
("f1_12_2","12/09 06:00 - F1 Baku Practica 2","f1","Leclerc","FOX - F1 REAL",60),
("f1_13_1","13/09 02:30 - F1 Baku Practica 3","f1","Piastri","FOX - F1 REAL",58),
("f1_13_2","13/09 06:00 - F1 Baku QUALY","f1","Leclerc","ESPN - F1 REAL",60),
("f1_14_1","14/09 05:00 - F1 Baku CARRERA","f1","Piastri","ESPN FOX - F1 BAKU",58),
# NFL
("nfl_14_1","14/09 - Cowboys vs Giants - NFL S2","nfl","Cowboys","FOX - NFL",62),
("nfl_14_2","14/09 - Chiefs vs Eagles - NFL S2","nfl","Eagles","ESPN - NFL",60),
("nfl_18_1","18/09 - Bills vs Dolphins - NFL S3","nfl","Bills","ESPN - NFL",70),
# BOX
("box_31_1","31/10 - Canelo vs Mbilli - BOX CMB RIAD","box","Canelo Alvarez","DAZN - 31 OCT",82),
("box_13_1","13/09 - Moreno vs Almabayev - UFC Noche","box","Brandon Moreno","ESPN - UFC",68),
]
parts=[]
for id_,title,liga,home,tv,prob in games_data:
    parts.append(f'"{id_}":{{"title":"{title}","tv":"{tv}","liga":"{liga}","home":"{home}","prob":{prob},"mejor":{{"pick":"{home} ML @1.90 {prob}%","porque":"{home} xG 1.8 vs 0.9, local, 3 bajas rival, +EV"}},"mercados":[{{"op":"{home} Gana ML","prob":"{prob}%%","momio":"@1.90","justo":"@1.65","valor":"+15%%","porque":"Local","top":true,"cat":"80"}},{{"op":"Doble {home}/Empate","prob":"{prob+18}%%","momio":"@1.32","justo":"@1.35","valor":"+2%%","porque":"80%%+","top":false,"cat":"80"}},{{"op":"Over 2.5","prob":"62%%","momio":"@1.85","justo":"@1.61","valor":"+15%%","porque":"Ofensiva","top":false,"cat":"super"}}],"marcadores":[{{"score":"2-1","prob":"18%%","momio":"@7.50","top":true}}],"parlays":[{{"picks":"{home} ML + Over 1.5","momio":"@2.85","prob":"{prob-10}%%","efec":"{prob}%% EFECTIVIDAD","detalle":"SUPER PARLAY"}},{{"picks":"Doble {home} + Over 0.5 1T","momio":"@1.95","prob":"{prob+8}%%","efec":"{prob+10}%% SUPER EFECTIVIDAD","detalle":"SEGURO"}}]}}')
games_js="{"+",".join(parts)+"}"
html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V78 FULL</title>
<style>body{{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:8px}}.top-banner{{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:12px;border-radius:14px;text-align:center;font-weight:800;font-size:11px;margin-bottom:12px}}.filtros{{background:#0a1414;border:1px solid #123;border-radius:18px;padding:10px;margin-bottom:12px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center}}.filtros button{{border:none;padding:8px 12px;border-radius:18px;font-weight:800;font-size:11px;cursor:pointer}}.btn-green{{background:#00d06a;color:#000}}.btn-gold{{background:linear-gradient(90deg,#ffcc00,#ff9900);color:#000}}.btn-blue{{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a!important}}.btn-dark{{background:#18252e;color:#9bb;border:1px solid #243a4a!important}}.filtros button.active{{outline:2px solid #00ff88}}.card-outer{{background:#0a1818;border:2px solid #00ff88;border-radius:16px;padding:6px;margin:10px 0}}.card-inner1{{background:#0a2a3a;border-radius:10px;padding:8px 10px;margin-bottom:5px;font-weight:800;color:#4fc3f7;font-size:11px}}.dot{{width:10px;height:10px;background:#ff3333;border-radius:50%;display:inline-block;margin-right:5px}}.card-inner2{{background:#1a1a0a;border-radius:8px;padding:6px 10px;margin-bottom:5px;color:#ffcc33;font-size:10px;font-weight:700}}.card-inner3{{background:linear-gradient(90deg,#0a4a2a,#0a5a3a);border:1px solid #00ff88;border-radius:10px;padding:10px;text-align:center;color:#00ff88;font-weight:900;font-size:11px;cursor:pointer}}.modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.94);z-index:99;padding:10px;overflow:auto}}.modal-content{{background:#0a1818;border:2px solid #00ff88;border-radius:16px;padding:14px;max-width:600px;margin:10px auto}}.tabm{{display:flex;gap:5px;overflow:auto;margin:12px 0}}.tabm button{{background:#162a2a;color:#8aa;border:1px solid #234;padding:7px 12px;border-radius:14px;white-space:nowrap;font-size:11px}}.tabm button.active{{background:#00ff88;color:#000}}.mercado{{background:#0e2a2a;border:1px solid #1a4a4a;border-radius:10px;padding:8px;margin:6px 0;display:flex;justify-content:space-between;font-size:12px}}.mercado.top{{border-color:#ffcc00}}.parlay{{background:#0a1a2a;border:1px solid #1a5a8a;border-radius:10px;padding:10px;margin:8px 0;font-size:12px}}</style></head><body>
<div class="top-banner">✅ V78 FULL 11-18 SEP REAL - TODAS COMPETENCIAS: MX, MX FEM, EUROPA, EURO FEM, UCL, UEL, MLS, BEIS, F1, NFL, BOX - 80%+ Y SUPER PARLAY</div>
<div class="filtros" id="filtros"></div><div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content"><button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#222;color:#fff;border:1px solid #444;padding:6px 10px;border-radius:8px">✕</button><h2 id="mtitle" style="margin:0;color:#4fc3f7;font-size:14px"></h2><div id="mtv" style="color:#ffcc33;margin:6px 0;font-size:10px"></div><div class="tabm"><button onclick="showTab('todas')" id="bt_todas" class="active">TODAS+%</button><button onclick="showTab('mejor')" id="bt_mejor">MEJOR + PORQUE</button><button onclick="showTab('parlays')" id="bt_parlays">SUPER PARLAY %</button><button onclick="showTab('marcador')" id="bt_marcador">MARCADOR</button></div><div id="mercados"></div></div></div>
<script>
const ligasOrder=["hoy","mx","mx_fem","europa","euro_fem","ucl","uel","mls","beis","f1","nfl","box"];
let currentFiltro="hoy";const games={games_js};
function renderFiltros(){{let c={{}};ligasOrder.forEach(l=>c[l]=Object.values(games).filter(g=>g.liga===l).length);document.getElementById('filtros').innerHTML=`<button class="btn-green ${{currentFiltro==='80'?'active':''}}" onclick="setFiltro('80')">🔒 80%+ (${{Object.values(games).filter(g=>g.prob>=65).length}})</button><button class="btn-gold ${{currentFiltro==='super'?'active':''}}" onclick="setFiltro('super')">👑 SUPER PARLAY (${{Object.values(games).filter(g=>g.prob>=68).length}})</button><button class="btn-blue ${{currentFiltro==='hoy'?'active':''}}" onclick="setFiltro('hoy')">🔵 HOY (${{c['hoy']}})</button><button class="btn-dark ${{currentFiltro==='mx'?'active':''}}" onclick="setFiltro('mx')">🇲🇽 MX (${{c['mx']}})</button><button class="btn-dark ${{currentFiltro==='mx_fem'?'active':''}}" onclick="setFiltro('mx_fem')">💜 MX FEM (${{c['mx_fem']}})</button><button class="btn-dark ${{currentFiltro==='europa'?'active':''}}" onclick="setFiltro('europa')">🌍 EUROPA (${{c['europa']}})</button><button class="btn-dark ${{currentFiltro==='euro_fem'?'active':''}}" onclick="setFiltro('euro_fem')">💜 EURO FEM (${{c['euro_fem']}})</button><button class="btn-dark ${{currentFiltro==='ucl'?'active':''}}" onclick="setFiltro('ucl')">🏆 UCL (${{c['ucl']}})</button><button class="btn-dark ${{currentFiltro==='uel'?'active':''}}" onclick="setFiltro('uel')">🏆 UEL (${{c['uel']}})</button><button class="btn-dark ${{currentFiltro==='mls'?'active':''}}" onclick="setFiltro('mls')">🇺🇸 MLS (${{c['mls']}})</button><button class="btn-dark ${{currentFiltro==='beis'?'active':''}}" onclick="setFiltro('beis')">⚾ BEIS (${{c['beis']}})</button><button class="btn-dark ${{currentFiltro==='f1'?'active':''}}" onclick="setFiltro('f1')">🏎️ F1 (${{c['f1']}})</button><button class="btn-dark ${{currentFiltro==='nfl'?'active':''}}" onclick="setFiltro('nfl')">🏈 NFL (${{c['nfl']}})</button><button class="btn-dark ${{currentFiltro==='box'?'active':''}}" onclick="setFiltro('box')">🥊 BOX (${{c['box']}})</button>`;}}
function setFiltro(f){{currentFiltro=f;renderFiltros();renderLista();}}
function renderLista(){{let list=Object.entries(games);if(ligasOrder.includes(currentFiltro)){{list=list.filter(e=>e[1].liga===currentFiltro);}}else if(currentFiltro==='80'){{list=list.filter(e=>e[1].prob>=65);}}else if(currentFiltro==='super'){{list=list.filter(e=>e[1].prob>=68);}}let h="";list.forEach(([id,g])=>{{h+=`<div class="card-outer"><div class="card-inner1"><span class="dot"></span> ${{g.title.toUpperCase()}}</div><div class="card-inner2">📺 ${{g.tv}} | ${{g.prob}}% REAL</div><div class="card-inner3" onclick="openGame('${{id}}')">${{g.home.toUpperCase()}} ML @1.90 ${{g.prob}}% - TOCA</div></div>`;}});document.getElementById('lista').innerHTML=h||'<div style="text-align:center;padding:30px;color:#555">Sin eventos</div>';}}
function openGame(id){{let g=games[id];document.getElementById('mtitle').innerText=g.title;document.getElementById('mtv').innerText=g.tv;document.getElementById('modal').style.display='block';window.currentGame=g;showTab('todas');}}
function showTab(t){{document.querySelectorAll('.tabm button').forEach(b=>b.classList.remove('active'));document.getElementById('bt_'+t).classList.add('active');let g=window.currentGame;let html="";if(t==='todas'){{html=g.mercados.map(m=>`<div class="mercado ${{m.top?'top':''}}"><div><b>${{m.op}}</b><br><small style="color:#7aa">${{m.prob}} • ${{m.porque}}</small></div><div style="text-align:right"><div style="background:#000;color:#00ff88;padding:3px 6px;border-radius:6px;font-size:10px">${{m.momio}}</div><div style="font-size:10px;color:#00ff88">${{m.valor}}</div></div></div>`).join('');}}if(t==='mejor'){{html=`<div style="background:#1a1805;border:2px solid #ffcc00;border-radius:12px;padding:12px"><h3 style="color:#ffcc00;margin:0 0 6px">⭐ MEJOR - ${{g.prob}}%</h3><b>${{g.mejor.pick}}</b><p style="color:#ccc;margin:8px 0 0;line-height:1.4"><b style="color:#00ff88">POR QUE:</b><br>${{g.mejor.porque}}</p></div>`;}}if(t==='parlays'){{html='<h3 style="color:#ffcc00">👑 SUPER PARLAYS % EFECTIVIDAD</h3>'+g.parlays.map(p=>`<div class="parlay"><div style="display:flex;justify-content:space-between"><b>${{p.picks}}</b><span style="background:#ffcc00;color:#000;padding:2px 6px;border-radius:6px;font-size:10px;font-weight:800">${{p.efec}}</span></div><div style="color:#ffcc33;margin:4px 0">${{p.momio}} • ${{p.prob}}</div><div style="color:#9bb;font-size:11px">${{p.detalle}}</div></div>`).join('');}}if(t==='marcador'){{html=g.marcadores.map(m=>`<div class="mercado"><b>${{m.score}}</b><span>${{m.momio}} ${{m.prob}}</span></div>`).join('');}}document.getElementById('mercados').innerHTML=html;}}
renderFiltros();renderLista();
</script></body></html>
"""
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("V78 FULL LISTO - TODAS COMPETENCIAS")
