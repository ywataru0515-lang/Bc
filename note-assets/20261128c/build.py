import re,json,sys
shop=sys.argv[1]
lines=open('article.txt').read().replace('{SHOP}',shop).replace('{DEMO}','https://ywataru0515-lang.github.io/Bc/demo.html').replace('{LP}','https://ywataru0515-lang.github.io/Bc/').split('\n')
def inline(t):
    out=[];pos=0
    for m in re.finditer(r'\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)',t):
        if m.start()>pos: out.append({'type':'text','text':t[pos:m.start()]})
        if m.group(1): out.append({'type':'text','text':m.group(1),'marks':[{'type':'strong'}]})
        else: out.append({'type':'text','text':m.group(2),'marks':[{'type':'link','attrs':{'href':m.group(3),'target':'_blank','rel':'noopener'}}]})
        pos=m.end()
    if pos<len(t): out.append({'type':'text','text':t[pos:]})
    return out
nodes=[]
for l in lines:
    if l.startswith('## '): nodes.append({'type':'heading','attrs':{'level':2},'content':inline(l[3:])})
    elif l.startswith('[img:'):
        f,c=l[5:-1].split('|'); nodes.append({'type':'IMG','file':f,'cap':c})
    elif l.startswith('- '):
        li={'type':'listItem','content':[{'type':'paragraph','content':inline(l[2:])}]}
        if nodes and nodes[-1]['type']=='bulletList': nodes[-1]['content'].append(li)
        else: nodes.append({'type':'bulletList','content':[li]})
    elif l.strip()=='' : nodes.append({'type':'paragraph'})
    else: nodes.append({'type':'paragraph','content':inline(l)})
# cleanup empties
res=[]
for i,n in enumerate(nodes):
    empty=n['type']=='paragraph' and 'content' not in n
    if empty:
        prev=res[-1] if res else None; nxt=nodes[i+1] if i+1<len(nodes) else None
        if prev is None or prev['type'] in('heading','IMG') or (prev['type']=='paragraph' and 'content' not in prev): continue
        if nxt is None or nxt['type']=='IMG': continue
    res.append(n)
while res and res[-1]['type']=='paragraph' and 'content' not in res[-1]: res.pop()
json.dump(res,open('doc.json','w'),ensure_ascii=False)
# checks
bad=0
for i,n in enumerate(res):
    if n['type']=='paragraph' and 'content' in n:
        t=''.join(x['text'] for x in n['content'])
        if t.count('。')>=2 or len(t)>50: print('BAD',t); bad+=1
    if n['type']=='paragraph' and 'content' not in n:
        if i>0 and (res[i-1]['type'] in ('heading','IMG') or (res[i-1]['type']=='paragraph' and 'content' not in res[i-1])): print('BADEMPTY',i); bad+=1
        if i+1<len(res) and res[i+1]['type']=='IMG': print('BADEMPTY-before-img',i); bad+=1
print('nodes',len(res),'imgs',sum(n['type']=='IMG' for n in res),'bad',bad)
