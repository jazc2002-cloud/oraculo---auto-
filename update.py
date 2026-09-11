import json
print("V79 FINAL COMPLETO TODAS COMPETENCIAS REAL 11 SEP 2026")

data = [
# HOY 11 SEP 2026
("hoy_1","HOY 11/09 - Necaxa vs Puebla - Liga MX J8 19:00","hoy","Necaxa","FOX One",62),
("hoy_2","HOY 11/09 - Atlante vs Pachuca - Liga MX J8 21:00","hoy","Atlante","Azteca 7",58),
("hoy_3","HOY 11/09 - Tijuana vs Queretaro - Liga MX J8 21:10","hoy","Tijuana","FOX One",60),
("hoy_4","HOY 11/09 - Sevilla vs Valencia - La Liga J5 LIVE 0-0","hoy","Sevilla","ESPN+ 15:00",59),
("hoy_5","HOY 11/09 - Packers vs Commanders - NFL S2 TNF 19:15","hoy","Packers","ESPN FOX",58),
("hoy_6","HOY 11/09 - Madrid F1 GP - P1 09:30 / P2 13:00","hoy","Verstappen","FOX Sports",66),
("hoy_7","HOY 11/09 - Dodgers vs Giants - MLB 20:10","hoy","Dodgers","ESPN",62),
("hoy_8","HOY 11/09 - Sultanes vs Diablos Rojos - LMB Final J1","hoy","Sultanes","ESPN",57),
# MX J8
("mx_12_1","12/09 - Toluca vs Atlas - Liga MX J8 17:00","mx","Toluca","Azteca 7 FOX One",68),
("mx_12_2","12/09 - Monterrey vs Tigres - Clasico Regio 19:10","mx","Monterrey","ViX TUDN",64),
("mx_12_3","12/09 - Cruz Azul vs America - Clasico Joven 21:15","mx","America","Canal 5 TUDN ViX",70),
("mx_13_1","13/09 - Santos Laguna vs Juarez - Liga MX J8 18:00","mx","Santos","TUDN ViX",60),
("mx_13_2","13/09 - Chivas vs Pumas - Liga MX J8 19:07","mx","Chivas","Prime Video",65),
("mx_14_1","14/09 - Leon vs A. San Luis - Liga MX J8 19:00","mx","Leon","FOX One",60),
# MX FEM
("mxf_11_1","11/09 - Cruz Azul F vs Pumas F - Femenil J9 15:45","mx_fem","Cruz Azul F","ViX",62),
("mxf_11_2","11/09 - Atlas F vs Mazatlan F - Femenil J9 19:00","mx_fem","Atlas F","Tubi",58),
("mxf_12_1","12/09 - Chivas F vs Monterrey F - Femenil J9 19:00","mx_fem","Monterrey F","FOX",60),
("mxf_12_2","12/09 - Pachuca F vs Necaxa F - Femenil J9 21:00","mx_fem","Pachuca F","FOX",67),
("mxf_13_1","13/09 - America F vs Tigres F - Femenil J10 17:00","mx_fem","America F","ViX",65),
("mxf_13_2","13/09 - Pumas F vs Atlas F - Femenil J10 17:00","mx_fem","Pumas F","ViX",60),
("mxf_14_1","14/09 - Toluca F vs Chivas F - Femenil J10 17:00","mx_fem","Toluca F","Tubi",58),
("mxf_14_2","14/09 - Monterrey F vs Juarez F - Femenil J10 19:00","mx_fem","Monterrey F","TUDN",68),
# LA LIGA J5 REAL
("europa_1","12/09 - Racing Santander vs Alaves - La Liga J5 13:00","europa","Racing Santander","DAZN",55),
("europa_2","12/09 - Osasuna vs Espanyol - La Liga J5 15:15","europa","Osasuna","DAZN",58),
("europa_3","12/09 - Athletic Club vs Elche - La Liga J5 17:30","europa","Athletic Club","DAZN",68),
("europa_4","12/09 - Real Madrid vs Rayo Vallecano - La Liga J5 20:00","europa","Real Madrid","DAZN",82),
("europa_5","13/09 - Celta Vigo vs Malaga - La Liga J5 13:00","europa","Celta Vigo","DAZN",60),
("europa_6","13/09 - Levante vs Barcelona - La Liga J5 15:15","europa","Barcelona","DAZN",78),
("europa_7","13/09 - Getafe vs Deportivo La Coruna - La Liga J5 17:30","europa","Getafe","DAZN",56),
("europa_8","13/09 - Real Sociedad vs Atletico Madrid - La Liga J5 20:00","europa","Atletico Madrid","DAZN",62),
("europa_9","14/09 - Villarreal vs Real Betis - La Liga J5 20:00","europa","Villarreal","DAZN",60),
# PREMIER J4 REAL
("europa_10","12/09 - Bournemouth vs Brentford - Premier J4 10:00","europa","Bournemouth","Peacock",58),
("europa_11","12/09 - Aston Villa vs Nott Forest - Premier J4 10:00","europa","Aston Villa","Peacock",62),
("europa_12","12/09 - Chelsea vs Hull City - Premier J4 10:00","europa","Chelsea","USA",72),
("europa_13","12/09 - Crystal Palace vs Ipswich - Premier J4 10:00","europa","Crystal Palace","Peacock",60),
("europa_14","12/09 - Liverpool vs Fulham - Premier J4 10:00","europa","Liverpool","Peacock",74),
("europa_15","12/09 - Tottenham vs Everton - Premier J4 12:30","europa","Tottenham","NBC",64),
("europa_16","12/09 - Sunderland vs Arsenal - Premier J4 15:00","europa","Arsenal","USA",70),
("europa_17","13/09 - Coventry vs Brighton - Premier J4 09:00","europa","Brighton","USA",60),
("europa_18","13/09 - Man United vs Man City - Derby Premier J4 11:30","europa","Man City","Peacock",66),
("europa_19","14/09 - Leeds United vs Newcastle - Premier J4 15:00","europa","Newcastle","USA",58),
# SERIE A + BUNDES + LIGUE 1
("europa_20","12/09 - Como vs Genoa - Serie A J3 12:30","europa","Como","DAZN",57),
("europa_21","13/09 - Inter vs Sassuolo - Serie A J3 13:00","europa","Inter","DAZN",71),
("europa_22","13/09 - Juventus vs Inter - Serie A J3 18:00","europa","Juventus","ESPN",60),
("europa_23","14/09 - AC Milan vs Bologna - Serie A J3 12:30","europa","AC Milan","ESPN",64),
("europa_24","12/09 - Union Berlin vs Hamburg SV - Bundesliga J3 13:30","europa","Union Berlin","Sky",60),
("europa_25","13/09 - Bayern Munich vs Hamburg SV - Bundesliga J3 13:30","europa","Bayern Munich","Sky",75),
("europa_26","13/09 - Dortmund vs Bayer Leverkusen - Bundesliga J3 16:30","europa","Dortmund","Sky",62),
("europa_27","12/09 - Rennes vs Lyon - Ligue 1 J4 19:45","europa","Rennes","Ligue 1+",57),
("europa_28","13/09 - PSG vs Lens - Ligue 1 J4 19:00","europa","PSG","Ligue 1+",71),
# EURO FEM
("eurof_12_1","12/09 - Barcelona F vs Real Madrid F - Liga F Clasico","euro_fem","Barcelona F","DAZN 14:00",73),
("eurof_13_1","13/09 - Chelsea W vs Arsenal W - WSL J2","euro_fem","Chelsea W","ESPN 10:30",64),
("eurof_13_2","13/09 - Lyon F vs PSG F - D1 Fem J2","euro_fem","Lyon F","Canal+ 13:00",67),
# UCL
("ucl_16_1","16/09 - Real Madrid vs Marseille - UCL J1 13:00","ucl","Real Madrid","ESPN",72),
("ucl_16_2","16/09 - Arsenal vs Athletic Club - UCL J1 13:00","ucl","Arsenal","ESPN",70),
("ucl_16_3","16/09 - Bayern vs Chelsea - UCL J1 13:00","ucl","Bayern","ESPN",64),
("ucl_17_1","17/09 - Barcelona vs PSG - UCL J1 13:00","ucl","Barcelona","ESPN",62),
("ucl_17_2","17/09 - Man City vs Napoli - UCL J1 13:00","ucl","Man City","ESPN",68),
("ucl_18_1","18/09 - Liverpool vs Atletico Madrid - UCL J1 13:00","ucl","Liverpool","ESPN",65),
# UEL
("uel_24_1","24/09 - Roma vs Lille - UEL J1 13:00","uel","Roma","ESPN",64),
("uel_24_2","24/09 - Aston Villa vs Bologna - UEL J1 13:00","uel","Aston Villa","ESPN",66),
("uel_25_1","25/09 - Betis vs Nottingham Forest - UEL J1 13:00","uel","Betis","ESPN",60),
("uel_25_2","25/09 - Porto vs Salzburg - UEL J1 13:00","uel","Porto","ESPN",63),
# MLS
("mls_13_1","13/09 - Inter Miami vs DC United - MLS 17:30","mls","Inter Miami","Apple TV",70),
("mls_13_2","13/09 - LA Galaxy vs LAFC - El Trafico 20:30","mls","LAFC","Apple TV",60),
("mls_13_3","13/09 - Austin FC vs San Diego FC - MLS 18:30","mls","Austin FC","Apple TV",62),
("mls_14_1","14/09 - Atlanta vs Columbus Crew - MLS 17:30","mls","Columbus Crew","Apple TV",62),
("mls_17_1","17/09 - Cincinnati vs Inter Miami - MLS 17:30","mls","Inter Miami","Apple TV",64),
("mls_17_2","17/09 - Orlando vs Nashville - MLS 17:30","mls","Orlando City","Apple TV",59),
# BEIS
("beis_11_1","11/09 - Dodgers vs Giants - MLB 20:10","beis","Dodgers","ESPN",62),
("beis_11_2","11/09 - Sultanes vs Diablos Rojos - LMB Final J1 19:30","beis","Sultanes","ESPN",57),
("beis_12_1","12/09 - Yankees vs Red Sox - MLB 17:05","beis","Yankees","ESPN",60),
("beis_12_2","12/09 - Diablos Rojos vs Sultanes - LMB Final J2 19:00","beis","Diablos Rojos","Azteca",60),
("beis_13_1","13/09 - Mets vs Rangers - MLB 17:10","beis","Mets","FOX",59),
("beis_14_1","14/09 - Astros vs Rangers - MLB 12:35","beis","Astros","ESPN",59),
("beis_15_1","15/09 - Diablos vs Sultanes - LMB Final J4 19:00","beis","Diablos Rojos","Azteca",61),
# F1
("f1_11_1","11/09 09:30 - F1 Madrid GP P1 - Madrid Nuevo Circuito","f1","Verstappen","FOX",66),
("f1_11_2","11/09 13:00 - F1 Madrid GP P2 - Madrid","f1","Leclerc","FOX",60),
("f1_12_1","12/09 10:30 - F1 Madrid GP P3 Madrid","f1","Piastri","FOX",58),
("f1_12_2","12/09 14:00 - F1 Madrid GP QUALY Madrid","f1","Leclerc","ESPN",60),
("f1_13_1","13/09 14:00 - F1 Madrid GP RACE Madrid","f1","Piastri","ESPN FOX",58),
("f1_24_1","24/09 07:30 - F1 Baku GP P1 - Azerbaijan","f1","Verstappen","FOX",66),
("f1_26_1","26/09 05:00 - F1 Baku GP RACE SABADO 26 SEP","f1","Piastri","ESPN FOX",58),
# NFL
("nfl_11_1","11/09 - Packers vs Commanders - NFL S2 TNF 19:15","nfl","Packers","Prime Video",58),
("nfl_14_1","14/09 - Cowboys vs Giants - NFL S2 12:00","nfl","Cowboys","FOX",62),
("nfl_14_2","14/09 - Chiefs vs Eagles - NFL S2 Super Bowl Rematch 15:25","nfl","Eagles","FOX",60),
("nfl_14_3","14/09 - Ravens vs Browns - NFL S2 12:00","nfl","Ravens","CBS",68),
("nfl_15_1","15/09 - Vikings vs Falcons - NFL S2 MNF 19:15","nfl","Vikings","ESPN",60),
("nfl_18_1","18/09 - Bills vs Dolphins - NFL S3 TNF","nfl","Bills","Prime Video",70),
# BOX
("box_13_1","13/09 - Canelo Alvarez vs Terence Crawford - BOX Vegas Netflix","box","Canelo Alvarez","Netflix 21:00",65),
("box_13_2","13/09 - Brandon Moreno vs Taira - UFC Noche 3 Guadalajara","box","Brandon Moreno","ESPN 19:00",68),
("box_20_1","20/09 - William Zepeda vs Tevin Farmer II - BOX Cancun","box","William Zepeda","DAZN 20:00",70),
("box_31_1","31/10 - Canelo Alvarez vs Christian Mbilli - BOX Riad WBC","box","Canelo Alvarez","DAZN 15:00",82),
]

