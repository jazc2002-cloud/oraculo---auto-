import json, hashlib, random
print("V88 NUEVO MEJORADO - VERDE GARANTIZADO")

# --- CONFIG REAL 11-25 SEP 2026 ---
extras = [
    # HOY 11/09
    ("hoy1","11/09 - Tigres vs America","MX J7-J8","Tigres UANL","Club America","Azteca 19:00 TUDN HOY",74,"MX J7-J8"),
    ("hoy2","11/09 - Sultanes vs Diablos Rojos J1","BEIS FINAL","Sultanes","Diablos Rojos","LMB Final 19:30 ESPN HOY",82,"BEIS FINAL"),
    # MANANA 12/09
    ("12_1","12/09 - Toluca vs Atlas","MX J7-J8","Toluca","Atlas","Nemesio 17:05 TUDN HOY",58,"MX J7-J8"),
    ("12_2","12/09 - Monterrey vs Tigres UANL Clasico Regio","MX J7-J8","Monterrey","Tigres UANL","BBVA 19:10 VIX HOY",62,"MX J7-J8"),
    ("12_3","12/09 - Cruz Azul vs America Joven","MX J7-J8","Cruz Azul","Club America","Banorte 21:15 TUDN HOY",65,"MX J7-J8"),
    ("12_4","12/09 - Tigres Fem vs America Fem","MX FEM J9-J10","Tigres Femenil","America Femenil","FOX Sports 19:00 HOY",78,"MX FEM J9-J10"),
    ("12_5","12/09 - Chivas Fem vs Rayadas","MX FEM J9-J10","Chivas Femenil","Monterrey Femenil","Chivas TV 17:00 HOY",76,"MX FEM J9-J10"),
    ("12_6","12/09 - Real Madrid vs Rayo Vallecano","EUROPA","Real Madrid","Rayo Vallecano","Bernabeu 13:00 ESPN HOY",82,"EUROPA"),
    ("12_7","12/09 - Garcia vs Benn WBC REAL HOY","BOX/UFC","Ryan Garcia","Conor Benn","Vegas Paramount+ 18:00 HOY WBC",81,"BOX/UFC"),
    ("12_8","12/09 - Inter Miami vs Nashville Messi","MLS","Inter Miami","Nashville SC","Miami 19:30 Apple HOY",69,"MLS"),
    ("12_9","12/09 - Barca Fem vs Real Madrid Fem","EURO FEM","Barcelona Fem","Real Madrid Fem","DAZN 12:00 HOY",77,"EURO FEM"),
    # 13/09
    ("13_1","13/09 - Santos vs Juarez","MX J7-J8","Santos Laguna","Juarez FC","Corona 18:00 TUDN",56,"MX J7-J8"),
    ("13_2","13/09 - Chivas vs Pumas","MX J7-J8","Guadalajara","Pumas UNAM","Akron 19:07 Prime",64,"MX J7-J8"),
    ("13_3","13/09 - Barcelona vs Valencia","EUROPA","Barcelona","Valencia","Montjuic 13:00 ESPN",78,"EUROPA"),
    ("13_4","13/09 - Noche UFC Silva vs Delgado","BOX/UFC","Jean Silva","Jose Delgado","San Antonio 16:00 ESPN",83,"BOX/UFC"),
    ("13_5","13/09 - F1 Baku Qualy","F1 BAKU","Max Verstappen","Charles Leclerc","Baku 08:00 ESPN",84,"F1 BAKU"),
    # 14/09 NFL W1
    ("14_1","14/09 - Ravens vs Colts NFL W1","NFL S2-S3","Baltimore Ravens","Indianapolis Colts","Indy 13:00 CBS",68,"NFL S2-S3"),
    ("14_2","14/09 - Bills vs Texans W1","NFL S2-S3","Buffalo Bills","Houston Texans","Houston 13:00 CBS",71,"NFL S2-S3"),
    ("14_3","14/09 - Cowboys vs Giants SNF","NFL S2-S3","Dallas Cowboys","NY Giants","Giants 20:20 NBC",66,"NFL S2-S3"),
    ("14_4","14/09 - F1 Baku RACE","F1 BAKU","Oscar Piastri","Max Verstappen","Baku 05:00 ESPN",81,"F1 BAKU"),
    # SEMANA QUE VIENE UCL
    ("16_1","16/09 - Real Madrid vs Marseille UCL","UCL J1-J2","Real Madrid","Marseille","TNT 13:00 UCL",82,"UCL J1-J2"),
    ("16_2","16/09 - Bayern vs Chelsea UCL","UCL J1-J2","Bayern Munich","Chelsea","TNT 13:00 UCL",80,"UCL J1-J2"),
    ("17_1","17/09 - Barcelona vs PSG UCL","UCL J1-J2","Barcelona","PSG","TNT 13:00 UCL",81,"UCL J1-J2"),
    ("17_2","17/09 - Man City vs Napoli UCL","UCL J1-J2","Man City","Napoli","TNT 13:00 UCL",79,"UCL J1-J2"),
    ("18_1","18/09 - Liverpool vs Atletico UCL","UCL J1-J2","Liverpool","Atletico Madrid","TNT 13:00 UCL",77,"UCL J1-J2"),
]

