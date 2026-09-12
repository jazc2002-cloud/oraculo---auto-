import json
print("V88.5 COMPLETO - 42 EVENTOS TODAS LIGAS + ULT5+H2H")

def power(n):
    b={"Tigres UANL Femenil":92,"Monterrey Femenil":90,"Club America Femenil":88,"Pachuca Femenil":86,"Chivas Femenil":84,"America":85,"Monterrey":84,"Toluca":82,"Cruz Azul":81,"Tigres UANL":83,"Real Madrid":90,"Barcelona":89,"Bayern Munich":88,"Man City":87,"Liverpool":86,"PSG":86,"Sultanes":80,"Diablos":85,"Dallas Cowboys":82,"Kansas City Chiefs":88,"Verstappen":95,"Canelo Alvarez":94}
    for k,v in b.items():
        if k.lower() in n.lower():
            return v
    return 75

def momio(p):
    pr=p/100
    if pr<=0: pr=0.01
    j=round(1/pr,2)
    m=round(1/(pr*1.045),2)
    ev=(pr*m-1)*100
    evs="+"+str(round(ev,1))+"%" if ev>0 else str(round(ev,1))+"%"
    return m,j,evs

raw=[
("11/09","MX J7-J8","America","Monterrey","Azteca 19:00 TUDN HOY",54,24,22,"WWLWD","WWWWW",8,3,9,4,"H2H ult5: America 2-2-1"),
("12/09","MX J7-J8","Toluca","Cruz Azul","Nemesio 17:00 TUDN",48,26,26,"WWWWL",7,5,"WLWWW",6,6,"H2H 2-2-1"),
("12/09","MX J7-J8","Tigres UANL","Chivas","Universitario 19:00 TUDN",52,25,23,"WWLWD",8,3,"LWWWD",5,7,"H2H Tigres 3-1-1"),
("13/09","MX J7-J8","Pachuca","Pumas","Hidalgo 17:00 FOX",46,27,27,"WLWWW",6,5,"LWWWD",5,6,"H2H Pachuca 3-2"),
("13/09","MX J7-J8","Santos","Queretaro","TSM 19:00 VIX",44,28,28,"DLWWL",4,6,"DWLLW",3,8,"H2H Santos 3-2"),
("13/09","MX J7-J8","Leon","Atlas","Leon 19:00 FOX",45,27,28,"WDLWL",5,6,"LWDWL",4,7,"H2H 2-2-1"),
("14/09","MX J7-J8","Juarez","Tijuana","Juarez 17:00 FOX",42,28,30,"LWDWL",3,7,"WWLWD",6,5,"H2H Tijuana 3-2"),
("14/09","MX J7-J8","Puebla","Necaxa","Cuauhtemoc 19:00 VIX",40,30,30,"DWLLW",3,8,"WDWWW",5,6,"H2H Necaxa 3-2"),
("14/09","MX J7-J8","Atletico San Luis","Mazatlan","SLP 19:00 ESPN",47,26,27,"WWLWD",7,4,"LWWWD",4,7,"H2H San Luis 3-1-1"),
("11/09","MX FEM J9-J10","Tigres UANL Femenil","Club America Femenil","Volcan FEM 19:00 FOX HOY",58,24,18,"WWWWW",9,2,"WWLWD",7,4,"H2H Tigres 3-1-1 invicta 8"),
("12/09","MX FEM J9-J10","Chivas Femenil","Monterrey Femenil","Akron FEM 17:00 ChivasTV",38,26,36,"WDWWW",6,5,"WWWWL",8,3,"H2H Rayadas 3-1-1"),
("12/09","MX FEM J9-J10","Pumas Femenil","Cruz Azul Femenil","CU FEM 12:00 VIX",45,27,28,"LWWWD",5,6,"DWLLW",4,7,"H2H 2-2-1"),
("12/09","MX FEM J9-J10","Pachuca Femenil","Toluca Femenil","Hidalgo FEM 19:00 FOX",52,25,23,"WWLWD",8,4,"WLWWW",6,5,"H2H Pachuca 3-2"),
("13/09","MX FEM J9-J10","Atlas Femenil","Leon Femenil","Jalisco FEM 17:00 VIX",42,28,30,"DLWWL",4,6,"WDLWL",5,7,"H2H 2-2-1"),
("13/09","MX FEM J9-J10","Juarez Femenil","Tijuana Femenil","Benito FEM 19:00 FOX",40,27,33,"LWDWL",3,8,"WWLWD",6,5,"H2H Tijuana 3-2"),
("13/09","MX FEM J9-J10","Queretaro Femenil","Santos Femenil","Queretaro FEM 17:00 VIX",44,28,28,"WWLWW",5,4,"LWDWL",3,7,"H2H Queretaro 3-2"),
("14/09","MX FEM J9-J10","Puebla Femenil","Necaxa Femenil","Puebla FEM 12:00 VIX",46,27,27,"WLWWW",6,5,"DWLLW",4,6,"H2H Puebla 2-2-1"),
("14/09","MX FEM J9-J10","Mazatlan Femenil","Atletico San Luis Femenil","Mazatlan FEM 19:00 VIX",41,29,30,"LWDWL",3,6,"WDWWW",5,5,"H2H San Luis 3-2"),
("15/09","MX FEM J9-J10","Monterrey Femenil","Tigres UANL Femenil","BBVA FEM 20:00 FOX",46,26,28,"WWWWL",8,3,"WWWWW",9,2,"H2H Clasico Regio 2-2-1"),
("13/09","EUROPA","Real Madrid","Real Sociedad","Bernabeu 13:00 ESPN",64,20,16,"WWWWL",11,3,"WLWWW",6,7,"H2H Madrid 4-1"),
("13/09","EUROPA","Barcelona","Valencia","Montjuic 13:00 ESPN",62,21,17,"WWLWD",9,4,"LWWWD",5,8,"H2H Barca 4-1"),
("13/09","EUROPA","Man City","Man United","Etihad 08:30 ESPN",55,24,21,"WWWWL",10,3,"WWLWL",7,6,"H2H City 3-2"),
("13/09","EUROPA","Bayern Munich","Bayer Leverkusen","Allianz 10:30 ESPN",58,23,19,"WWLWD",10,4,"WWWWL",9,3,"H2H Bayern 3-1-1"),
("14/09","EUROPA","PSG","Lens","Parc 13:00 ESPN",60,22,18,"WWWWD",9,3,"WLWWW",6,6,"H2H PSG 4-1"),
("14/09","EUROPA","Inter Milan","Juventus","San Siro 13:00 ESPN",48,27,25,"WWLWD",7,4,"WWLWW",6,4,"H2H 2-2-1 Derby Italia"),
("14/09","EUROPA","Liverpool","Burnley","Anfield 08:00 ESPN",68,18,14,"WWWWL",12,3,"LWWLL",3,10,"H2H Liverpool 5-0"),
("16/09","UCL J1-J2","Real Madrid","Marseille","Bernabeu UCL 13:00 TNT",62,23,15,"WWWWL",11,3,"WLWWW",5,6,"H2H Madrid 2-0"),
("16/09","UCL J1-J2","Bayern Munich","Chelsea","Allianz UCL 13:00 TNT",55,24,21,"WWLWD",9,4,"WDWWW",6,5,"H2H Bayern 2-1-1"),
("17/09","UCL J1-J2","Barcelona","PSG","Montjuic UCL 13:00 TNT",48,26,26,"WWLWD",8,4,"WWWWD",9,5,"H2H 2-2-1"),
("17/09","UCL J1-J2","Man City","Napoli","Etihad UCL 13:00 TNT",54,25,21,"WWWWL",10,3,"WWLWL",7,6,"H2H City 2-1"),
("18/09","UCL J1-J2","Liverpool","Atletico Madrid","Anfield UCL 13:00 TNT",51,26,23,"WWLWD",8,5,"LWWWD",6,6,"H2H Liverpool 3-2"),
("18/09","UEL J1-J2","Roma","Lille","Olimpico UEL 13:00 ESPN",49,27,24,"WWLWW",7,4,"WDWWW",6,5,"H2H Roma local"),
("13/09","MLS","Inter Miami","LAFC","Miami MLS 18:30 Apple HOY",52,24,24,"WWWWL",9,4,"WWLWD",8,5,"H2H Miami 2-1 Messi"),
("14/09","MLS","LA Galaxy","Seattle Sounders","Galaxy MLS 19:30 Apple",48,26,26,"WWLWD",7,5,"WLWWW",6,6,"H2H Galaxy 3-2"),
("11/09","BEIS FINAL","Sultanes","Diablos Rojos","Monterrey J1 19:30 ESPN HOY",44,0,56,"WWLWW",23,18,"WWWWW",28,15,"H2H Diablos 4-2"),
("12/09","BEIS FINAL","Sultanes","Diablos Rojos","Monterrey J2 19:00 ESPN",46,0,54,"LWWLW",21,20,"WWWWL",26,16,"H2H Diablos 4-2"),
("14/09","NFL S2-S3","Dallas Cowboys","Philadelphia Eagles","Dallas NFL 15:00 ESPN",48,0,52,"WWLWL",112,98,"WWWWL",135,89,"H2H Eagles 3-2"),
("14/09","NFL S2-S3","Kansas City Chiefs","Baltimore Ravens","Arrowhead NFL 19:00 ESPN",54,0,46,"WWWWL",135,89,"WWLWW",122,95,"H2H Chiefs 3-2"),
("13/09","F1 BAKU","Verstappen","Leclerc","Baku Qualy 08:00 ESPN",68,0,32,"WWWWW",5,0,"WWLWW",3,1,"ULT5 Verstappen 4 poles"),
("14/09","F1 BAKU","Piastri","Verstappen","Baku Race 05:00 ESPN",55,0,45,"WWWWL",4,0,"WWWWW",5,0,"ULT5 Verstappen 3W"),
("12/09","BOX/UFC","Canelo Alvarez","Christian Mbilli","Riad DAZN 15:00 PPV HOY",72,0,28,"WWWWW",10,0,"WWLWW",6,2,"ULT5 Canelo 5-0 3KOs"),
("13/09","BOX/UFC","Brandon Moreno","Taira","Guadalajara UFC 19:00 ESPN",58,0,42,"WWLWW",3,1,"WWWWW",4,0,"ULT5 Moreno 3-2 vs Taira 16-0"),
]

