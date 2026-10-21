"""Build the profile's responsive Alpine Ember artwork with no external assets."""
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BG, PANEL, BORDER = "#121018", "#191621", "#51475f"
TEXT, MUTED, AMBER, LAVENDER = "#f6f0e8", "#b9afc5", "#ffbd69", "#c5adff"


def shell(width, height, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Abhishek Ash — making agents easier to understand</title>
<desc id="desc">Senior Staff Engineer in Berlin. Agenturm for agent monitoring, SpanHound for trace inspection, and agent-evals for regression checks. A geometric amber tower represents a clear view of agent activity.</desc>
<defs><linearGradient id="sky" x2="1" y2="1"><stop stop-color="#30223d"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="24" fill="url(#sky)" stroke="{BORDER}"/>
{body}
</svg>'''


def build():
    # Reuse the app's original vector artwork, including its accessible title.
    ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')
    icon = ElementTree.parse(ASSETS / "agenturm-icon.svg").getroot()
    mark = ''.join(ElementTree.tostring(path, encoding='unicode')
                   for path in icon.findall('{http://www.w3.org/2000/svg}path'))
    base = 'font-family="DejaVu Sans,Arial,sans-serif"'
    mono = 'font-family="DejaVu Sans Mono,monospace"'
    desktop = f'''
<g {mono}>
  <path d="M48 47h32" stroke="{AMBER}" stroke-width="3"/>
  <text x="94" y="53" fill="{MUTED}" font-size="14" letter-spacing="2">OPEN SOURCE / AGENT TOOLS</text>
  <text x="48" y="107" fill="{TEXT}" font-size="22" font-weight="bold" letter-spacing="2">ABHISHEK ASH</text>
  <text x="48" y="138" fill="{MUTED}" font-size="15">SENIOR STAFF ENGINEER · BERLIN</text>
</g>
<g {base} font-size="66" font-weight="bold" letter-spacing="-1.5">
  <text x="44" y="227" fill="{TEXT}">Making agents</text>
  <text x="44" y="307" fill="{AMBER}">easier to understand.</text>
</g>
<text x="48" y="353" fill="{MUTED}" {base} font-size="21">See the work. Follow the evidence. Check the behavior.</text>
<g transform="translate(948 52) scale(.5)">{mark}</g>
<path d="M48 390h1184" stroke="{BORDER}"/>
<g {mono} font-size="16">
  <text x="48" y="434" fill="{AMBER}">01 / AGENTURM</text>
  <text x="475" y="434" fill="{LAVENDER}">02 / SPANHOUND</text>
  <text x="900" y="434" fill="#86e3b5">03 / AGENT-EVALS</text>
</g>'''
    mobile = f'''
<g {mono}>
  <path d="M32 35h28" stroke="{AMBER}" stroke-width="3"/>
  <text x="74" y="41" fill="{MUTED}" font-size="15" letter-spacing="1">OPEN SOURCE / AGENT TOOLS</text>
  <text x="32" y="98" fill="{TEXT}" font-size="29" font-weight="bold">ABHISHEK ASH</text>
  <text x="32" y="133" fill="{MUTED}" font-size="17">SENIOR STAFF ENGINEER · BERLIN</text>
</g>
<g transform="translate(518 59) scale(.28)">{mark}</g>
<g {base} font-size="56" font-weight="bold" letter-spacing="-1.5">
  <text x="30" y="224" fill="{TEXT}">Making agents</text>
  <text x="30" y="292" fill="{AMBER}">easier to understand.</text>
</g>
<text x="32" y="343" fill="{MUTED}" {base} font-size="20">See the work. Follow the evidence. Check the behavior.</text>
<path d="M32 381h636" stroke="{BORDER}"/>
<g {mono} font-size="19">
  <text x="32" y="420" fill="{AMBER}">01 / AGENTURM</text>
  <text x="32" y="455" fill="{LAVENDER}">02 / SPANHOUND</text>
  <text x="32" y="490" fill="#86e3b5">03 / AGENT-EVALS</text>
</g>'''
    (ASSETS / "profile-hero.svg").write_text(shell(1280, 470, desktop))
    (ASSETS / "profile-hero-mobile.svg").write_text(shell(700, 524, mobile))


if __name__ == "__main__":
    build()
