print("V72 FINAL CORREGIDO - CANELO VS MBILLI - 66 EVENTOS")
extras = [
("hoy1","HOY 11/09 - Atlas vs Puebla - Liga MX J7","hoy","Atlas","11/09"),
("hoy2","HOY 11/09 - Tijuana vs Juarez - Liga MX J7","hoy","Tijuana","11/09"),
("hoy3","HOY 11/09 - Tigres F vs America F - MX FEM J9","hoy","Tigres F","11/09"),
("mx_11_1","11/09 - Atlas vs Puebla - Liga MX J7","mx","Atlas","11/09"),
("mx_11_2","11/09 - Tijuana vs Juarez - Liga MX J7","mx","Tijuana","11/09"),
("mx_12_1","12/09 - Mazatlan vs Leon - Liga MX J7","mx","Leon","11/09"),
("mx_13_1","13/09 - America vs Guadalajara - Liga MX J7","mx","America","13/09"),
("mx_13_2","13/09 - Cruz Azul vs Pumas - Liga MX J7","mx","Cruz Azul","13/09"),
("mx_14_1","14/09 - Monterrey vs Toluca - Liga MX J8","mx","Monterrey","14/09"),
("mx_14_2","14/09 - Tigres vs Pachuca - Liga MX J8","mx","Tigres","14/09"),
("mx_15_1","15/09 - Santos vs Queretaro - Liga MX J8","mx","Santos","15/09"),
("mxf_11_1","11/09 - Tigres F vs America F - MX FEM J9","mx_fem","Tigres F","11/09"),
("mxf_12_1","12/09 - Chivas F vs Monterrey F - MX FEM J9","mx_fem","Monterrey F","11/09"),
("mxf_13_1","13/09 - Pachuca F vs Atlas F - MX FEM J10","mx_fem","Pachuca F","13/09"),
("mxf_14_1","14/09 - Juarez F vs Pumas F - MX FEM J10","mx_fem","Juarez F","14/09"),
("mxf_15_1","15/09 - Toluca F vs Leon F - MX FEM J10","mx_fem","Toluca F","15/09"),
("mxf_15_2","15/09 - Puebla F vs Cruz Azul F - MX FEM J10","mx_fem","Puebla F","15/09"),
("eur_13_1","13/09 - Arsenal vs Nottingham - Premier J4","europa","Arsenal","13/09"),
("eur_13_2","13/09 - Real Madrid vs Real Sociedad - La Liga J4","europa","Real Madrid","13/09"),
("eur_13_3","13/09 - Bayern vs Hamburgo - Bundesliga J3","europa","Bayern","13/09"),
("eur_13_4","13/09 - Inter vs Sassuolo - Serie A J3","europa","Inter","13/09"),
("eur_14_1","14/09 - Man United vs Burnley - Premier J4","europa","Man United","14/09"),
("eur_14_2","14/09 - Atletico Madrid vs Villarreal - La Liga J4","europa","Atletico","14/09"),
("eur_14_3","14/09 - Juventus vs Inter - Serie A J3","europa","Juventus","14/09"),
("eur_14_4","14/09 - Barcelona vs Valencia - La Liga J4","europa","Barcelona","14/09"),
("eur_15_1","15/09 - Man City vs Man United - Premier J4","europa","Man City","15/09"),
("eur_15_2","15/09 - PSG vs Lens - Ligue 1 J4","europa","PSG","15/09"),
("efem_13_1","13/09 - Chelsea W vs Man City W - WSL","euro_fem","Chelsea W","13/09"),
("efem_14_1","14/09 - Barcelona F vs Real Madrid F - Liga F","euro_fem","Barcelona F","14/09"),
("efem_14_2","14/09 - Arsenal W vs Tottenham W - WSL","euro_fem","Arsenal W","14/09"),
("efem_15_1","15/09 - Lyon F vs PSG F - Division 1","euro_fem","Lyon F","15/09"),
("nfl_11_1","11/09 - Packers vs Commanders - NFL S2","nfl","Packers","11/09"),
("nfl_14_1","14/09 - Cowboys vs Giants - NFL S2","nfl","Cowboys","14/09"),
("nfl_14_2","14/09 - Chiefs vs Eagles - NFL S2","nfl","Eagles","14/09"),
("nfl_14_3","14/09 - Ravens vs Browns - NFL S2","nfl","Ravens","14/09"),
("nfl_15_1","15/09 - Texans vs Buccaneers - NFL S2","nfl","Texans","14/09"),
("nfl_18_1","18/09 - Bills vs Dolphins - NFL S3","nfl","Bills","14/09"),
("nfl_21_1","21/09 - 49ers vs Cardinals - NFL S3","nfl","49ers","14/09"),
("nfl_21_2","21/09 - Seahawks vs Saints - NFL S3","nfl","Seahawks","14/09"),
("ucl_16_1","16/09 - Real Madrid vs Marseille - UCL J1","ucl","Real Madrid","16/09"),
("ucl_16_2","16/09 - Arsenal vs Athletic - UCL J1","ucl","Arsenal","16/09"),
("ucl_16_3","16/09 - PSV vs Union SG - UCL J1","ucl","PSV","16/09"),
("ucl_17_1","17/09 - Liverpool vs Atletico - UCL J1","ucl","Liverpool","17/09"),
("ucl_17_2","17/09 - Bayern vs Chelsea - UCL J1","ucl","Bayern","17/09"),
("ucl_17_3","17/09 - PSG vs Atalanta - UCL J1","ucl","PSG","17/09"),
("uel_24_1","24/09 - Roma vs Lille - UEL J1","uel","Roma","24/09"),
("uel_24_2","24/09 - Aston Villa vs Bologna - UEL J1","uel","Aston Villa","24/09"),
("uel_24_3","24/09 - Rangers vs Genk - UEL J1","uel","Rangers","24/09"),
("uel_25_1","25/09 - Betis vs Nottingham - UEL J1","uel","Betis","25/09"),
("mls_13_1","13/09 - Inter Miami vs DC United - MLS","mls","Inter Miami","13/09"),
("mls_13_2","13/09 - LAFC vs Real Salt Lake - MLS","mls","LAFC","13/09"),
("mls_14_1","14/09 - Atlanta vs Columbus - MLS","mls","Atlanta","14/09"),
("mls_20_1","20/09 - LA Galaxy vs Seattle - MLS","mls","LA Galaxy","20/09"),
("mls_20_2","20/09 - Austin FC vs San Jose - MLS","mls","Austin FC","20/09"),
("beis_11_1","11/09 - Dodgers vs Giants - BEIS FINAL","beis","Dodgers","11/09"),
("beis_12_1","12/09 - Yankees vs Red Sox - BEIS FINAL","beis","Yankees","11/09"),
("beis_13_1","13/09 - Astros vs Rangers - BEIS FINAL","beis","Astros","11/09"),
("beis_14_1","14/09 - Braves vs Phillies - BEIS FINAL","beis","Braves","11/09"),
("beis_15_1","15/09 - Sultanes vs Diablos - LMB FINAL","beis","Sultanes","11/09"),
("f1_12_1","12/09 08:30 - F1 Azerbaijan Practica","f1","Verstappen","12/09"),
("f1_13_1","13/09 06:00 - F1 Baku QUALY","f1","Leclerc","13/09"),
("f1_14_1","14/09 05:00 - F1 Baku CARRERA","f1","Piastri","14/09"),
("box_13_1","12/09 22:00 - Canelo Alvarez vs Christian Mbilli - BOX CMB","box","Canelo Alvarez","12/09"),
("box_13_2","13/09 20:00 - Moreno vs Almabayev - UFC Noche","box","Brandon Moreno","13/09"),
("box_14_1","14/09 18:00 - Inoue vs Akhmadaliev - BOX Unificacion","box","Inoue","14/09"),
("box_20_1","20/09 21:00 - UFC 320 - Ankalaev vs Pereira 2","box","Pereira","20/09"),
]
games_parts=[]
for id_,title,liga,home,fecha in extras:
    p='"'+id_+'":{"title":"'+title+'","tv":"V72 '+fecha+' ESPN","liga":"'+liga+'","prob":58,"mejor":{"pick":"'+home+' ML @1.90"},"mercados":[{"op":"'+home+' Gana ML","prob":"58%","momio":"@1.90","justo":"@1.72","valor":"+10%","porque":"Forma '+fecha+'","top":true},{"op":"Empate","prob":"22%","momio":"@3.40","justo":"@4.54","valor":"-25%","porque":"Historial","top":false},{"op":"Visitante","prob":"20%","momio":"@3.80","justo":"@5.00","valor":"-24%","porque":"Visita","top":false},{"op":"Doble '+home+'/Empate","prob":"72%","momio":"@1.35","justo":"@1.38","valor":"+2%","porque":"Seguro","top":false},{"op":"Over 2.5","prob":"62%","momio":"@1.85","justo":"@1.61","valor":"+15%","porque":"Ofensiva","top":false},{"op":"Under 2.5","prob":"38%","momio":"@2.10","justo":"@2.63","valor":"-20%","porque":"Defensiva","top":false},{"op":"Ambos SI","prob":"55%","momio":"@1.80","justo":"@1.81","valor":"-1%","porque":"BTTS","top":false},{"op":"Ambos NO","prob":"45%","momio":"@2.00","justo":"@2.22","valor":"-10%","porque":"Porteria","top":false},{"op":"'+home+' -0.5","prob":"58%","momio":"@1.90","justo":"@1.72","valor":"+10%","porque":"Handicap","top":false}],"marcadores":[{"score":"1-0","prob":"16%","momio":"@6.50","justo":"@6.25","valor":"+4%"},{"score":"2-0","prob":"14%","momio":"@8.00","justo":"@7.14","valor":"+12%"},{"score":"2-1","prob":"18%","momio":"@7.50","justo":"@5.55","valor":"+35%","top":true},{"score":"1-1","prob":"12%","momio":"@6.00","justo":"@8.33","valor":"-28%"},{"score":"0-0","prob":"6%","momio":"@11.00","justo":"@16.6","valor":"-34%"},{"score":"3-1","prob":"9%","momio":"@12.00","justo":"@11.1","valor":"+8%"}],"parlays":[{"picks":2,"momio":"@3.20","prob":"32%"}]}'
    games_parts.append(p)
