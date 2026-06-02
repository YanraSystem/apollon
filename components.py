"""
Composants HTML/CSS custom pour Streamlit.
Animations cinematiques pour la page d'accueil et les wow moments.
"""

import base64
from pathlib import Path

import streamlit.components.v1 as components

ASSETS_DIR = Path(__file__).parent / "assets"


def _b64_image(filename: str) -> str:
    """Lit une image et retourne son data URL base64."""
    path = ASSETS_DIR / filename
    if not path.exists():
        return ""
    data = base64.b64encode(path.read_bytes()).decode()
    ext = path.suffix[1:].lower()
    return f"data:image/{ext};base64,{data}"


def splash_screen_markdown() -> str:
    """Retourne le HTML du splash a injecter via st.markdown (pas d'iframe = clic marche)."""
    return """
<style>
  .splash-root {
    position: fixed;
    inset: 0;
    z-index: 999998;
    background: radial-gradient(ellipse at center, #1a0033 0%, #0a0014 60%, #000000 100%);
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  .splash-container {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .splash-stars {
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(2px 2px at 15% 25%, white, transparent),
      radial-gradient(2px 2px at 65% 75%, #FFB347, transparent),
      radial-gradient(1px 1px at 85% 15%, white, transparent),
      radial-gradient(1px 1px at 35% 85%, #FF6B35, transparent),
      radial-gradient(2px 2px at 92% 55%, white, transparent),
      radial-gradient(1px 1px at 12% 65%, #FFB347, transparent),
      radial-gradient(1px 1px at 55% 12%, white, transparent),
      radial-gradient(2px 2px at 75% 45%, #FF6B35, transparent),
      radial-gradient(1px 1px at 25% 45%, white, transparent),
      radial-gradient(2px 2px at 45% 60%, white, transparent);
    opacity: 0;
    animation: splash-fadein 1.5s ease-in 0.5s forwards, splash-twinkle 5s ease-in-out 2s infinite alternate;
  }
  @keyframes splash-fadein { to { opacity: 0.6; } }
  @keyframes splash-twinkle { from { opacity: 0.3; } to { opacity: 0.9; } }

  .splash-emoji {
    position: absolute;
    font-size: 32px;
    opacity: 0;
    animation: splash-float 6s ease-in-out infinite;
    filter: drop-shadow(0 0 12px rgba(255,107,53,0.5));
  }
  .splash-emoji:nth-of-type(1) { top: 15%; left: 12%; animation-delay: 0s; }
  .splash-emoji:nth-of-type(2) { top: 22%; right: 18%; animation-delay: 1.5s; }
  .splash-emoji:nth-of-type(3) { bottom: 30%; left: 20%; animation-delay: 3s; }
  .splash-emoji:nth-of-type(4) { bottom: 18%; right: 14%; animation-delay: 0.8s; }
  .splash-emoji:nth-of-type(5) { top: 45%; left: 8%; animation-delay: 2.2s; }
  .splash-emoji:nth-of-type(6) { top: 55%; right: 8%; animation-delay: 4s; }
  @keyframes splash-float {
    0% { opacity: 0; transform: translateY(20px); }
    20% { opacity: 0.7; }
    50% { transform: translateY(-15px); }
    80% { opacity: 0.7; }
    100% { opacity: 0; transform: translateY(20px); }
  }

  .splash-title {
    font-family: "Brush Script MT", "Snell Roundhand", "Apple Chancery", "Lucida Handwriting", cursive;
    font-size: 110px;
    font-weight: 400;
    font-style: italic;
    text-shadow:
      0 0 20px rgba(255,107,53,0.6),
      0 0 40px rgba(255,107,53,0.4),
      0 4px 8px rgba(0,0,0,0.5);
    letter-spacing: 4px;
    opacity: 0;
    animation: splash-titlein 1.5s ease-out 0.3s forwards;
    background: linear-gradient(135deg, #FFFFFF 0%, #FFB347 50%, #FF6B35 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin: 0;
  }
  @keyframes splash-titlein {
    from { opacity: 0; transform: scale(0.8) translateY(20px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
  }
  .splash-tagline {
    color: rgba(255,255,255,0.6);
    font-size: 16px;
    letter-spacing: 6px;
    text-transform: uppercase;
    margin-top: 24px;
    opacity: 0;
    animation: splash-fadeup 1s ease-out 1.2s forwards;
  }
  .splash-divider {
    width: 60px;
    height: 1px;
    background: rgba(255,255,255,0.3);
    margin-top: 32px;
    opacity: 0;
    animation: splash-expand 1s ease-out 1.6s forwards;
  }
  @keyframes splash-expand {
    from { width: 0; opacity: 0; }
    to { width: 60px; opacity: 1; }
  }
  @keyframes splash-fadeup {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .splash-cta {
    position: absolute;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.7);
    font-size: 13px;
    letter-spacing: 8px;
    text-transform: uppercase;
    font-weight: 600;
    opacity: 0;
    animation: splash-blink 2s ease-in-out 2s infinite;
  }
  .splash-cta::before, .splash-cta::after {
    content: "•";
    margin: 0 14px;
    color: #FF6B35;
  }
  @keyframes splash-blink {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 1; }
  }
  .splash-footer {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.25);
    font-size: 11px;
    letter-spacing: 2px;
  }

  /* Overlay clickable plein ecran, lien HTML natif sans iframe -> marche */
  .splash-overlay-link {
    position: fixed;
    inset: 0;
    z-index: 999999;
    cursor: pointer;
    display: block;
    text-decoration: none;
  }
</style>

<div class="splash-root">
  <div class="splash-container">
    <div class="splash-stars"></div>
    <span class="splash-emoji">🍅</span>
    <span class="splash-emoji">🥖</span>
    <span class="splash-emoji">🌶️</span>
    <span class="splash-emoji">🍣</span>
    <span class="splash-emoji">🥕</span>
    <span class="splash-emoji">🍋</span>
    <h1 class="splash-title">NutriRecettes</h1>
    <p class="splash-tagline">Toutes les cuisines du monde</p>
    <div class="splash-divider"></div>
    <div class="splash-cta">CLICK ANYWHERE TO ENTER</div>
    <div class="splash-footer">© 2026 NutriRecettes</div>
  </div>
</div>
"""


