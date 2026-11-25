import json,sys,base64,re
a=json.load(open(sys.argv[1])); t=a[0]['text']
m=re.search(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)',t)
open(sys.argv[2],'wb').write(base64.b64decode(m.group(1)))
