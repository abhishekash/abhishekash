"""Build responsive profile artwork using Agenturm's website palette and tower."""
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PAPER, INK, MUTED = "#f2efe7", "#222722", "#596157"
RULE, SIGNAL, VIOLET, GREEN = "#cbcfc2", "#dceb5a", "#7352a3", "#32684c"


def shell(width, height, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Abhishek Ash — know what your agents are doing</title>
<desc id="desc">Senior Staff Engineer in Berlin. Building Agenturm for local coding-agent observability, SpanHound for trace inspection, and agent-evals for regression checks. An architectural drawing of Berlin's observation tower echoes Agenturm's website.</desc>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="6" fill="{PAPER}" stroke="{RULE}"/>
{body}
</svg>'''


def build():
    # Source: https://www.agenturm.dev/brand/tower-drawing.svg (MIT).
    ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')
    tower = ElementTree.parse(ASSETS / "agenturm-tower-drawing.svg").getroot()
    mark = ''.join(ElementTree.tostring(element, encoding='unicode')
                   for element in tower
                   if element.tag != '{http://www.w3.org/2000/svg}title')
    base = 'font-family="DejaVu Sans,Arial,sans-serif"'
    mono = 'font-family="DejaVu Sans Mono,monospace"'
    desktop = f'''
<g {mono}>
  <path d="M48 47h32" stroke="{VIOLET}" stroke-width="3"/>
  <text x="94" y="53" fill="{MUTED}" font-size="14" letter-spacing="2">OPEN SOURCE / BUILT IN THE OPEN</text>
  <text x="48" y="107" fill="{INK}" font-size="22" font-weight="bold" letter-spacing="2">ABHISHEK ASH</text>
  <text x="48" y="138" fill="{MUTED}" font-size="15">SENIOR STAFF ENGINEER · BERLIN</text>
</g>
<rect x="48" y="320" width="96" height="5" fill="{SIGNAL}"/>
<g {base} font-size="66" font-weight="bold" letter-spacing="-1.5">
  <text x="44" y="227" fill="{INK}">Know what your</text>
  <text x="44" y="307" fill="{INK}">agents are doing.</text>
</g>
<text x="48" y="363" fill="{MUTED}" {base} font-size="21">Local observability. Trace inspection. Regression checks.</text>
<path d="M916 48v310" stroke="{RULE}"/>
<g transform="translate(990 44) scale(1.05)" fill="none">{mark}</g>
<text x="960" y="363" fill="{MUTED}" {mono} font-size="13">BUILT IN BERLIN</text>
<path d="M48 400h1184" stroke="{RULE}"/>
<g {mono} font-size="16">
  <text x="48" y="441" fill="{INK}">01 / AGENTURM</text>
  <text x="475" y="441" fill="{VIOLET}">02 / SPANHOUND</text>
  <text x="900" y="441" fill="{GREEN}">03 / AGENT-EVALS</text>
</g>'''
    mobile = f'''
<g {mono}>
  <path d="M32 35h28" stroke="{VIOLET}" stroke-width="3"/>
  <text x="74" y="41" fill="{MUTED}" font-size="15" letter-spacing="1">OPEN SOURCE / BUILT IN THE OPEN</text>
  <text x="32" y="98" fill="{INK}" font-size="29" font-weight="bold">ABHISHEK ASH</text>
  <text x="32" y="133" fill="{MUTED}" font-size="17">SENIOR STAFF ENGINEER · BERLIN</text>
</g>
<g transform="translate(578 64) scale(.36)" fill="none">{mark}</g>
<rect x="32" y="305" width="72" height="5" fill="{SIGNAL}"/>
<g {base} font-size="56" font-weight="bold" letter-spacing="-1.5">
  <text x="30" y="224" fill="{INK}">Know what your</text>
  <text x="30" y="292" fill="{INK}">agents are doing.</text>
</g>
<text x="32" y="345" fill="{MUTED}" {base} font-size="20">Local observability. Trace inspection. Regression checks.</text>
<path d="M32 381h636" stroke="{RULE}"/>
<g {mono} font-size="19">
  <text x="32" y="420" fill="{INK}">01 / AGENTURM</text>
  <text x="32" y="455" fill="{VIOLET}">02 / SPANHOUND</text>
  <text x="32" y="490" fill="{GREEN}">03 / AGENT-EVALS</text>
</g>'''
    (ASSETS / "profile-hero.svg").write_text(shell(1280, 470, desktop))
    (ASSETS / "profile-hero-mobile.svg").write_text(shell(700, 524, mobile))


if __name__ == "__main__":
    build()