def splash_screen(height: int = 900):
    """[DEPRECATED, voir splash_screen_markdown] Splash dans iframe — clic ne marche pas."""
    html = """
<!DOCTYPE html>
<html>
<head>
<style>
  html, body { width: 100%; height: 100%; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: radial-gradient(ellipse at center, #1a0033 0%, #0a0014 60%, #000000 100%);
    overflow: hidden;
    cursor: pointer;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  body:hover .title { letter-spacing: 8px; }

  .overlay-link {
    position: fixed;
    inset: 0;
    z-index: 9999;
    cursor: pointer;
    text-decoration: none;
    display: block;
  }

  .container {
    position: relative;
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .stars {
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(2px 2px at 15% 25%, white, transparent),
      radial-gradient(2px 2px at 65% 75%, #FFB347, transparent),
      radial-gradient(1px 1px at 85% 15%, white, transparent),
      radial-gradient(1px 1px at 35% 85%, #FF6B35, transparent),
      radial-gradient(2px 2px at 92% 55%, white, transparent),
      radial-gradient(1px 1px at 12% 65%, #FFB347, transparent),
      radial-gradient(1px 1px at 55% 12%, white, transparent),
      radial-gradient(2px 2px at 75% 45%, #FF6B35, transparent),
      radial-gradient(1px 1px at 25% 45%, white, transparent),
      radial-gradient(2px 2px at 45% 60%, white, transparent);
    opacity: 0;
    animation: fadeIn 1.5s ease-in 0.5s forwards, twinkle 5s ease-in-out 2s infinite alternate;
  }

  @keyframes fadeIn { to { opacity: 0.6; } }
  @keyframes twinkle {
    from { opacity: 0.3; }
    to { opacity: 0.9; }
  }

  .floating-emoji {
    position: absolute;
    font-size: 32px;
    opacity: 0;
    animation: float 6s ease-in-out infinite;
    filter: drop-shadow(0 0 12px rgba(255,107,53,0.5));
  }
  .floating-emoji:nth-child(1) { top: 15%; left: 12%; animation-delay: 0s; }
  .floating-emoji:nth-child(2) { top: 22%; right: 18%; animation-delay: 1.5s; }
  .floating-emoji:nth-child(3) { bottom: 30%; left: 20%; animation-delay: 3s; }
  .floating-emoji:nth-child(4) { bottom: 18%; right: 14%; animation-delay: 0.8s; }
  .floating-emoji:nth-child(5) { top: 45%; left: 8%; animation-delay: 2.2s; }
  .floating-emoji:nth-child(6) { top: 55%; right: 8%; animation-delay: 4s; }

  @keyframes float {
    0% { opacity: 0; transform: translateY(20px); }
    20% { opacity: 0.7; }
    50% { transform: translateY(-15px); }
    80% { opacity: 0.7; }
    100% { opacity: 0; transform: translateY(20px); }
  }

  .title {
    font-family: "Brush Script MT", "Pacifico", cursive;
    font-size: 96px;
    font-weight: 900;
    color: white;
    text-shadow:
      0 0 20px rgba(255,107,53,0.6),
      0 0 40px rgba(255,107,53,0.4),
      0 4px 8px rgba(0,0,0,0.5);
    letter-spacing: 4px;
    transition: letter-spacing 0.6s;
    opacity: 0;
    animation: titleIn 1.5s ease-out 0.3s forwards;
    background: linear-gradient(135deg, #FFFFFF 0%, #FFB347 50%, #FF6B35 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    z-index: 2;
  }
  @keyframes titleIn {
    from { opacity: 0; transform: scale(0.8) translateY(20px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
  }

  .tagline {
    color: rgba(255,255,255,0.6);
    font-size: 16px;
    letter-spacing: 6px;
    text-transform: uppercase;
    margin-top: 24px;
    opacity: 0;
    animation: fadeUp 1s ease-out 1.2s forwards;
    z-index: 2;
  }
  .divider {
    width: 60px;
    height: 1px;
    background: rgba(255,255,255,0.3);
    margin-top: 32px;
    opacity: 0;
    animation: expand 1s ease-out 1.6s forwards;
  }
  @keyframes expand {
    from { width: 0; opacity: 0; }
    to { width: 60px; opacity: 1; }
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .cta {
    position: absolute;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.7);
    font-size: 13px;
    letter-spacing: 8px;
    text-transform: uppercase;
    font-weight: 600;
    opacity: 0;
    animation: cta-blink 2s ease-in-out 2s infinite;
    z-index: 2;
  }
  .cta::before, .cta::after {
    content: "•";
    margin: 0 14px;
    color: #FF6B35;
  }
  @keyframes cta-blink {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 1; }
  }

  .footer-mini {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.25);
    font-size: 11px;
    letter-spacing: 2px;
    z-index: 2;
  }
</style>
</head>
<body>
  <div class="container">
    <div class="stars"></div>
    <span class="floating-emoji">🍅</span>
    <span class="floating-emoji">🥖</span>
    <span class="floating-emoji">🌶️</span>
    <span class="floating-emoji">🍣</span>
    <span class="floating-emoji">🥕</span>
    <span class="floating-emoji">🍋</span>
    <h1 class="title">NutriRecettes</h1>
    <p class="tagline">Toutes les cuisines du monde</p>
    <div class="divider"></div>
    <div class="cta">CLICK ANYWHERE TO ENTER</div>
    <div class="footer-mini">© 2026 NutriRecettes</div>
  </div>
  <!-- Overlay clickable plein ecran : lien HTML natif qui force la navigation top-level -->
  <a href="?enter=1" target="_top" class="overlay-link" aria-label="Entrer dans le site"></a>
  <script>
    // Bonus : touche clavier (Enter / Espace) pour valider aussi
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        window.top.location.href = '?enter=1';
      }
    });
  </script>
</body>
</html>
"""
    components.html(html, height=height, scrolling=False)


