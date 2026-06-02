"""
Embed des fonts custom (Cormorant Garamond + Inter) en base64 inline.
Garantit l'affichage premium sur tout host (Linux, Windows, Mac) y compris Streamlit Cloud
ou les fonts systeme ne sont pas dispos.
"""

import base64
from functools import lru_cache
from pathlib import Path

FONTS_DIR = Path(__file__).parent / "assets" / "fonts"


@lru_cache(maxsize=8)
def _b64(filename: str) -> str:
    """Lit un WOFF2 et retourne son base64."""
    path = FONTS_DIR / filename
    return base64.b64encode(path.read_bytes()).decode()


@lru_cache(maxsize=1)
def fonts_css() -> str:
    """Genere le CSS @font-face avec les fonts inline (mis en cache une seule fois)."""
    return f"""
<style>
@font-face {{
  font-family: 'Cormorant Garamond';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{_b64('cormorant-regular.woff2')}) format('woff2');
}}
@font-face {{
  font-family: 'Cormorant Garamond';
  font-style: italic;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{_b64('cormorant-italic.woff2')}) format('woff2');
}}
@font-face {{
  font-family: 'Cormorant Garamond';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(data:font/woff2;base64,{_b64('cormorant-bold.woff2')}) format('woff2');
}}
@font-face {{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{_b64('inter-400.woff2')}) format('woff2');
}}
@font-face {{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(data:font/woff2;base64,{_b64('inter-500.woff2')}) format('woff2');
}}
@font-face {{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(data:font/woff2;base64,{_b64('inter-600.woff2')}) format('woff2');
}}
</style>
"""