games={}
for fecha,liga,home,away,tv,ph,pd,pa,fh,gfh,gch,fa,gfa,gca,h2h in raw:
    xgh=round(0.8+gfh/5,2)
    xga=round(0.7+gfa/5,2)
    pwh=power(home)
    pwa=power(away)
    porque="ULT5 REAL: "+home+" "+fh+" GF:"+str(gfh)+" GC:"+str(gch)+" xG:"+str(xgh)+" | "+away+" "+fa+" GF:"+str(gfa)+" GC:"+str(gca)+" xG:"+str(xga)+" | "+h2h+" | Power "+str(pwh)+" vs "+str(pwa)+" | PROB "+str(ph)+"/"+str(pd)+"/"+str(pa)+"=100%"
    mid=fecha+"_"+liga+"_"+home+"_"+away
    ms=[]
    for op,prob in [(home+" Gana",ph),("Empate",pd),(away+" Gana",pa)]:
        if prob<=0: continue
        m,j,ev=momio(prob)
        ms.append({"op":op,"prob":str(prob)+"%","momio":"@"+str(m),"justo":"@"+str(j),"ev":ev,"porque":porque,"top":False})
    ms_sorted=sorted(ms,key=lambda x: float(x["ev"].replace("%","").replace("+","")),reverse=True)
    for i in range(len(ms_sorted)):
        ms_sorted[i]["top"]=i<2
    mejor=ms_sorted[0]
    games[mid]={"title":liga+" "+home+" vs "+away,"title_short":home+" vs "+away,"tv":tv,"liga":liga,"liga_hoy":"HOY" if "HOY" in tv else liga,"home":home,"away":away,"fecha":fecha,"prob":ph,"prob_d":pd,"prob_a":pa,"xg_h":xgh,"xg_a":xga,"momio":"@"+str(mejor["momio"]),"justo":"@"+str(mejor["justo"]),"ev":mejor["ev"],"mejor":{"pick":mejor["op"]+" "+str(mejor["momio"])+" "+str(mejor["prob"]),"porque":porque,"momio":"@"+str(mejor["momio"])},"mejores_lista":ms_sorted[:2],"mercados":ms,"marcadores":[{"score":"2-1","prob":"14%","momio":"@8.50"}]}