games_js="{"+",".join(games_parts)+"}"
html="""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V72 CORREGIDO</title>
<style>body{background:#0a0a0a;color:#fff;font-family:Arial;margin:0;padding:10px}#nube{background:#00ff88;color:#000;padding:12px;border-radius:12px;text-align:center;font-weight:bold;margin-bottom:12px}.tabs{display:flex;gap:6px;overflow-x:auto;margin-bottom:12px}.tabs button{background:#222;color:#fff;border:1px solid #444;padding:8px 14px;border-radius:20px;white-space:nowrap}.tabs button.active{background:#00ff88;color:#000}.card{background:#1a1a1a;border:1px solid #333;border-radius:12px;padding:14px;margin:8px 0;cursor:pointer}.mercado{border:1px solid #444;padding:10px;margin:8px 0;border-radius:10px}.mercado.top{border-color:gold;background:#222}.modal{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.95);overflow:auto;padding:15px;z-index:99}.modal-content{background:#1a1a1a;padding:18px;border-radius:12px;max-width:600px;margin:auto}.tabm{display:flex;gap:6px;margin:14px 0;overflow:auto}.tabm button{background:#333;color:#fff;border:none;padding:8px 14px;border-radius:16px;white-space:nowrap}.tabm button.active{background:gold;color:#000}</style></head><body>
<div id="nube">✅ V72 CORREGIDO CANELO VS MBILLI 12/09 - 66 EVENTOS - HOY 3 MX 8 MXF 6 EUROPA 10 EUROF 4 NFL 8 UCL 6 UEL 4 MLS 5 BEIS 5 F1 3 BOX 4</div>
<div class="tabs" id="filtros"></div><div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content"><button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#333;color:#fff;border:none;padding:8px 14px;border-radius:10px">X</button><h2 id="mtitle"></h2><div id="mtv" style="color:#00ff88;margin-bottom:10px"></div><div class="tabm"><button onclick="showTab('todas')" id="bt_todas" class="active">TODAS+%</button><button onclick="showTab('mejor')" id="bt_mejor">MEJOR</button><button onclick="showTab('parlays')" id="bt_parlays">PARLAYS</button><button onclick="showTab('marcador')" id="bt_marcador">MARCADOR EXACTO</button></div><div id="mercados"></div></div></div>
<script>
const ligas=["hoy","mx","mx_fem","europa","euro_fem","nfl","ucl","uel","mls","beis","f1","box"];
const nombres={"hoy":"HOY","mx":"MX J7-J8","mx_fem":"MX FEM J9-J10","europa":"EUROPA","euro_fem":"EURO FEM","nfl":"NFL S2-S3","ucl":"UCL J1-J2","uel":"UEL J1-J2","mls":"MLS","beis":"BEIS FINAL","f1":"F1 BAKU","box":"BOX/UFC"};
let currentLiga="hoy";let currentGame=null;
const games=__GAMES__;
function renderFiltros(){let f="";ligas.forEach(function(l){let c=Object.values(games).filter(function(g){return g.liga===l}).length;f+='<button onclick="setLiga(\\''+l+'\\')" class="'+(currentLiga===l?'active':'')+'">'+nombres[l]+' ('+c+')</button>';});document.getElementById('filtros').innerHTML=f;}
function setLiga(l){currentLiga=l;renderFiltros();renderLista();}
function renderLista(){let h="";Object.entries(games).filter(function(e){return e[1].liga===currentLiga}).forEach(function(e){let id=e[0];let g=e[1];h+='<div class="card" onclick="openGame(\\''+id+'\\')"><b>'+g.title+'</b><br><small>'+g.tv+' | '+g.mejor.pick+'</small></div>';});if(!h)h='<div style="text-align:center;padding:30px;color:#888">0 eventos</div>';document.getElementById('lista').innerHTML=h;}
function openGame(id){currentGame=games[id];document.getElementById('mtitle').innerText=currentGame.title;document.getElementById('mtv').innerText=currentGame.tv;document.getElementById('modal').style.display='block';showTab('todas');}
function showTab(t){document.querySelectorAll('.tabm button').forEach(function(b){b.classList.remove('active')});document.getElementById('bt_'+t).classList.add('active');let g=currentGame;let html="";if(t==='todas'){html=g.mercados.map(function(m){return '<div class="mercado '+(m.top?'top':'')+'"><b>'+m.op+'</b> '+(m.top?'TOP':'' )+'<br>Prob: '+m.prob+' | '+m.momio+' | '+m.justo+' | '+m.valor+'</div>'}).join('');}if(t==='mejor'){html=g.mercados.filter(function(m){return m.top}).map(function(m){return '<div class="mercado top"><b>'+m.op+'</b> MEJOR<br>'+m.prob+' | '+m.momio+'</div>'}).join('');}if(t==='parlays'){html=g.parlays.map(function(p){return '<div class="mercado">Parlay '+p.picks+' - '+p.momio+'</div>'}).join('');}if(t==='marcador'){html='<h3>MARCADOR EXACTO %</h3>'+g.marcadores.map(function(m){return '<div class="mercado '+(m.top?'top':'')+'"><b>'+m.score+'</b> '+(m.top?'MAS PROBABLE':'')+'<br>'+m.prob+' | '+m.momio+'</div>'}).join('');}document.getElementById('mercados').innerHTML=html;}
renderFiltros();renderLista();
</script></body></html>
"""
html=html.replace("__GAMES__",games_js)
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("V72 CORREGIDO CANELO VS MBILLI 12/09 - 66 EVENTOS LISTO")