def hero_personnage(height: int = 640):
    """Hero accueil : layout magazine editorial 2 colonnes (typographie + personnage)."""
    perso_b64 = _b64_image("hero_perso_small.png")
    if not perso_b64:
        return globe_hero(height)  # fallback

    # Charger fonts inline directement dans l'iframe (components.html isole le contexte)
    from fonts import fonts_css as _ff
    fonts_block = _ff()

    html = f"""
<!DOCTYPE html>
<html>
<head>
{fonts_block}
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    min-height: 100vh;
    background: #FAF7F2;
    background-image:
      radial-gradient(ellipse 800px 600px at 80% 50%, rgba(201,123,95,0.06) 0%, transparent 70%);
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    color: #2D2A26;
    position: relative;
  }}
  /* Texture noise subtile */
  body::before {{
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.04 0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E");
    opacity: 0.5;
    pointer-events: none;
    z-index: 1;
  }}

  .scene {{
    position: relative;
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    align-items: center;
    min-height: 100vh;
    max-width: 1240px;
    margin: 0 auto;
    padding: 40px 64px;
    gap: 48px;
    z-index: 2;
  }}

  /* === Colonne gauche : typographie editoriale === */
  .meta-top {{
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 0.32em;
    text-transform: uppercase;
    color: #8B7E70;
    margin-bottom: 32px;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .meta-top::after {{
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(45,42,38,0.15);
    max-width: 80px;
  }}

  .title {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(72px, 9vw, 128px);
    font-style: italic;
    font-weight: 700;
    line-height: 0.92;
    letter-spacing: -0.045em;
    color: #2D2A26;
    margin-bottom: 28px;
  }}

  .subtitle {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(20px, 1.8vw, 26px);
    font-style: italic;
    font-weight: 400;
    line-height: 1.45;
    color: #5C5751;
    max-width: 520px;
    margin-bottom: 40px;
  }}

  .footer-line {{
    display: flex;
    align-items: center;
    gap: 24px;
    margin-top: 48px;
    padding-top: 32px;
    border-top: 1px solid rgba(45,42,38,0.12);
    max-width: 520px;
  }}
  .footer-line .label {{
    font-size: 0.65rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #8B7E70;
    font-weight: 600;
  }}
  .footer-line .value {{
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.1rem;
    color: #2D2A26;
  }}
  .footer-line .divider {{
    width: 1px;
    height: 24px;
    background: rgba(45,42,38,0.15);
  }}

  /* === Colonne droite : perso === */
  .perso-wrap {{
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .number-bg {{
    position: absolute;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-weight: 700;
    font-size: 24rem;
    color: rgba(201,123,95,0.08);
    line-height: 0.8;
    z-index: 1;
    left: -8%;
    top: -6%;
    user-select: none;
    pointer-events: none;
  }}

  .perso {{
    position: relative;
    z-index: 2;
    height: 78vh;
    max-height: 580px;
    filter: drop-shadow(0 24px 48px rgba(45,42,38,0.18));
    animation: bobbing 4s ease-in-out infinite;
  }}
  @keyframes bobbing {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-12px); }}
  }}

  /* Trait ornemental sous le perso */
  .ornament {{
    position: absolute;
    bottom: 8%;
    right: -4%;
    width: 180px;
    height: 1px;
    background: linear-gradient(90deg, transparent, #C97B5F 50%, transparent);
    z-index: 1;
  }}
  .ornament-dot {{
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #C97B5F;
    z-index: 2;
  }}
  .ornament-dot.d1 {{ top: 18%; right: 4%; }}
  .ornament-dot.d2 {{ bottom: 28%; left: -2%; }}

  /* Responsive */
  @media (max-width: 880px) {{
    .scene {{
      grid-template-columns: 1fr;
      padding: 24px 24px;
      gap: 24px;
    }}
    .number-bg {{ display: none; }}
    .title {{ font-size: 56px; }}
  }}
</style>
</head>
<body>
  <div class="scene">
    <div>
      <div class="meta-top">Vol. I · 2026 · Cuisine du monde</div>
      <h1 class="title">NutriRecettes</h1>
      <p class="subtitle">Une recette du monde, composee a partir de ce qu'il te reste dans le frigo. Du tajine de Marrakech au pad thai d'Hanoi, en passant par la carbonara de Rome.</p>
      <div class="footer-line">
        <div>
          <div class="label">Cuisines</div>
          <div class="value">18 pays</div>
        </div>
        <div class="divider"></div>
        <div>
          <div class="label">Temps moyen</div>
          <div class="value">30 a 45 min</div>
        </div>
        <div class="divider"></div>
        <div>
          <div class="label">Methode</div>
          <div class="value">IA &amp; tradition</div>
        </div>
      </div>
    </div>
    <div class="perso-wrap">
      <div class="number-bg">N°1</div>
      <span class="ornament-dot d1"></span>
      <span class="ornament-dot d2"></span>
      <img class="perso" src="{perso_b64}" alt="NutriRecettes — la mascotte" />
      <div class="ornament"></div>
    </div>
  </div>
</body>
</html>
"""
    components.html(html, height=height, scrolling=False)


