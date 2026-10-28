"""Verify publication boundaries, relative references, accessibility metadata and output."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

html = (SITE / 'index.html').read_text()
doc = Document()
doc.feed(html)
ids = [a['id'] for _, a in doc.tags if 'id' in a]
assert len(ids) == len(set(ids)), 'Duplicate HTML IDs'
for tag, attrs in doc.tags:
    for key in ('src', 'href'):
        value = attrs.get(key)
        if not value:
            continue
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or value == '../':
            continue
        if parsed.path:
            assert (SITE / unquote(parsed.path)).is_file(), value
        elif parsed.fragment:
            assert parsed.fragment in ids, value
    if tag == 'img' and attrs.get('src'):
        assert attrs.get('alt'), 'Missing image description'
        assert attrs.get('width') and attrs.get('height'), 'Missing intrinsic image dimensions'
assert sum(tag == 'h1' for tag, _ in doc.tags) == 1
assert any(tag == 'link' and a.get('rel') == 'canonical' and a.get('href') == 'https://projects.jessenth.com/triageplus/' for tag, a in doc.tags)
assert 'Interactive demo coming soon' in html
assert html.count('https://triage-production-b22c.up.railway.app') == 2
assert re.search(r'styles\.css\?v=[a-f0-9]{12}', html)
assert re.search(r'app\.js\?v=[a-f0-9]{12}', html)
for path in SITE.rglob('*'):
    if path.is_file():
        assert path.suffix in {'.html', '.css', '.js', '.svg', '.webp', '.jpg'}, path
        assert not any(x in path.parts for x in ('.env', 'backend', '.triage-data', '.git')), path
        if path.suffix in {'.html', '.css', '.js', '.svg'}:
            text = path.read_text()
            assert not re.search(r'(?:sk-[a-zA-Z0-9_-]{20,}|tvly-[a-zA-Z0-9_-]{20,})', text), path
            assert '/Users/' not in text and '127.0.0.1' not in text, path
for phrase in ('not just', 'at its core', 'revolutionizing', 'game-changing', 'cutting-edge', 'seamlessly integrates', 'a testament to', 'journey of innovation'):
    assert phrase not in html.lower(), phrase
print('PASS static references, metadata, image accessibility, publication allowlist and editorial checks')
