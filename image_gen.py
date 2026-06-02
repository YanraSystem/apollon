"""
Generation d'image du plat via Pollinations.ai (gratuit, sans cle API).
Modele 'turbo' = 3x plus rapide que le default flux.
"""

import hashlib
import urllib.parse


def image_url_for(plat: str, origine: str = "") -> str:
    """Construit une URL Pollinations.ai qui genere une photo realiste du plat.
    Seed deterministe base sur le nom du plat → meme plat = meme image (cache backend)."""
    prompt = f"professional food photography of {plat}"
    if origine:
        prompt += f", {origine} cuisine"
    prompt += ", appetizing, top view, restaurant plating, warm light, hyperrealistic, 4k"

    seed = int(hashlib.md5(plat.encode()).hexdigest()[:8], 16) % 1000000
    encoded = urllib.parse.quote(prompt)
    return (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width=640&height=480&model=turbo&nologo=true&seed={seed}"
    )