def globe_hero(height: int = 480):
    """Hero page d'accueil : globe rotatif + ingredients qui volent autour."""
    html = """
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #334155 100%);
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .scene { position: relative; width: 100%; height: 100vh; }

  .globe {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 280px;
    height: 280px;
    border-radius: 50%;
    background:
      radial-gradient(circle at 30% 30%, #60A5FA, #2563EB 40%, #1E40AF 70%, #1E3A8A);
    box-shadow:
      inset -30px -30px 60px rgba(0,0,0,0.5),
      inset 20px 20px 40px rgba(255,255,255,0.1),
      0 0 80px rgba(96, 165, 250, 0.4),
      0 0 120px rgba(96, 165, 250, 0.2);
    animation: rotate 20s linear infinite;
    position: relative;
  }

  .globe::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background:
      repeating-linear-gradient(90deg,
        transparent 0px,
        transparent 28px,
        rgba(255,255,255,0.08) 28px,
        rgba(255,255,255,0.08) 30px),
      repeating-linear-gradient(0deg,
        transparent 0px,
        transparent 28px,
        rgba(255,255,255,0.05) 28px,
        rgba(255,255,255,0.05) 30px);
  }

  .globe::after {
    content: "";
    position: absolute;
    inset: 10%;
    border-radius: 50%;
    background:
      radial-gradient(ellipse at 20% 30%, rgba(34, 197, 94, 0.7) 0, transparent 18%),
      radial-gradient(ellipse at 60% 25%, rgba(34, 197, 94, 0.6) 0, transparent 22%),
      radial-gradient(ellipse at 75% 55%, rgba(34, 197, 94, 0.5) 0, transparent 15%),
      radial-gradient(ellipse at 35% 70%, rgba(34, 197, 94, 0.6) 0, transparent 20%),
      radial-gradient(ellipse at 80% 80%, rgba(34, 197, 94, 0.4) 0, transparent 12%);
    filter: blur(2px);
  }

  @keyframes rotate {
    0% { transform: translate(-50%, -50%) rotateY(0deg); }
    100% { transform: translate(-50%, -50%) rotateY(360deg); }
  }

  .ingredient {
    position: absolute;
    font-size: 48px;
    top: 50%;
    left: 50%;
    transform-origin: center;
    animation-name: orbit;
    animation-duration: 18s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
    filter: drop-shadow(0 4px 12px rgba(0,0,0,0.4));
  }

  .ingredient:nth-child(1) { animation-delay: 0s; }
  .ingredient:nth-child(2) { animation-delay: -3s; }
  .ingredient:nth-child(3) { animation-delay: -6s; }
  .ingredient:nth-child(4) { animation-delay: -9s; }
  .ingredient:nth-child(5) { animation-delay: -12s; }
  .ingredient:nth-child(6) { animation-delay: -15s; }

  @keyframes orbit {
    from {
      transform: translate(-50%, -50%) rotate(0deg) translateX(260px) rotate(0deg);
    }
    to {
      transform: translate(-50%, -50%) rotate(360deg) translateX(260px) rotate(-360deg);
    }
  }

  .title {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    text-align: center;
    z-index: 10;
  }

  .title h1 {
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(135deg, #FF6B35, #F7931E);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
    margin-bottom: 8px;
  }

  .title p {
    color: rgba(255,255,255,0.7);
    font-size: 16px;
    font-weight: 400;
  }

  .stars {
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(2px 2px at 20% 30%, white, transparent),
      radial-gradient(2px 2px at 60% 70%, white, transparent),
      radial-gradient(1px 1px at 80% 20%, white, transparent),
      radial-gradient(1px 1px at 30% 80%, white, transparent),
      radial-gradient(2px 2px at 90% 50%, white, transparent),
      radial-gradient(1px 1px at 10% 60%, white, transparent),
      radial-gradient(1px 1px at 50% 10%, white, transparent),
      radial-gradient(2px 2px at 70% 40%, white, transparent);
    opacity: 0.6;
    animation: twinkle 4s ease-in-out infinite alternate;
  }

  @keyframes twinkle {
    from { opacity: 0.3; }
    to { opacity: 0.8; }
  }
</style>
</head>
<body>
  <div class="scene">
    <div class="stars"></div>
    <div class="globe"></div>
    <span class="ingredient">🍅</span>
    <span class="ingredient">🥖</span>
    <span class="ingredient">🌶️</span>
    <span class="ingredient">🍣</span>
    <span class="ingredient">🥕</span>
    <span class="ingredient">🍋</span>
    <div class="title">
      <h1>NutriRecettes</h1>
      <p>Toutes les cuisines du monde, generees par IA</p>
    </div>
  </div>
</body>
</html>
"""
    components.html(html, height=height, scrolling=False)