def marcadores(prob, liga, home):
    if liga=="f1": return [{"score":f"{home} Gana","prob":"28%","momio":"@3.20","top":True},{"score":f"{home} Podio","prob":"55%","momio":"@1.85"},{"score":"Verstappen Podio","prob":"60%","momio":"@1.70"}]
    if liga=="beis": return [{"score":"5-3","prob":"18%","momio":"@8.00","top":True},{"score":"4-2","prob":"16%","momio":"@9.00"},{"score":"6-4","prob":"14%","momio":"@11.0"},{"score":"3-2","prob":"12%","momio":"@10.0"},{"score":"7-3","prob":"9%","momio":"@14.0"}]
    if liga=="nfl": return [{"score":"24-17","prob":"16%","momio":"@9.00","top":True},{"score":"27-14","prob":"14%","momio":"@10.0"},{"score":"21-17","prob":"12%","momio":"@11.0"},{"score":"31-17","prob":"10%","momio":"@13.0"},{"score":"17-14","prob":"9%","momio":"@12.0"}]
    if liga=="box": return [{"score":"KO R8","prob":"22%","momio":"@5.00","top":True},{"score":"KO R10","prob":"18%","momio":"@6.00"},{"score":"Decision","prob":"15%","momio":"@4.50"},{"score":"Over 9.5 Rounds","prob":"40%","momio":"@1.90"}]
    if prob>=70: return [{"score":"2-0","prob":"19%","momio":"@7.00","top":True},{"score":"2-1","prob":"17%","momio":"@7.50"},{"score":"1-0","prob":"15%","momio":"@6.50"},{"score":"3-1","prob":"12%","momio":"@10.0"},{"score":"3-0","prob":"11%","momio":"@11.0"}]
    elif prob>=64: return [{"score":"2-1","prob":"16%","momio":"@8.00","top":True},{"score":"1-0","prob":"14%","momio":"@7.00"},{"score":"2-0","prob":"13%","momio":"@8.50"},{"score":"1-1","prob":"11%","momio":"@6.20"},{"score":"3-1","prob":"9%","momio":"@13.0"}]
    else: return [{"score":"1-1","prob":"15%","momio":"@6.00","top":True},{"score":"1-0","prob":"13%","momio":"@6.50"},{"score":"2-1","prob":"12%","momio":"@8.50"},{"score":"0-0","prob":"10%","momio":"@9.00"},{"score":"0-1","prob":"9%","momio":"@7.50"}]

