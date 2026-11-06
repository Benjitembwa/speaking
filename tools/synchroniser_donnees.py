from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
path=root/'data'/'lessons.json'
obj=json.loads(path.read_text(encoding='utf-8'))
assert len(obj['lessons'])==23
(root/'data'/'lessons.js').write_text('window.MANDARIN_LESSONS = '+json.dumps(obj,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
print('Synchronisé : data/lessons.js')
