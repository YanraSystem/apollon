"""
NutriRecettes API — FastAPI wrapper autour du moteur Python existant.

Expose les fonctions de recipe_engine, image_gen et pdf_export via REST.
Le code Streamlit a la racine reste intact (legacy).
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# Charge le .env qui est a la racine du projet (un niveau au-dessus de api/)
ROOT_ENV = Path(__file__).resolve().parent.parent / ".env"
if ROOT_ENV.exists():
    load_dotenv(ROOT_ENV)
else:
    load_dotenv()  # fallback : variables d'env systeme / .env courant

from recipe_engine import get_recipe  # noqa: E402
from image_gen import image_url_for  # noqa: E402

app = FastAPI(
    title="NutriRecettes API",
    description="API REST autour du moteur Claude + TheMealDB + Spoonacular.",
    version="1.0.0",
)

# CORS : dev local Next.js + previews/prod Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- Pydantic models ----------

class RecipeRequest(BaseModel):
    ingredients: list[str] = Field(..., min_length=1, description="Liste d'ingredients en francais")
    cuisine: str = Field(default="Surprends-moi", description="Style de cuisine")
    personnes: int = Field(default=2, ge=1, le=20, description="Nombre de personnes")
    regime: str = Field(default="Aucun", description="Regime alimentaire")


class PdfRequest(BaseModel):
    recipe: dict
    personnes: int = Field(default=2, ge=1, le=20)
    regime: str = Field(default="Aucun")


# ---------- Endpoints ----------

@app.get("/api/health")
def health():
    """Healthcheck simple pour Render et monitoring."""
    return {"status": "ok"}


@app.post("/api/recipe")
def post_recipe(payload: RecipeRequest):
    """Genere ou recupere une recette complete (Claude + TheMealDB)."""
    try:
        recipe = get_recipe(
            ingredients=payload.ingredients,
            cuisine=payload.cuisine,
            personnes=payload.personnes,
            regime=payload.regime,
        )
        return recipe
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Erreur lors de la generation de la recette",
                "code": "recipe_generation_failed",
                "details": {"message": str(exc)},
            },
        )


@app.get("/api/image")
def get_image(
    plat: str = Query(..., description="Nom du plat"),
    origine: str = Query(default="", description="Origine / pays du plat"),
    nom_image: str = Query(default="", description="Mot-cle anglais pour Spoonacular"),
):
    """Retourne une URL d'image (Spoonacular puis Pollinations en fallback)."""
    try:
        url = image_url_for(plat=plat, origine=origine, nom_image=nom_image)
        return {"url": url}
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Erreur lors de la recuperation de l'image",
                "code": "image_lookup_failed",
                "details": {"message": str(exc)},
            },
        )


@app.post("/api/recipe/pdf")
def post_recipe_pdf(payload: PdfRequest):
    """Export PDF d'une recette. Placeholder dans la v1 (501 Not Implemented)."""
    return JSONResponse(
        status_code=501,
        content={
            "error": "Export PDF non implemente dans la v1 de l'API",
            "code": "not_implemented",
            "details": {"hint": "Sera ajoute apres validation de la migration Next.js."},
        },
    )


@app.get("/")
def root():
    """Page d'accueil minimale (utile pour verifier deploy)."""
    return {
        "name": "NutriRecettes API",
        "version": "1.0.0",
        "endpoints": ["/api/health", "/api/recipe", "/api/image", "/api/recipe/pdf"],
    }
