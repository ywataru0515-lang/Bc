import re,sys
for n,l in enumerate(open('article.txt').read().split('\n'),1):
    t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',l).replace('**','')
    if not t or t.startswith('[img') or t.startswith('[ai') or t.startswith('##'): continue
    isli=t.startswith('- ')
    body=t[2:] if isli else t
    probs=[]
    if body.count('。')>=2: probs.append('2文')
    lim=30 if isli else 35
    if len(body)>lim: probs.append(f'len{len(body)}')
    if body.count('、')>2: probs.append('読点')
    if probs: print(n,probs,body)
