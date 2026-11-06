import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'data'/'lessons.json').read_text(encoding='utf-8'))
L=d['lessons']
assert len(L)==23
assert [l['id'] for l in L]==list(range(1,24))
for l in L:
    assert l['title'] and l['hanzi'] and l['sourcePage']
    assert len(l['vocab'])>=19 and len(l['grammar'])>=3
    assert len(l['dialogs'])==2
    for v in l['vocab']:
        assert v['zh'] and v['py'] and v['fr']
    for g in l['grammar']:
        assert all(g[k] for k in ('title','explanation','zh','py','fr'))
    for dia in l['dialogs']:
        assert len(dia['lines'])>=4
        assert {'A','B'}.issubset({line['speaker'] for line in dia['lines']})
        assert all(all(line[k] for k in ('zh','py','fr')) for line in dia['lines'])
print(f'OK : {len(L)} leçons · {sum(len(x["vocab"]) for x in L)} mots · {sum(len(x["grammar"]) for x in L)} notions de grammaire · {sum(len(y["lines"]) for x in L for y in x["dialogs"])} répliques')