def feu_tricolore(indicateur: str, label: str):
    """Affiche un feu tricolore (rouge/orange/vert) pour la sante du plat."""
    couleurs = {
        "vert": ("#22C55E", "#86EFAC", "🟢"),
        "orange": ("#F59E0B", "#FCD34D", "🟠"),
        "rouge": ("#EF4444", "#FCA5A5", "🔴"),
    }
    color, bg, emoji = couleurs.get(indicateur.lower(), couleurs["orange"])

    html = f"""
<div style="
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  background: {bg}33;
  border: 2px solid {color};
  border-radius: 30px;
  font-family: -apple-system, sans-serif;
">
  <div style="display: flex; flex-direction: column; gap: 4px;">
    <div style="width: 14px; height: 14px; border-radius: 50%; background: {'#EF4444' if indicateur == 'rouge' else '#3F3F3F'}; opacity: {'1' if indicateur == 'rouge' else '0.3'};"></div>
    <div style="width: 14px; height: 14px; border-radius: 50%; background: {'#F59E0B' if indicateur == 'orange' else '#3F3F3F'}; opacity: {'1' if indicateur == 'orange' else '0.3'};"></div>
    <div style="width: 14px; height: 14px; border-radius: 50%; background: {'#22C55E' if indicateur == 'vert' else '#3F3F3F'}; opacity: {'1' if indicateur == 'vert' else '0.3'};"></div>
  </div>
  <div>
    <div style="font-size: 18px; font-weight: 700; color: {color};">{label}</div>
    <div style="font-size: 12px; color: #666;">Indicateur sante</div>
  </div>
</div>
"""
    return html


