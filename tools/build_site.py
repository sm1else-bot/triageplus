"""Build the static case study; publish only the explicit public allowlist."""
from pathlib import Path
import hashlib
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
SITE.mkdir(exist_ok=True)
html = (ROOT / 'index.html').read_text()
for name in ('styles.css', 'app.js'):
    source = ROOT / name
    version = hashlib.sha256(source.read_bytes()).hexdigest()[:12]
    html = re.sub(re.escape(name) + r'(?:\?v=[a-z0-9]+)?', name + '?v=' + version, html)
    shutil.copyfile(source, SITE / name)
(SITE / 'index.html').write_text(html)
shutil.copyfile(ROOT / 'favicon.svg', SITE / 'favicon.svg')
shutil.copytree(ROOT / 'assets', SITE / 'assets', dirs_exist_ok=True)
print('Built static case study in _site/')