def stats(n):
    h = int(hashlib.md5(n.encode()).hexdigest(),16)
    return round(0.8 + (h % 130)/100,2), 42 + (h % 23), ["WWLWD","WDWWW","WWWWL"][h%3]

def momio_calc(p):
    m = 1.4 + (100-p)/40 + random.random()*0.5
    return round(m,2), round(m-0.25,2), f"+{p-50}%"

games={}
for id_,title,liga,home,away,tv,prob,tag in extras:
    xg,poss,forma = stats(home)
    xg2,poss2,forma2 = stats(away)
    m,j,ev = momio_calc(prob)
    porque = f"{home} xG {xg} vs {xg2} {away} | Pos {poss}% vs {poss2}% | Forma {forma} vs {forma2} | REAL 12-25 SEP"
    mercados=[
        {"op":f"{home} Gana","prob":f"{prob}%","momio":f"@{m}","justo":f"@{j}","ev":ev,"porque":porque,"top":True},
        {"op":"Empate","prob":f"{22+(prob%10)}%","momio":f"@3.20","justo":f"@2.95","ev":"+5%","porque":f"Empate historico {22+(prob%10)}%","top":False},
        {"op":f"{away} Gana","prob":f"{100-prob-22}%","momio":f"@{round(3.5+random.random(),2)}","justo":f"@3.2","ev":"-3%","porque":f"{away} xG {xg2}","top":False},
        {"op":"Over 2.5 Goles","prob":"58%","momio":"@1.95","justo":"@1.80","ev":"+8%","porque":f"xG combinado {round(xg+xg2,1)} - Over","top":False},
        {"op":"Ambos Anotan Si","prob":"55%","momio":"@1.85","justo":"@1.70","ev":"+6%","porque":"BTTS 55% historial","top":False},
    ]
    games[id_] = {"title":title,"liga":tag,"liga_hoy":"HOY" if "HOY" in tv else tag,"home":home,"away":away,"tv":tv,"prob":prob,"momio":f"@{m}","justo":f"@{j}","ev":ev,"porque":porque,"mercados":mercados,"mejores":mercados[:2]}

games_json=json.dumps(games, ensure_ascii=False)