def carte_nutrition(nutrition: dict, personnes: int = 1):
    """Tableau nutritionnel complet avec barres de progression."""
    cal = nutrition.get("calories_par_personne", 0)
    prot = nutrition.get("proteines_g", 0)
    gluc = nutrition.get("glucides_g", 0)
    lip = nutrition.get("lipides_g", 0)
    fib = nutrition.get("fibres_g", 0)

    # Valeurs de reference AJR (apports journaliers recommandes adulte)
    refs = {"cal": 2000, "prot": 50, "gluc": 260, "lip": 70, "fib": 30}

    def barre(value, ref, label, unit, color):
        pct = min(100, (value / ref) * 100) if ref else 0
        return f"""
        <div style="margin-bottom: 12px;">
          <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
            <span style="font-size: 13px; color: #555; font-weight: 500;">{label}</span>
            <span style="font-size: 13px; color: #222; font-weight: 700;">{value}{unit} <span style="color:#999;font-weight:400">/ {ref}{unit} AJR</span></span>
          </div>
          <div style="width: 100%; height: 8px; background: #F1F5F9; border-radius: 10px; overflow: hidden;">
            <div style="width: {pct}%; height: 100%; background: {color}; border-radius: 10px; transition: width 0.6s;"></div>
          </div>
        </div>
        """

    return f"""
<div style="
  background: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  border: 1px solid #E2E8F0;
">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <h3 style="margin: 0; font-size: 18px; color: #1E293B;">Tableau nutritionnel</h3>
    <span style="font-size: 12px; color: #64748B; background: #F1F5F9; padding: 4px 10px; border-radius: 12px;">par personne</span>
  </div>
  {barre(cal, refs['cal'], "Calories", " kcal", "#FF6B35")}
  {barre(prot, refs['prot'], "Proteines", " g", "#3B82F6")}
  {barre(gluc, refs['gluc'], "Glucides", " g", "#F59E0B")}
  {barre(lip, refs['lip'], "Lipides", " g", "#EF4444")}
  {barre(fib, refs['fib'], "Fibres", " g", "#22C55E")}
</div>
"""


def carte_anecdote(origine: str, drapeau: str, anecdote: str, fun_fact: str, authenticite: str):
    """Carte immersion culturelle : drapeau + anecdote + fun fact + niveau d'authenticite."""
    auth_colors = {
        "Traditionnel": ("#22C55E", "Recette traditionnelle authentique"),
        "Adapte": ("#F59E0B", "Recette adaptee aux ingredients dispos"),
        "Fusion": ("#A855F7", "Fusion creative de cuisines"),
    }
    auth_color, auth_desc = auth_colors.get(authenticite, ("#64748B", authenticite))

    return f"""
<div style="
  background: linear-gradient(135deg, #FEF3C7 0%, #FEE2E2 100%);
  padding: 24px;
  border-radius: 16px;
  border: 1px solid #FCA5A5;
  margin-top: 16px;
">
  <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;">
    <div style="font-size: 56px; line-height: 1;">{drapeau}</div>
    <div>
      <div style="font-size: 12px; color: #92400E; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Origine</div>
      <div style="font-size: 22px; font-weight: 800; color: #7C2D12;">{origine}</div>
    </div>
  </div>
  <p style="font-size: 14px; color: #44403C; line-height: 1.6; margin-bottom: 12px;">{anecdote}</p>
  <div style="
    background: rgba(255,255,255,0.6);
    padding: 12px 16px;
    border-radius: 10px;
    border-left: 3px solid #F59E0B;
    margin-bottom: 12px;
  ">
    <div style="font-size: 11px; color: #92400E; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; margin-bottom: 4px;">🎲 Le saviez-vous</div>
    <div style="font-size: 13px; color: #44403C;">{fun_fact}</div>
  </div>
  <div style="
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    background: {auth_color}22;
    border: 1px solid {auth_color};
    border-radius: 16px;
    font-size: 12px;
    font-weight: 600;
    color: {auth_color};
  ">
    <span style="width: 6px; height: 6px; border-radius: 50%; background: {auth_color};"></span>
    {authenticite} - {auth_desc}
  </div>
</div>
"""