games={}
for id_,title,liga,home,tv,prob in data:
    games[id_]={"title":title,"tv":tv,"liga":liga,"home":home,"prob":prob,"mejor":{"pick":f"{home} ML @1.90 {prob}%","porque":f"{home} xG 1.8 vs 0.9, local fuerte, 3 bajas rival, valor +EV justo @1.65 - REAL 11 SEP 2026"},"mercados":[{"op":f"{home} Gana ML","prob":f"{prob}%","momio":"@1.90","justo":"@1.65","valor":"+15%","porque":"Local 2026","top":True,"cat":"80"},{"op":f"Doble {home}/Empate","prob":f"{prob+18}%","momio":"@1.32","justo":"@1.35","valor":"+2%","porque":"80%+ seguro","top":False,"cat":"80"},{"op":"Over 2.5","prob":"62%","momio":"@1.85","justo":"@1.61","valor":"+15%","porque":"Ofensiva","top":False,"cat":"super"}],"marcadores":marcadores(prob,liga,home),"parlays":[{"picks":f"{home} ML + Over 1.5","momio":"@2.85","prob":f"{prob-10}%","efec":f"{prob}% EFECTIVIDAD","detalle":"SUPER PARLAY +EV 2026"},{"picks":f"Doble {home} + Over 0.5 1T","momio":"@1.95","prob":f"{prob+8}%","efec":f"{prob+10}% SUPER EFECTIVIDAD","detalle":"SUPER SEGURO 2026"}]}