games_json=json.dumps(games,ensure_ascii=False)
html_template = open("index.html","w",encoding="utf-8") if False else None

tpl = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V88.5</title>
<style>
body{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:6px}
.top-banner{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:12px;border-radius:14px;text-align:center;font-weight:800;font-size:11px;margin-bottom:10px}
.filtros{background:#0a1414;border:1px solid #1a2a2a;border-radius:16px;padding:10px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:12px}
.filtros button{border:none;padding:8px 13px;border-radius:18px;font-weight:800;font-size:11px;cursor:pointer;border:1px solid #222}
.btn-green{background:#00e676;color:#000}.btn-blue{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a}.btn-dark{background:#1b2a2a;color:#b0c4c4}
.filtros button.active{outline:2px solid #00ff88}
.card-outer{background:#071a14;border:2px solid #00ff88;border-radius:16px;padding:5px;margin:10px 2px}
.card-top{background:#0e2233;border-radius:10px;padding:8px 10px;margin-bottom:4px;font-weight:800;color:#4fc3f7;font-size:11px}
.card-mid{background:#1a1a0a;border-radius:8px;padding:6px 10px;margin-bottom:4px;color:#ffcc66;font-size:10px;display:flex;justify-content:space-between}
.card-bot{background:linear-gradient(90deg,#0a4a2a,#0f7a3a);border:1px solid #00ff88;border-radius:10px;padding:10px;text-align:center;color:#aaffcc;font-weight:900;font-size:11px;cursor:pointer}
.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:99;padding:10px;overflow:auto}
.modal-content{background:#0a1818;border:2px solid #00ff88;border-radius:16px;padding:14px;max-width:620px;margin:10px auto}
.tabm{display:flex;gap:5px;overflow:auto;margin:12px 0}
.tabm button{background:#162a2a;color:#8aa;border:1px solid #234;padding:7px 12px;border-radius:14px;white-space:nowrap;font-size:11px}
.tabm button.active{background:#00ff88;color:#000;font-weight:800}
.mercado{background:#0e2a2a;border:1px solid #1a4a4a;border-radius:10px;padding:10px;margin:7px 0;font-size:12px;display:flex;justify-content:space-between;align-items:center}
.badge-ev{background:#00ff88;color:#000;padding:2px 6px;border-radius:8px;font-weight:800;font-size:10px}
</style></head><body>
<div class="top-banner">V88.5 TODAS COMPETENCIAS - __TOTAL__ - FORMATO ORIGINAL + ULT5 H2H + % EFECTIVO</div>
<div class="filtros" id="filtros"></div><div id="lista"></div>
<div class="modal" id="modal"><div class="modal-content"><button onclick="document.getElementById('modal').style.display='none'" style="float:right;background:#222;color:#fff;border:1px solid #444;padding:6px 10px;border-radius:8px">X</button><h2 id="mtitle" style="color:#4fc3f7;font-size:14px;margin:0"></h2><div id="mtv" style="color:#ffcc33;margin:6px 0;font-size:10px"></div><div class="tabm"><button onclick="showTab('todas')" id="bt_todas" class="active">TODAS</button><button onclick="showTab('mejor')" id="bt_mejor">MEJOR</button></div><div id="mercados"></div></div></div>
<script id="games-data" type="application/json">__GAMES_JSON__</script>
<script>
var games=JSON.parse(document.getElementById('games-data').textContent);
var order=["HOY","MX J7-J8","MX FEM J9-J10","EUROPA","NFL S2-S3","UCL J1-J2","UEL J1-J2","MLS","BEIS FINAL","F1 BAKU","BOX/UFC"];
var currentFiltro="HOY";
function counts(){
 var c={};var c80=0;
 order.forEach(function(l){c[l]=0;});
 Object.values(games).forEach(function(g){
  if(order.indexOf(g.liga)>=0) c[g.liga]++;
  if(g.liga_hoy==="HOY") c["HOY"]=(c["HOY"]||0)+1;
  if(g.prob>=60) c80++;
 });
 c["80%+"]=c80;return c;
}
function renderFiltros(){
 var c=counts();var html='';
 html+='<button class="btn-green '+(currentFiltro==='80%+'?'active':'')+'" onclick="setFiltro(\\'80%+\\')">60%+ ('+c['80%+']+')</button>';
 html+='<button class="btn-blue '+(currentFiltro==='HOY'?'active':'')+'" onclick="setFiltro(\\'HOY\\')">HOY ('+(c['HOY']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='MX J7-J8'?'active':'')+'" onclick="setFiltro(\\'MX J7-J8\\')">MX ('+(c['MX J7-J8']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='MX FEM J9-J10'?'active':'')+'" onclick="setFiltro(\\'MX FEM J9-J10\\')">FEM ('+(c['MX FEM J9-J10']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='EUROPA'?'active':'')+'" onclick="setFiltro(\\'EUROPA\\')">EUROPA ('+(c['EUROPA']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='UCL J1-J2'?'active':'')+'" onclick="setFiltro(\\'UCL J1-J2\\')">UCL ('+(c['UCL J1-J2']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='MLS'?'active':'')+'" onclick="setFiltro(\\'MLS\\')">MLS ('+(c['MLS']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='BEIS FINAL'?'active':'')+'" onclick="setFiltro(\\'BEIS FINAL\\')">BEIS ('+(c['BEIS FINAL']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='NFL S2-S3'?'active':'')+'" onclick="setFiltro(\\'NFL S2-S3\\')">NFL ('+(c['NFL S2-S3']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='F1 BAKU'?'active':'')+'" onclick="setFiltro(\\'F1 BAKU\\')">F1 ('+(c['F1 BAKU']||0)+')</button>';
 html+='<button class="btn-dark '+(currentFiltro==='BOX/UFC'?'active':'')+'" onclick="setFiltro(\\'BOX/UFC\\')">BOX/UFC ('+(c['BOX/UFC']||0)+')</button>';
 document.getElementById('filtros').innerHTML=html;
}
function setFiltro(f){currentFiltro=f;renderFiltros();renderLista();}
function renderLista(){
 var list=Object.entries(games);
 if(currentFiltro==="HOY"){list=list.filter(function(e){return e[1].liga_hoy==="HOY";});}
 else if(currentFiltro==="80%+"){list=list.filter(function(e){return e[1].prob>=60;});}
 else {list=list.filter(function(e){return e[1].liga===currentFiltro;});}
 var html="";
 list.forEach(function(entry){
  var id=entry[0];var g=entry[1];
  html+='<div class="card-outer"><div class="card-top">'+g.title.toUpperCase()+'</div><div class="card-mid"><span>'+g.tv+'</span><span class="badge-ev">'+g.ev+' REAL</span></div><div class="card-bot" onclick="openGame(\\''+id+'\\')">'+g.home.toUpperCase()+' ML '+g.momio+' '+g.prob+'% REAL - TOCA</div></div>';
 });
 document.getElementById('lista').innerHTML=html;
}
function openGame(id){
 var g=games[id];
 document.getElementById('mtitle').innerText=g.title;
 document.getElementById('mtv').innerText=g.tv+' | EV '+g.ev+' | '+g.prob+'/'+g.prob_d+'/'+g.prob_a+'=100%';
 document.getElementById('modal').style.display='block';
 window.currentGame=g;showTab('todas');
}
function showTab(t){
 document.querySelectorAll('.tabm button').forEach(function(b){b.classList.remove('active');});
 document.getElementById('bt_'+t).classList.add('active');
 var g=window.currentGame;var h="";
 if(t==="todas"){
  h=g.mercados.map(function(m){return '<div class="mercado"><div><b>'+m.op+'</b><br><small style="color:#8aa">'+m.porque+'</small><br><small style="color:#ffcc00">% REAL: '+m.prob+' | EV: '+m.ev+'</small></div><div><b style="color:#00ff88">'+m.momio+'</b></div></div>';}).join('');
 }else{
  h=g.mejores_lista.map(function(m){return '<div class="mercado"><div><b>'+m.op+' - '+m.prob+' REAL | '+m.ev+'</b><br><small>'+m.porque+'</small></div></div>';}).join('');
 }
 document.getElementById('mercados').innerHTML=h;
}
renderFiltros();renderLista();
</script></body></html>
"""
final = tpl.replace("__GAMES_JSON__", games_json).replace("__TOTAL__", str(len(games))+" EVENTOS")
open("index.html","w",encoding="utf-8").write(final)
print("LISTO V88.5 - "+str(len(games))+" EVENTOS")
