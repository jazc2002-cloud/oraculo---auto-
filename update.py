import re
from datetime import datetime

with open('index.html','r',encoding='utf-8') as f:
    html = f.read()

ahora = datetime.now().strftime('%d %b %Y %H:%M CDMX')
nueva_nube = f'✅ V63 AUTO {ahora} - NUBE LIMPIA - FORMATO COMPLETO'

html = re.sub(r'<div id="nube">.*?</div>', f'<div id="nube">{nueva_nube}</div>', html)

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)

with open('last_update.txt','w') as f:
    f.write(nueva_nube)
