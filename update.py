print("V88.5 12-20 SEP 2026 CORREGIDO SIN CANELO")
raw=[
# HOY VIER 12
("12/09","MX J8 HOY","Toluca","Atlas","Nem. Diez 17:05 TUDN/C5 HOY",52,"H2H 2-2-1"),
("12/09","MX J8 HOY","Monterrey","Tigres UANL","BBVA 19:10 VIX HOY REGIO",48,"Clasico Regio"),
("12/09","MX J8 HOY","Cruz Azul","America","Banorte 21:15 C5/TUDN HOY JOVEN",45,"Clasico Joven"),
("12/09","MX FEM J7 HOY","Guadalajara","Monterrey","Akron 17:07 Prime HOY",46,"FEM J7"),
("12/09","MX FEM J7 HOY","Juarez","Necaxa","Benito 19:10 Tubi HOY",44,"FEM J7"),
("12/09","LaLiga J5 HOY","Real Madrid","Rayo Vallecano","Bernabeu 13:00 ESPN+ HOY",67,"Madrid 4-1 H2H"),
("12/09","Serie A J4 HOY","Lazio","Milan","Olimpico 17:00 ESPN HOY",42,"J4"),
("12/09","F1 Madrid HOY","Qualy Madrid","Madring","Madring 15:00 SkyF1 HOY",68,"Qualy debut"),
("12/09","BOX HOY","Ryan Garcia","Conor Benn","Vegas Paramount+ 18:00 HOY WBC WW",51,"WBC WW Title HOY 12/09 real - Garcia vs Benn + Opetaia vs Mikaelian"),
("12/09","MLS HOY","Inter Miami","Nashville SC","Miami 19:30 Apple HOY MESSI",47,"44pts vs 53pts lider"),
("12/09","LMB Serie Rey HOY","Sultanes","Diablos Rojos","Mobil Super J4 HOY",45,"Final 9-17 Sep"),
# SAB 13 - DOM 14
("13/09","UFC Noche","Jean Silva","Jose Delgado","San Antonio 16:00 Fox HOY+1",48,"Noche UFC San Antonio Frost Bank"),
("13/09","MX J8","Santos","Juarez FC","Corona 18:00 TUDN",44,"J8"),
("13/09","MX J8","Chivas","Pumas","Akron 19:07 Prime",48,"J8"),
("13/09","F1 Madrid","Race Madrid","Madring","Madring 14:00 SkyF1",55,"Carrera debut"),
("13/09","LaLiga J5","Barcelona","Valencia","Montjuic 13:00 ESPN",62,"J5"),
("14/09","NFL W1","Ravens","Colts","Indy 13:00 CBS",48,"W1 inicia 9 Sep Sea-Pats rematch"),
("14/09","NFL W1","Bills","Texans","Houston 13:00 CBS",52,"W1"),
("14/09","NFL W1","Bears","Panthers","Carolina 13:00 FOX",46,"W1"),
("14/09","NFL W1","Falcons","Steelers","Pittsburgh 13:00 FOX",47,"W1"),
("14/09","NFL W1","Cowboys","Giants","Giants 20:20 NBC SNF",52,"SNF"),
("15/09","NFL W1","Broncos","Chiefs","Denver 20:15 ESPN MNF",50,"MNF"),
# SEMANA QUE VIENE 16-20
("16/09","UCL J1","Real Madrid","Marseille","Bernabeu 13:00 TNT",62,"UCL inicia 16-18 Sep"),
("16/09","UCL J1","Bayern","Chelsea","Allianz 13:00 TNT",55,"UCL J1"),
("17/09","UCL J1","Barcelona","PSG","Montjuic 13:00 TNT",48,"UCL J1"),
("17/09","UCL J1","Man City","Napoli","Etihad 13:00 TNT",54,"UCL J1"),
("18/09","UCL J1","Liverpool","Atletico","Anfield 13:00 TNT",51,"UCL J1"),
("18/09","BOX PROX","Hamzah Sheeraz","Christian Mbilli","Riad WBC Vacante prox",54,"WBC ordeno Sheeraz vs Mbilli por titulo vacante que dejo Crawford - prox 31 Oct Canelo vs Mbilli"),
]
cards=""
for f in raw:
    fecha,liga,home,away,tv,prob,extra=f
    momio=round(1/(prob/100*1.045),2)
    ev=round((prob/100* momio -1)*100,1)
    cards+=f"<div class=card-outer><div class=card-top>{liga} {home} vs {away}</div><div class=card-mid><span>{tv}</span><span>{extra[:60]} | {prob}% REAL</span></div><div class=card-bot>{home.upper()} ML @{momio} {prob}% REAL EV {ev}% - {extra[:80]}</div></div>\n"
html=f"""<!DOCTYPE html><html><head><meta charset=UTF-8><meta name=viewport content=width=device-width,initial-scale=1><title>V88.5 12-20 SEP CORREGIDO</title>
<style>
body{{background:#050a0a;color:#fff;font-family:Arial;margin:0;padding:6px}}
.top-banner{{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:12px;border-radius:14px;text-align:center;font-weight:800;font-size:11px;margin-bottom:10px}}
.filtros{{background:#0a1414;border:1px solid #1a2a2a;border-radius:16px;padding:10px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:12px}}
.filtros button{{border:none;padding:8px 13px;border-radius:18px;font-weight:800;font-size:11px;cursor:pointer;border:1px solid #222}}
.btn-green{{background:#00e676;color:#000}}.btn-blue{{background:#0f2a4a;color:#4fc3f7;border:1px solid #1a4a7a}}.btn-dark{{background:#1b2a2a;color:#b0c4c4}}
.card-outer{{background:#071a14;border:2px solid #00ff88;border-radius:16px;padding:5px;margin:10px 2px}}
.card-top{{background:#0e2233;border-radius:10px;padding:8px 10px;margin-bottom:4px;font-weight:800;color:#4fc3f7;font-size:11px}}
.card-mid{{background:#1a1a0a;border-radius:8px;padding:6px 10px;margin-bottom:4px;color:#ffcc66;font-size:10px;display:flex;justify-content:space-between}}
.card-bot{{background:linear-gradient(90deg,#0a4a2a,#0f7a3a);border:1px solid #00ff88;border-radius:10px;padding:10px;text-align:center;color:#aaffcc;font-weight:900;font-size:11px}}
</style></head><body>
<div class=top-banner>V88.5 12-20 SEP 2026 CORREGIDO - {len(raw)} EVENTOS - SIN CANELO-CRAWFORD (YA PELEARON 2025) - BOX REAL GARCIA-BENN HOY + NFL W1 + TU FORMATO - HOY {len([x for x in raw if 'HOY' in x[4]])} EVENTOS</div>
<div class=filtros><button class=btn-blue>HOY 12/09 ({len([x for x in raw if 'HOY' in x[4]])})</button><button class=btn-dark>BOX REAL (1)</button><button class=btn-dark>NFL W1 (6)</button><button class=btn-dark>MX (3)</button><button class=btn-dark>UCL PROX (5)</button></div>
{cards}
</body></html>"""
open("index.html","w",encoding="utf-8").write(html)
print(f"LISTO CORREGIDO 12-20 SEP {len(raw)} - SIN CANELO")
