print("V88.5 MIN VERDE")
games_html = ""
for i in range(42):
    games_html += f"<div style='background:#071a14;border:2px solid #00ff88;margin:8px;padding:10px;border-radius:12px'><b>EVENTO {i+1}</b> - HOY - 55% @1.8</div>"

open("index.html","w",encoding="utf-8").write(f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>V88.5</title>
<style>body{{background:#050a0a;color:#fff;font-family:Arial;padding:6px}}.top{{background:#0a2a1a;border:2px dashed #00ff88;color:#00ff88;padding:12px;border-radius:14px;text-align:center;font-weight:800}}</style></head><body>
<div class="top">V88.5 VERDE - 42 EVENTOS - HOY</div>
{games_html}
</body></html>""")
print("LISTO 42")