def score_compatibilite(score: int):
    """Affichage du score de compatibilite ingredients/cuisine en cercle anime."""
    if score >= 80:
        color = "#22C55E"
        label = "Excellent match"
    elif score >= 60:
        color = "#F59E0B"
        label = "Bon match"
    else:
        color = "#EF4444"
        label = "Match partiel"

    circumference = 2 * 3.14159 * 40
    dash = (score / 100) * circumference

    return f"""
<div style="
  display: flex;
  align-items: center;
  gap: 16px;
  background: white;
  padding: 16px 20px;
  border-radius: 14px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  border: 1px solid #E2E8F0;
">
  <svg width="100" height="100" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40" fill="none" stroke="#F1F5F9" stroke-width="10"/>
    <circle cx="50" cy="50" r="40" fill="none" stroke="{color}" stroke-width="10"
            stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
            transform="rotate(-90 50 50)"
            style="transition: stroke-dasharray 1s ease-out;"/>
    <text x="50" y="55" text-anchor="middle" font-size="22" font-weight="700" fill="#1E293B">{score}</text>
  </svg>
  <div>
    <div style="font-size: 11px; color: #64748B; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Compatibilite</div>
    <div style="font-size: 16px; font-weight: 700; color: #1E293B;">{label}</div>
    <div style="font-size: 12px; color: #64748B;">Ingredients vs cuisine</div>
  </div>
</div>
"""


def how_it_works():
    """Section 'Comment ca marche' en 3 etapes — design editorial asymetrique."""
    return """
<div style="margin: 60px auto; max-width: 1000px; font-family: -apple-system, sans-serif;">
  <div style="text-align: center; margin-bottom: 8px;">
    <span style="font-family: 'Brush Script MT', cursive; font-size: 32px; color: #C97B5F; font-style: italic;">une recette en</span>
  </div>
  <h2 style="text-align: center; font-family: 'Cormorant Garamond', Georgia, serif; font-size: 56px; color: #2D2A26; margin: 0 0 56px 0; font-weight: 700; font-style: italic; letter-spacing: -1.5px;">trois mouvements</h2>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 48px; align-items: start;">
    <div style="text-align: left;">
      <div style="font-family: 'Cormorant Garamond', serif; font-size: 88px; color: #C97B5F; font-style: italic; line-height: 0.8; margin-bottom: 16px; font-weight: 300;">i.</div>
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; color: #2D2A26; margin-bottom: 12px; font-weight: 600; line-height: 1.2;">Sors ce qu'il te reste</h3>
      <p style="font-size: 15px; color: #5C5751; line-height: 1.7;">Le poulet du dimanche, l'oignon orphelin, ces epinards qui te jugent. Tout est bon.</p>
    </div>
    <div style="text-align: left; padding-top: 40px;">
      <div style="font-family: 'Cormorant Garamond', serif; font-size: 88px; color: #8B9A6C; font-style: italic; line-height: 0.8; margin-bottom: 16px; font-weight: 300;">ii.</div>
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; color: #2D2A26; margin-bottom: 12px; font-weight: 600; line-height: 1.2;">Voyage en cuisine</h3>
      <p style="font-size: 15px; color: #5C5751; line-height: 1.7;">Marrakech, Hanoi, Naples, Mexico — choisis ta destination du soir.</p>
    </div>
    <div style="text-align: left;">
      <div style="font-family: 'Cormorant Garamond', serif; font-size: 88px; color: #2D2A26; font-style: italic; line-height: 0.8; margin-bottom: 16px; font-weight: 300;">iii.</div>
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; color: #2D2A26; margin-bottom: 12px; font-weight: 600; line-height: 1.2;">Cuisine, ecoute, savoure</h3>
      <p style="font-size: 15px; color: #5C5751; line-height: 1.7;">Recette pas-a-pas, anecdote du pays, minuteur, coup de main du chef.</p>
    </div>
  </div>
</div>
"""