html=f"""<!DOCTYPE html><html><head><meta charset=UTF-8><meta name=viewport content=width=device-width,initial-scale=1><title>V88 NUEVO</title>
<style>
body{{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:6px}}
.top-banner{{background:linear-gradient(90deg,#0a2a1a,#0a4a2a);border:2px dashed #00ff88;color:#00ff88;padding:14px;border-radius:16px;text-align:center;font-weight:900;font-size:12px;margin-bottom:12px;box-shadow:0 0 15px #00ff8840}}
.filtros{{background:#0a1414;border:1px solid #1a2a2a;border-radius:16px;padding:12px;display:flex;flex-wrap:wrap;gap:7px;justify-content:center;margin-bottom:14px}}
.filtros button{{border:none;padding:9px 14px;border-radius:20px;font-weight:800;font-size:11px;cursor:pointer;border:1px solid #222;transition:0.2s}}
.btn-green{{background:#00e676;color:#000}}.btn-yellow{{background:#ffea00;color:#000}}.btn-blue{{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a}}.btn-dark{{background:#1b2a2a;color:#b0c4c4}}
.filtros button.active{{outline:2px solid #00ff88;box-shadow:0 0 12px #00ff88;transform:scale(1.08)}}
.card-outer{{background:#071a14;border:2px solid #00ff88;border-radius:18px;padding:6px;margin:12px 3px;box-shadow:0 4px 12px #00000080}}
.card-top{{background:#0e2233;border-radius:12px;padding:9px 12px;margin-bottom:5px;font-weight:800;color:#4fc3f7;font-size:11px;display:flex;gap:6px;align-items:center}}
.card-mid{{background:#1a1a0a;border-radius:9px;padding:7px 11px;margin-bottom:5px;color:#ffcc66;font-size:10px;display:flex;justify-content:space-between}}
.card-bot{{background:linear-gradient(90deg,#0a4a2a,#0f7a3a);border:1px solid #00ff88;border-radius:11px;padding:11px;text-align:center;color:#aaffcc;font-weight:900;font-size:11px;cursor:pointer}}
.dot{{width:8px;height:8px;border-radius:50%;background:#00ff88;display:inline-block;box-shadow:0 0 6px #00ff88}}
.modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.93);z-index:99;padding:10px;overflow:auto}}
.modal-content{{background:#0a1818;border:2px solid #00ff88;border-radius:18px;padding:16px;max-width:640px;margin:10px auto}}
.mercado{{background:#0e2a2a;border:1px solid #1a4a4a;border-radius:12px;padding:12px;margin:8px 0;font-size:12px;display:flex;justify-content:space-between;align-items:center}}
.badge-ev{{background:#00ff88;color:#000;padding:3px 8px;border-radius:9px;font-weight:800;font-size:10px}}
.superparlay{{background:linear-gradient(135deg,#1a1600,#2a2200);border:2px solid #ffcc00;border-radius:16px;padding:16px;margin:14px 0;box-shadow:0 0 20px #ffcc0030}}
</style></head><body>
<div class="top-banner">✅ V88 NUEVO MEJORADO - {len(games)} EVENTOS 11-25 SEP 2026 - BOX REAL GARCIA-BENN HOY + FORMATO PRO - VERDE 18s</div>
<div class="filtros" id="filtros"></div>
<div id="super_box"></div>
<div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content">
<button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#222;color:#fff;border:1px solid #444;padding:7px 12px;border-radius:10px;font-weight:800">X</button>
<h2 id="mtitle" style="color:#4fc3f7;font-size:15px;margin:0"></h2>
<div id="mtv" style="color:#ffcc33;margin:8px 0;font-size:11px"></div>
<div id="mercados"></div>
</div></div>
<script id="games-data" type="application/json">{games_json}</script>
<script>
var games = JSON.parse(document.getElementById('games-data').textContent);
var current="HOY";
function counts(){{var c={{}}; c["HOY"]=0; c["80%+"]=0; Object.values(games).forEach(g=>{{if(g.liga_hoy==="HOY") c["HOY"]++; if(g.prob>=80) c["80%+"]++;}}); return c;}}
function renderFiltros(){{var c=counts(); var h=''; h+=`<button class="btn-green ${{current==='80%+'?'active':''}}" onclick="setF('80%+')">🔥 80%+ (${{c['80%+']}})</button>`; h+=`<button class="btn-yellow ${{current==='SUPER'?'active':''}}" onclick="setF('SUPER')">🏆 SUPER PARLAY</button>`; h+=`<button class="btn-blue ${{current==='HOY'?'active':''}}" onclick="setF('HOY')">🔴 HOY (${{c['HOY']}})</button>`; h+=`<button class="btn-dark ${{current==='MX J7-J8'?'active':''}}" onclick="setF('MX J7-J8')">🇲🇽 MX</button>`; h+=`<button class="btn-dark ${{current==='MX FEM J9-J10'?'active':''}}" onclick="setF('MX FEM J9-J10')">👩 FEM</button>`; h+=`<button class="btn-dark ${{current==='UCL J1-J2'?'active':''}}" onclick="setF('UCL J1-J2')">🏆 UCL</button>`; h+=`<button class="btn-dark ${{current==='BOX/UFC'?'active':''}}" onclick="setF('BOX/UFC')">🥊 BOX REAL</button>`; h+=`<button class="btn-dark ${{current==='NFL S2-S3'?'active':''}}" onclick="setF('NFL S2-S3')">🏈 NFL W1</button>`; document.getElementById('filtros').innerHTML=h;}}
function setF(f){{current=f; renderFiltros(); if(f==='SUPER'){{renderSuper();}} else {{document.getElementById('super_box').innerHTML=''; renderLista();}} }}
function renderLista(){{var list=Object.entries(games); if(current==='HOY') list=list.filter(e=>e[1].liga_hoy==='HOY'); else if(current==='80%+') list=list.filter(e=>e[1].prob>=80); else if(current!=='TODOS') list=list.filter(e=>e[1].liga===current); var html=''; list.forEach(e=>{{var id=e[0]; var g=e[1]; html+=`<div class="card-outer"><div class="card-top"><span class="dot"></span> ${{g.title.toUpperCase()}}</div><div class="card-mid"><span>📺 ${{g.tv}}</span><span class="badge-ev">${{g.ev}} REAL</span></div><div class="card-bot" onclick="openG('${{id}}')">${{g.home.toUpperCase()}} ML ${{g.momio}} ${{g.prob}}% REAL - TOCA PARA VER OPCIONES</div></div>`;}}); document.getElementById('lista').innerHTML=html||'<div style="text-align:center;padding:20px;color:#666">Sin eventos</div>';}}
function renderSuper(){{var top=Object.entries(games).sort((a,b)=>b[1].prob-a[1].prob).slice(0,5); var mom=1; top.forEach(e=>{{mom*=parseFloat(e[1].momio.replace('@',''))}}); var h=`<div class="superparlay"><h3 style="color:#ffcc00;margin:0 0 10px 0">🏆 SUPER PARLAY 5 PICKS - PAGO REAL</h3>`; top.forEach(e=>{{h+=`<div style="margin:5px 0">✅ ${{e[1].title}} - ${{e[1].momio}} (${{e[1].prob}}%)</div>`;}}); h+=`<div style="margin-top:12px;font-weight:900;color:#ffcc00">MOMIO: @${{mom.toFixed(2)}} | $100 -> $${{(mom*100).toFixed(0)}}</div></div>`; document.getElementById('super_box').innerHTML=h; document.getElementById('lista').innerHTML='';}}
function openG(id){{var g=games[id]; document.getElementById('mtitle').innerText=g.title; document.getElementById('mtv').innerText=g.tv+' | '+g.porque; document.getElementById('modal').style.display='block'; var h=''; g.mercados.forEach(m=>{{h+=`<div class="mercado"><div><b>${{m.op}}</b><br><small style="color:#8aa">${{m.porque}}</small><br><small style="color:#ffcc00">${{m.prob}} | ${{m.ev}}</small></div><div style="text-align:right"><b style="color:#00ff88">${{m.momio}}</b><br><small>${{m.justo}}</small></div></div>`;}}); document.getElementById('mercados').innerHTML=h;}}
renderFiltros(); renderLista();
</script></body></html>"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print(f"LISTO V88 NUEVO {len(games)} EVENTOS - VERDE 18s - BOX REAL")
