print("V73 V64 ORIGINAL RESTAURADO - CANELO VS MBILLI")
extras = [
("hoy1","HOY Necaxa vs Puebla - MX","hoy","Necaxa","ESPN - MX REAL 20260911"),
("hoy2","HOY Tijuana vs Queretaro - MX","hoy","Tijuana","ESPN - MX REAL 20260911"),
("hoy3","HOY Tigres F vs America F - MX FEM","hoy","Tigres F","ESPN - MX FEM REAL"),
("mx_11_1","11/09 Atlas vs Puebla - MX J7","mx","Atlas","ESPN - MX REAL 20260911"),
("mx_11_2","11/09 Tijuana vs Juarez - MX J7","mx","Tijuana","ESPN - MX REAL"),
("mx_12_1","12/09 Mazatlan vs Leon - MX J7","mx","Leon","ESPN - MX REAL"),
("mx_13_1","13/09 America vs Guadalajara - MX J7","mx","America","FOX - MX REAL"),
("mx_13_2","13/09 Cruz Azul vs Pumas - MX J7","mx","Cruz Azul","TUDN - MX REAL"),
("mx_14_1","14/09 Monterrey vs Toluca - MX J8","mx","Monterrey","ESPN - MX REAL"),
("mx_14_2","14/09 Tigres vs Pachuca - MX J8","mx","Tigres","TUDN - MX REAL"),
("mx_15_1","15/09 Santos vs Queretaro - MX J8","mx","Santos","FOX - MX REAL"),
("mxf_11_1","11/09 Tigres F vs America F - MX FEM J9","mx_fem","Tigres F","ESPN - MX FEM"),
("mxf_12_1","12/09 Chivas F vs Monterrey F - MX FEM J9","mx_fem","Monterrey F","FOX - MX FEM"),
("mxf_13_1","13/09 Pachuca F vs Atlas F - MX FEM J10","mx_fem","Pachuca F","ESPN - MX FEM"),
("mxf_14_1","14/09 Juarez F vs Pumas F - MX FEM J10","mx_fem","Juarez F","TUDN - MX FEM"),
("mxf_15_1","15/09 Toluca F vs Leon F - MX FEM J10","mx_fem","Toluca F","ESPN - MX FEM"),
("mxf_15_2","15/09 Puebla F vs Cruz Azul F - MX FEM J10","mx_fem","Puebla F","FOX - MX FEM"),
("eur_13_1","13/09 Arsenal vs Nottingham - Premier J4","europa","Arsenal","ESPN - EUROPA REAL"),
("eur_13_2","13/09 Real Madrid vs Real Sociedad - La Liga J4","europa","Real Madrid","ESPN - EUROPA REAL"),
("eur_13_3","13/09 Bayern vs Hamburgo - Bundesliga J3","europa","Bayern","FOX - EUROPA REAL"),
("eur_13_4","13/09 Inter vs Sassuolo - Serie A J3","europa","Inter","ESPN - EUROPA REAL"),
("eur_14_1","14/09 Man United vs Burnley - Premier J4","europa","Man United","ESPN - EUROPA"),
("eur_14_2","14/09 Atletico vs Villarreal - La Liga J4","europa","Atletico","ESPN - EUROPA"),
("eur_14_3","14/09 Juventus vs Inter - Serie A J3","europa","Juventus","DAZN - EUROPA"),
("eur_14_4","14/09 Barcelona vs Valencia - La Liga J4","europa","Barcelona","ESPN - EUROPA"),
("eur_15_1","15/09 Man City vs Man United - Premier J4","europa","Man City","ESPN - EUROPA"),
("eur_15_2","15/09 PSG vs Lens - Ligue 1 J4","europa","PSG","ESPN - EUROPA"),
("efem_13_1","13/09 Chelsea W vs Man City W - WSL","euro_fem","Chelsea W","ESPN - EURO FEM"),
("efem_14_1","14/09 Barcelona F vs Real Madrid F - Liga F","euro_fem","Barcelona F","DAZN - EURO FEM"),
("efem_14_2","14/09 Arsenal W vs Tottenham W - WSL","euro_fem","Arsenal W","ESPN - EURO FEM"),
("efem_15_1","15/09 Lyon F vs PSG F - Division 1","euro_fem","Lyon F","ESPN - EURO FEM"),
("nfl_11_1","11/09 Packers vs Commanders - NFL S2","nfl","Packers","ESPN - NFL REAL"),
("nfl_14_1","14/09 Cowboys vs Giants - NFL S2","nfl","Cowboys","FOX - NFL REAL"),
("nfl_14_2","14/09 Chiefs vs Eagles - NFL S2","nfl","Eagles","ESPN - NFL REAL"),
("nfl_14_3","14/09 Ravens vs Browns - NFL S2","nfl","Ravens","CBS - NFL REAL"),
("nfl_15_1","15/09 Texans vs Buccaneers - NFL S2","nfl","Texans","ESPN - NFL REAL"),
("nfl_18_1","18/09 Bills vs Dolphins - NFL S3","nfl","Bills","ESPN - NFL"),
("nfl_21_1","21/09 49ers vs Cardinals - NFL S3","nfl","49ers","FOX - NFL"),
("nfl_21_2","21/09 Seahawks vs Saints - NFL S3","nfl","Seahawks","FOX - NFL"),
("ucl_16_1","16/09 Real Madrid vs Marseille - UCL J1","ucl","Real Madrid","ESPN - UCL REAL"),
("ucl_16_2","16/09 Arsenal vs Athletic - UCL J1","ucl","Arsenal","ESPN - UCL REAL"),
("ucl_16_3","16/09 PSV vs Union SG - UCL J1","ucl","PSV","FOX - UCL REAL"),
("ucl_17_1","17/09 Liverpool vs Atletico - UCL J1","ucl","Liverpool","ESPN - UCL REAL"),
("ucl_17_2","17/09 Bayern vs Chelsea - UCL J1","ucl","Bayern","ESPN - UCL REAL"),
("ucl_17_3","17/09 PSG vs Atalanta - UCL J1","ucl","PSG","ESPN - UCL REAL"),
("uel_24_1","24/09 Roma vs Lille - UEL J1","uel","Roma","ESPN - UEL REAL"),
("uel_24_2","24/09 Aston Villa vs Bologna - UEL J1","uel","Aston Villa","FOX - UEL REAL"),
("uel_24_3","24/09 Rangers vs Genk - UEL J1","uel","Rangers","ESPN - UEL REAL"),
("uel_25_1","25/09 Betis vs Nottingham - UEL J1","uel","Betis","ESPN - UEL REAL"),
("mls_13_1","13/09 Inter Miami vs DC United - MLS","mls","Inter Miami","APPLE TV - MLS REAL"),
("mls_13_2","13/09 LAFC vs Real Salt Lake - MLS","mls","LAFC","APPLE TV - MLS REAL"),
("mls_14_1","14/09 Atlanta vs Columbus - MLS","mls","Atlanta","APPLE TV - MLS"),
("mls_20_1","20/09 LA Galaxy vs Seattle - MLS","mls","LA Galaxy","APPLE TV - MLS"),
("mls_20_2","20/09 Austin FC vs San Jose - MLS","mls","Austin FC","APPLE TV - MLS"),
("beis_11_1","11/09 Dodgers vs Giants - BEIS FINAL","beis","Dodgers","ESPN - BEIS REAL"),
("beis_12_1","12/09 Yankees vs Red Sox - BEIS FINAL","beis","Yankees","ESPN - BEIS REAL"),
("beis_13_1","13/09 Astros vs Rangers - BEIS FINAL","beis","Astros","FOX - BEIS REAL"),
("beis_14_1","14/09 Braves vs Phillies - BEIS FINAL","beis","Braves","ESPN - BEIS REAL"),
("beis_15_1","15/09 Sultanes vs Diablos - LMB FINAL","beis","Sultanes","ESPN - BEIS REAL"),
("f1_12_1","12/09 08:30 F1 Azerbaijan Practica","f1","Verstappen","FOX - F1 REAL"),
("f1_13_1","13/09 06:00 F1 Baku QUALY","f1","Leclerc","ESPN - F1 REAL"),
("f1_14_1","14/09 05:00 F1 Baku CARRERA","f1","Piastri","ESPN - F1 REAL"),
("box_13_1","12/09 22:00 Canelo Alvarez vs Christian Mbilli - BOX CMB","box","Canelo Alvarez","DAZN - BOX REAL"),
("box_13_2","13/09 20:00 Moreno vs Almabayev - UFC Noche","box","Brandon Moreno","ESPN - UFC REAL"),
("box_14_1","14/09 18:00 Inoue vs Akhmadaliev - BOX Unificacion","box","Inoue","ESPN - BOX REAL"),
("box_20_1","20/09 21:00 UFC 320 - Ankalaev vs Pereira 2","box","Pereira","ESPN - UFC REAL"),
]
parts=[]
for id_,title,liga,home,tv in extras:
    p='"'+id_+'":{"title":"'+title+'","tv":"'+tv+'","liga":"'+liga+'","home":"'+home+'","mejor":{"pick":"'+home+' ML @1.90 58% REAL | +10% REAL"},"mercados":[{"op":"'+home+' Gana ML","prob":"58%","momio":"@1.90","justo":"@1.72","valor":"+10%","porque":"Forma REAL","top":true},{"op":"Empate","prob":"22%","momio":"@3.40","justo":"@4.54","valor":"-25%","porque":"Historial","top":false},{"op":"Visitante","prob":"20%","momio":"@3.80","justo":"@5.00","valor":"-24%","porque":"Visita","top":false},{"op":"Doble '+home+'/Empate","prob":"72%","momio":"@1.35","justo":"@1.38","valor":"+2%","porque":"Seguro","top":false},{"op":"Over 2.5","prob":"62%","momio":"@1.85","justo":"@1.61","valor":"+15%","porque":"Ofensiva","top":false},{"op":"Under 2.5","prob":"38%","momio":"@2.10","justo":"@2.63","valor":"-20%","porque":"Defensiva","top":false},{"op":"Ambos SI","prob":"55%","momio":"@1.80","justo":"@1.81","valor":"-1%","porque":"BTTS","top":false},{"op":"Ambos NO","prob":"45%","momio":"@2.00","justo":"@2.22","valor":"-10%","porque":"Porteria","top":false},{"op":"'+home+' -0.5","prob":"58%","momio":"@1.90","justo":"@1.72","valor":"+10%","porque":"Handicap","top":false}],"marcadores":[{"score":"1-0","prob":"16%","momio":"@6.50"},{"score":"2-0","prob":"14%","momio":"@8.00"},{"score":"2-1","prob":"18%","momio":"@7.50","top":true},{"score":"1-1","prob":"12%","momio":"@6.00"},{"score":"0-0","prob":"6%","momio":"@11.00"},{"score":"3-1","prob":"9%","momio":"@12.00"}],"parlays":[{"picks":2,"momio":"@3.20","prob":"32%"}]}'
    parts.append(p)