def temoignages():
    """Section temoignages — citations sobres, style editorial."""
    return """
<div style="margin: 80px auto; max-width: 1000px; font-family: -apple-system, sans-serif;">
  <div style="text-align: center; margin-bottom: 56px;">
    <span style="font-family: 'Brush Script MT', cursive; font-size: 28px; color: #C97B5F; font-style: italic;">murmures de</span>
    <h2 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 48px; color: #2D2A26; margin: 4px 0 0 0; font-weight: 700; font-style: italic;">chefs imaginaires</h2>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 56px;">
    <div style="border-left: 2px solid #C97B5F; padding-left: 20px;">
      <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 20px; color: #2D2A26; line-height: 1.5; margin-bottom: 20px;">« J'ai retrouve le tajine de ma grand-mere a partir d'un poulet et trois oignons. »</p>
      <div style="font-size: 11px; color: #5C5751; text-transform: uppercase; letter-spacing: 2px;">Karim B. — Marrakech 🇲🇦</div>
    </div>
    <div style="border-left: 2px solid #8B9A6C; padding-left: 20px;">
      <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 20px; color: #2D2A26; line-height: 1.5; margin-bottom: 20px;">« Un ramen italo-japonais qui a fait sensation. Avec l'anecdote du miso, en plus. »</p>
      <div style="font-size: 11px; color: #5C5751; text-transform: uppercase; letter-spacing: 2px;">Yuki T. — Tokyo 🇯🇵</div>
    </div>
    <div style="border-left: 2px solid #2D2A26; padding-left: 20px;">
      <p style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 20px; color: #2D2A26; line-height: 1.5; margin-bottom: 20px;">« Le minuteur pas-a-pas m'a sauve un risotto que je croyais perdu. »</p>
      <div style="font-size: 11px; color: #5C5751; text-transform: uppercase; letter-spacing: 2px;">Lorenzo M. — Florence 🇮🇹</div>
    </div>
  </div>
</div>
"""


def footer_cuisines():
    """Footer — palette terracotta + sage, style editorial sobre."""
    return """
<div style="
  margin-top: 80px;
  padding: 56px 32px;
  background: #2D2A26;
  color: #FAF7F2;
  border-top: 4px solid #C97B5F;
  font-family: -apple-system, sans-serif;
">
  <div style="max-width: 1000px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 32px;">
      <span style="font-family: 'Brush Script MT', cursive; font-size: 26px; color: #C97B5F; font-style: italic;">dix-huit pays,</span>
      <h3 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 38px; margin: 4px 0 0 0; font-weight: 700; font-style: italic; color: #FAF7F2;">une seule assiette</h3>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: center; margin-bottom: 48px; font-size: 14px; letter-spacing: 1px;">
      <span>🇫🇷 France</span>
      <span style="color: #5C5751;">·</span>
      <span>🇮🇹 Italie</span>
      <span style="color: #5C5751;">·</span>
      <span>🇪🇸 Espagne</span>
      <span style="color: #5C5751;">·</span>
      <span>🇬🇷 Grece</span>
      <span style="color: #5C5751;">·</span>
      <span>🇨🇳 Chine</span>
      <span style="color: #5C5751;">·</span>
      <span>🇯🇵 Japon</span>
      <span style="color: #5C5751;">·</span>
      <span>🇹🇭 Thailande</span>
      <span style="color: #5C5751;">·</span>
      <span>🇻🇳 Vietnam</span>
      <span style="color: #5C5751;">·</span>
      <span>🇮🇳 Inde</span>
      <span style="color: #5C5751;">·</span>
      <span>🇰🇷 Coree</span>
      <span style="color: #5C5751;">·</span>
      <span>🇲🇦 Maroc</span>
      <span style="color: #5C5751;">·</span>
      <span>🇹🇳 Tunisie</span>
      <span style="color: #5C5751;">·</span>
      <span>🇹🇷 Turquie</span>
      <span style="color: #5C5751;">·</span>
      <span>🇱🇧 Liban</span>
      <span style="color: #5C5751;">·</span>
      <span>🇺🇸 USA</span>
      <span style="color: #5C5751;">·</span>
      <span>🇲🇽 Mexique</span>
      <span style="color: #5C5751;">·</span>
      <span>🇰🇪 Kenya</span>
      <span style="color: #5C5751;">·</span>
      <span>🇪🇬 Egypte</span>
    </div>
    <div style="text-align: center; color: #8B7E70; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; padding-top: 32px; border-top: 1px solid #5C5751;">
      NutriRecettes — Projet etudiant — Cuisine generee par IA
    </div>
  </div>
</div>
"""