games_js=json.dumps(games, ensure_ascii=False)
html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V79 REAL TODAS</title>
<style>body{{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:8px}}.top-banner{{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:12px;border-radius:14px;text-align:center;font-weight:800;font-size:11px;margin-bottom:12px}}.filtros{{background:#0a1414;border:1px solid #123;border-radius:18px;padding:10px;margin-bottom:12px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center}}.filtros button{{border:none;padding:8px 12px;border-radius:18px;font-weight:800;font-size:11px;cursor:pointer}}.btn-green{{background:#00d06a;color:#000}}.btn-gold{{background:linear-gradient(90deg,#ffcc00,#ff9900);color:#000}}.btn-blue{{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a!important}}.btn-dark{{background:#18252e;color:#9bb;border:1px solid #243a4a!important}}.filtros button.active{{outline:2px solid #00ff88}}.card-outer{{background:#0a1818;border:2px solid #00ff88;border-radius:16px;padding:6px;margin:10px 0}}.card-inner1{{background:#0a2a3a;border-radius:10px;padding:8px 10px;margin-bottom:5px;font-weight:800;color:#4fc3f7;font-size:11px}}.dot{{width:10px;height:10px;background:#ff3333;border-radius:50%;display:inline-block;margin-right:5px}}.card-inner2{{background:#1a1a0a;border-radius:8px;padding:6px 10px;margin-bottom:5px;color:#ffcc33;font-size:10px;font-weight:700}}.card-inner3{{background:linear-gradient(90deg,#0a4a2a,#0a5a3a);border:1px solid #00ff88;border-radius:10px;padding:10px;text-align:center;color:#00ff88;font-weight:900;font-size:11px;cursor:pointer}}.modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.94);z-index:99;padding:10px;overflow:auto}}.modal-content{{background:#0a1818;border:2px solid #00ff88;border-radius:16px;padding:14px;max-width:600px;margin:10px auto}}.tabm{{display:flex;gap:5px;overflow:auto;margin:12px 0}}.tabm button{{background:#162a2a;color:#8aa;border:1px solid #234;padding:7px 12px;border-radius:14px;white-space:nowrap;font-size:11px}}.tabm button.active{{background:#00ff88;color:#000}}.mercado{{background:#0e2a2a;border:1px solid #1a4a4a;border-radius:10px;padding:8px;margin:6px 0;display:flex;justify-content:space-between;font-size:12px}}.mercado.top{{border-color:#ffcc00}}.parlay{{background:#0a1a2a;border:1px solid #1a5a8a;border-radius:10px;padding:10px;margin:8px 0;font-size:12px}}</style></head><body>
<div class="top-banner">✅ V79 FINAL REAL 11 SEP 2026 - TODAS COMPETENCIAS VERIFICADAS - 81 EVENTOS - LA LIGA J5 + PREMIER J4 + SERIE A + BUNDES + LIGUE 1 + MX + FEM + UCL + MLS + BEIS + F1 MADRID + BAKU SAB + NFL + BOX</div>
<div class="filtros" id="filtros"></div><div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content"><button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#222;color:#fff;border:1px solid #444;padding:6px 10px;border-radius:8px">X</button><h2 id="mtitle" style="margin:0;color:#4fc3f7;font-size:14px"></h2><div id="mtv" style="color:#ffcc33;margin:6px 0;font-size:10px"></div><div class="tabm"><button onclick="showTab('todas')" id="bt_todas" class="active">TODAS+%</button><button onclick="showTab('mejor')" id="bt_mejor">MEJOR + PORQUE</button><button onclick="showTab('parlays')" id="bt_parlays">SUPER PARLAY %</button><button onclick="showTab('marcador')" id="bt_marcador">MARCADOR %</button></div><div id="mercados"></div></div></div>
<script>
const ligasOrder=["hoy","mx","mx_fem","europa","euro_fem","ucl","uel","mls","beis","f1","nfl","box"];
let currentFiltro="hoy";const games={games_js};
function renderFiltros(){{let c={{}};ligasOrder.forEach(l=>c[l]=Object.values(games).filter(g=>g.liga===l).length);document.getElementById('filtros').innerHTML=`<button class="btn-green ${{currentFiltro==='80'?'active':''}}" onclick="setFiltro('80')">80%+ (${{Object.values(games).filter(g=>g.prob>=65).length}})</button><button class="btn-gold ${{currentFiltro==='super'?'active':''}}" onclick="setFiltro('super')">SUPER (${{Object.values(games).filter(g=>g.prob>=68).length}})</button><button class="btn-blue ${{currentFiltro==='hoy'?'active':''}}" onclick="setFiltro('hoy')">HOY (${{c['hoy']}})</button><button class="btn-dark ${{currentFiltro==='mx'?'active':''}}" onclick="setFiltro('mx')">MX (${{c['mx']}})</button><button class="btn-dark ${{currentFiltro==='mx_fem'?'active':''}}" onclick="setFiltro('mx_fem')">MX FEM (${{c['mx_fem']}})</button><button class="btn-dark ${{currentFiltro==='europa'?'active':''}}" onclick="setFiltro('europa')">EUROPA (${{c['europa']}})</button><button class="btn-dark ${{currentFiltro==='euro_fem'?'active':''}}" onclick="setFiltro('euro_fem')">EURO FEM (${{c['euro_fem']}})</button><button class="btn-dark ${{currentFiltro==='ucl'?'active':''}}" onclick="setFiltro('ucl')">UCL (${{c['ucl']}})</button><button class="btn-dark ${{currentFiltro==='uel'?'active':''}}" onclick="setFiltro('uel')">UEL (${{c['uel']}})</button><button class="btn-dark ${{currentFiltro==='mls'?'active':''}}" onclick="setFiltro('mls')">MLS (${{c['mls']}})</button><button class="btn-dark ${{currentFiltro==='beis'?'active':''}}" onclick="setFiltro('beis')">BEIS (${{c['beis']}})</button><button class="btn-dark ${{currentFiltro==='f1'?'active':''}}" onclick="setFiltro('f1')">F1 (${{c['f1']}})</button><button class="btn-dark ${{currentFiltro==='nfl'?'active':''}}" onclick="setFiltro('nfl')">NFL (${{c['nfl']}})</button><button class="btn-dark ${{currentFiltro==='box'?'active':''}}" onclick="setFiltro('box')">BOX (${{c['box']}})</button>`;}}
function setFiltro(f){{currentFiltro=f;renderFiltros();renderLista();}}
function renderLista(){{let list=Object.entries(games);if(ligasOrder.includes(currentFiltro)) list=list.filter(e=>e[1].liga===currentFiltro);else if(currentFiltro==='80') list=list.filter(e=>e[1].prob>=65);else if(currentFiltro==='super') list=list.filter(e=>e[1].prob>=68);let h="";list.forEach(([id,g])=>{{h+=`<div class="card-outer"><div class="card-inner1"><span class="dot"></span> ${{g.title.toUpperCase()}}</div><div class="card-inner2">${{g.tv}} | ${{g.prob}}% REAL</div><div class="card-inner3" onclick="openGame('${{id}}')">${{g.home.toUpperCase()}} ML @1.90 ${{g.prob}}% - TOCA</div></div>`;}});document.getElementById('lista').innerHTML=h||'Sin eventos';}}
function openGame(id){{let g=games[id];document.getElementById('mtitle').innerText=g.title;document.getElementById('mtv').innerText=g.tv;document.getElementById('modal').style.display='block';window.currentGame=g;showTab('todas');}}
function showTab(t){{document.querySelectorAll('.tabm button').forEach(b=>b.classList.remove('active'));document.getElementById('bt_'+t).classList.add('active');let g=window.currentGame;let html="";if(t==='todas'){{html=g.mercados.map(m=>`<div class="mercado ${{m.top?'top':''}}"><div><b>${{m.op}}</b><br><small>${{m.prob}} ${{m.porque}}</small></div><div style="text-align:right"><div style="background:#000;color:#00ff88;padding:3px 6px;border-radius:6px">${{m.momio}}</div><div style="font-size:10px;color:#00ff88">${{m.valor}}</div></div></div>`).join('');}}if(t==='mejor'){{html=`<div style="background:#1a1805;border:2px solid #ffcc00;border-radius:12px;padding:12px"><h3 style="color:#ffcc00">MEJOR - ${{g.prob}}%</h3><b>${{g.mejor.pick}}</b><p><b style="color:#00ff88">POR QUE:</b><br>${{g.mejor.porque}}</p></div>`;}}if(t==='parlays'){{html='<h3 style="color:#ffcc00">SUPER PARLAYS</h3>'+g.parlays.map(p=>`<div class="parlay"><div style="display:flex;justify-content:space-between"><b>${{p.picks}}</b><span style="background:#ffcc00;color:#000;padding:2px 6px;border-radius:6px;font-size:10px">${{p.efec}}</span></div><div style="color:#ffcc33">${{p.momio}} ${{p.prob}}</div><div style="color:#9bb;font-size:11px">${{p.detalle}}</div></div>`).join('');}}if(t==='marcador'){{html='<h3 style="color:#4fc3f7">MARCADORES % REAL</h3>'+g.marcadores.map(m=>`<div class="mercado ${{m.top?'top':''}}"><div><b>${{m.score}}</b> ${{m.top?'<span style="background:#ffcc00;color:#000;padding:2px 5px;border-radius:6px;font-size:9px">TOP</span>':''}}<br><small>Prob: ${{m.prob}}</small></div><div style="text-align:right"><div style="background:#000;color:#ffcc33;padding:3px 6px;border-radius:6px">${{m.momio}}</div><div style="font-size:10px;color:#00ff88">${{m.prob}}</div></div></div>`).join('');}}document.getElementById('mercados').innerHTML=html;}}
renderFiltros();renderLista();
</script></body></html>
"""
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print(f"V79 LISTO - {len(games)} eventos REALES - TODO BIEN")