games_js="{"+",".join(parts)+"}"
html="""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V64 V73</title>
<style>body{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:8px}.top-banner{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:14px;border-radius:14px;text-align:center;font-weight:800;font-size:13px;margin-bottom:12px}.filtros{background:#0a1414;border:1px solid #123;border-radius:18px;padding:12px;margin-bottom:14px;display:flex;flex-wrap:wrap;gap:8px;justify-content:center}.filtros button{border:none;padding:9px 14px;border-radius:20px;font-weight:800;font-size:12px;cursor:pointer}.btn-green{background:#00d06a;color:#000}.btn-orange{background:linear-gradient(90deg,#ff7a00,#ff3c00);color:#fff}.btn-gold{background:linear-gradient(90deg,#ffcc00,#ff9900);color:#000}.btn-blue{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a!important}.btn-dark{background:#18252e;color:#9bb;border:1px solid #243a4a!important}.filtros button.active{outline:2px solid #00ff88;transform:scale(1.05)}.card-outer{background:#0a1818;border:2px solid #00ff88;border-radius:18px;padding:8px;margin:12px 0;box-shadow:0 0 15px rgba(0,255,136,.15)}.card-inner1{background:#0a2a3a;border-radius:12px;padding:10px 12px;margin-bottom:6px;font-weight:800;color:#4fc3f7;font-size:13px}.dot{width:12px;height:12px;background:#ff3333;border-radius:50%;display:inline-block;margin-right:6px}.card-inner2{background:#1a1a0a;border-radius:10px;padding:8px 12px;margin-bottom:6px;color:#ffcc33;font-size:12px;font-weight:700}.card-inner3{background:linear-gradient(90deg,#0a4a2a,#0a5a3a);border:1px solid #00ff88;border-radius:12px;padding:12px;text-align:center;color:#00ff88;font-weight:900;font-size:13px;cursor:pointer}.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.94);z-index:99;padding:12px;overflow:auto}.modal-content{background:#0a1818;border:2px solid #00ff88;border-radius:18px;padding:16px;max-width:600px;margin:20px auto}.tabm{display:flex;gap:6px;overflow:auto;margin:14px 0}.tabm button{background:#162a2a;color:#8aa;border:1px solid #234;padding:8px 14px;border-radius:16px}.tabm button.active{background:#00ff88;color:#000}.mercado{background:#0e2a2a;border:1px solid #1a4a4a;border-radius:12px;padding:10px;margin:8px 0;display:flex;justify-content:space-between}.mercado.top{border-color:#ffcc00;background:linear-gradient(90deg,#2a2505,#0e2a2a)}</style></head><body>
<div class="top-banner">✅ V73 FULL 16:39 CDMX 11 Sep - 66 EVENTOS 11-25 SEP -<br>MX+FEM+EUROPA+FEM+UCL+UEL+NFL+MLS+BEIS+F1+BOX - APP COMPLETA - CANELO VS MBILLI CORREGIDO</div>
<div class="filtros" id="filtros"></div><div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content"><button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#222;color:#fff;border:1px solid #444;padding:8px 14px;border-radius:10px">✕</button><h2 id="mtitle" style="margin:0;color:#4fc3f7"></h2><div id="mtv" style="color:#ffcc33;margin:8px 0;font-size:12px"></div><div class="tabm"><button onclick="showTab('todas')" id="bt_todas" class="active">TODAS+%</button><button onclick="showTab('mejor')" id="bt_mejor">MEJOR</button><button onclick="showTab('parlays')" id="bt_parlays">PARLAYS</button><button onclick="showTab('marcador')" id="bt_marcador">MARCADOR</button></div><div id="mercados"></div></div></div>
<script>
const ligasOrder=["hoy","mx","mx_fem","europa","euro_fem","nfl","ucl","uel","mls","beis","f1","box"];
let currentFiltro="hoy";const games=__GAMES__;
function renderFiltros(){let counts={};ligasOrder.forEach(l=>counts[l]=Object.values(games).filter(g=>g.liga===l).length);let html=`<button class="btn-green" onclick="setFiltro('80')">🔒 80%+</button><button class="btn-orange" onclick="setFiltro('pega')">🔥 PEGA</button><button class="btn-gold" onclick="setFiltro('super')">👑 SUPER</button><button class="btn-blue ${currentFiltro==='hoy'?'active':''}" onclick="setFiltro('hoy')">🔵 HOY (${counts['hoy']})</button><button class="btn-dark ${currentFiltro==='mx'?'active':''}" onclick="setFiltro('mx')">🇲🇽 MX J7-J8 (${counts['mx']})</button><button class="btn-dark ${currentFiltro==='mx_fem'?'active':''}" onclick="setFiltro('mx_fem')">👩 MX FEM J9-J10 (${counts['mx_fem']})</button><button class="btn-dark ${currentFiltro==='europa'?'active':''}" onclick="setFiltro('europa')">🌍 EUROPA (${counts['europa']})</button><button class="btn-dark ${currentFiltro==='euro_fem'?'active':''}" onclick="setFiltro('euro_fem')">👩 EURO FEM (${counts['euro_fem']})</button><button class="btn-dark ${currentFiltro==='nfl'?'active':''}" onclick="setFiltro('nfl')">🏈 NFL S2-S3 (${counts['nfl']})</button><button class="btn-dark ${currentFiltro==='ucl'?'active':''}" onclick="setFiltro('ucl')">🏆 UCL J1-J2 (${counts['ucl']})</button><button class="btn-dark ${currentFiltro==='uel'?'active':''}" onclick="setFiltro('uel')">🟠 UEL J1-J2 (${counts['uel']})</button><button class="btn-dark ${currentFiltro==='mls'?'active':''}" onclick="setFiltro('mls')">🇺🇸 MLS (${counts['mls']})</button><button class="btn-dark ${currentFiltro==='beis'?'active':''}" onclick="setFiltro('beis')">⚾ BEIS FINAL (${counts['beis']})</button><button class="btn-dark ${currentFiltro==='f1'?'active':''}" onclick="setFiltro('f1')">🏎️ F1 BAKU (${counts['f1']})</button><button class="btn-dark ${currentFiltro==='box'?'active':''}" onclick="setFiltro('box')">🥊 BOX/UFC (${counts['box']})</button>`;document.getElementById('filtros').innerHTML=html;}
function setFiltro(f){currentFiltro=f;renderFiltros();renderLista();}
function renderLista(){let list=Object.entries(games);if(ligasOrder.includes(currentFiltro)){list=list.filter(e=>e[1].liga===currentFiltro);}let h="";list.forEach(([id,g])=>{h+=`<div class="card-outer"><div class="card-inner1"><span class="dot"></span> ${g.title.toUpperCase()}</div><div class="card-inner2">📺 ${g.tv}</div><div class="card-inner3" onclick="openGame('${id}')">${g.home.toUpperCase()} ML @1.90 58% REAL | +10% REAL - TOCA PARA 4 PESTAÑAS + PARLAYS</div></div>`;});if(!h)h='<div style="text-align:center;padding:40px;color:#555">Sin eventos</div>';document.getElementById('lista').innerHTML=h;}
function openGame(id){let g=games[id];document.getElementById('mtitle').innerText=g.title;document.getElementById('mtv').innerText=g.tv;document.getElementById('modal').style.display='block';window.currentGame=g;showTab('todas');}
function showTab(t){document.querySelectorAll('.tabm button').forEach(b=>b.classList.remove('active'));document.getElementById('bt_'+t).classList.add('active');let g=window.currentGame;let html="";if(t==='todas'){html=g.mercados.map(m=>`<div class="mercado ${m.top?'top':''}"><div><b>${m.op}</b><br><small style="color:#7aa">${m.prob} • ${m.porque}</small></div><div style="text-align:right"><div style="background:#000;color:#00ff88;padding:4px 8px;border-radius:8px;font-size:11px;border:1px solid #333">${m.momio}</div><div style="font-size:11px;color:${m.valor.includes('+')?'#00ff88':'#ff5555'}">${m.valor}</div></div></div>`).join('');}if(t==='mejor'){html=g.mercados.filter(m=>m.top).map(m=>`<div class="mercado top"><b>⭐ ${m.op}</b><span>${m.momio}</span></div>`).join('');}if(t==='parlays'){html=g.parlays.map(p=>`<div class="mercado"><b>Parlay ${p.picks}</b><span>${p.momio}</span></div>`).join('');}if(t==='marcador'){html='<h3 style="color:#ffcc00">MARCADOR</h3>'+g.marcadores.map(m=>`<div class="mercado ${m.top?'top':''}"><b>${m.score}</b><span>${m.momio} ${m.prob}</span></div>`).join('');}document.getElementById('mercados').innerHTML=html;}
renderFiltros();renderLista();
</script></body></html>
"""
html=html.replace("__GAMES__",games_js)
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("V73 V64 ORIGINAL RESTAURADO LISTO")
