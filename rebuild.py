"""Rebuild the standalone app from the files in the delivered ZIP. Python 3 only."""
from pathlib import Path
import base64,json,re

root=Path(__file__).resolve().parent
css=(root/'source/style.css').read_text(encoding='utf8')
js=(root/'source/app.js').read_text(encoding='utf8')
data=json.loads((root/'data/synthetic-data.json').read_text(encoding='utf8'))
readme=(root/'README.md').read_text(encoding='utf8')
files={}
for key,name in [('annex','documents/CareFlow_Synthetic_Patients.xlsx'),('pdf','documents/CareFlow_Presentation.pdf'),('pptx','documents/CareFlow_Editable_Slides.pptx'),('spec','documents/Workbench_Specification.md'),('design','documents/Design_References.md'),('sourceJS','source/app.js'),('sourceCSS','source/style.css'),('sourceBuild','rebuild.py'),('qa','QA.md'),('designNotes','DESIGN_NOTES.md')]:
 p=root/name
 if p.exists():files[key]=base64.b64encode(p.read_bytes()).decode()
def safe(v):return json.dumps(v,ensure_ascii=False).replace('<','\\u003c')
html=(root/'index.html').read_text(encoding='utf8')
html=re.sub(r'<style>[\s\S]*?</style>',lambda m:'<style>'+css+'</style>',html,count=1)
script='<script>window.CARE_DATA='+safe(data)+';window.CARE_FILES='+safe(files)+';window.CARE_README='+safe(readme)+';</script>'
html=re.sub(r'<script>window.CARE_DATA=[\s\S]*?</script>',lambda m:script,html,count=1)
html=re.sub(r'<script>\s*[\'"]use strict[\'"];[\s\S]*?</script>',lambda m:'<script>'+js+'</script>',html,count=1)
(root/'index.html').write_text(html,encoding='utf8')
print('Rebuilt index.html. Open it directly in your browser.')
