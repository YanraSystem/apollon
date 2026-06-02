# NutriRecettes

Site web en Python qui genere une recette de cuisine **europeenne, asiatique ou orientale** a partir des aliments que tu coches. Pense comme le **complement nutrition de l'app sport** du groupe.

---

## Ce que ca fait

1. Tu coches les aliments que t'as dans le frigo (proteines, legumes, feculents, herbes, laitiers)
2. Tu choisis ton style de cuisine (europeenne / asiatique / orientale / surprise)
3. Tu choisis le nombre de personnes et ton regime (vegetarien, halal, sans gluten, sans lactose)
4. Tu cliques sur "Generer ma recette"
5. L'app cherche d'abord dans une vraie base de recettes (TheMealDB), si rien matche ou si t'as choisi un style oriental/asiatique elle bascule sur **Gemini IA** pour t'inventer une recette
6. Une image realiste du plat est generee automatiquement
7. Tu peux **telecharger la recette en PDF**

Bonus :
- Score nutritionnel live : proteines / legumes / feculents
- Astuce du chef sur les recettes IA
- Footer qui fait le lien avec l'app sport du groupe

---

## Comment lancer le projet (a faire UNE SEULE FOIS)

### Etape 1 : Installer Python

Verifie que t'as Python 3.10 ou plus recent :

```bash
python3 --version
```

Si t'as rien, va sur https://www.python.org/downloads/ et installe la derniere version.

### Etape 2 : Telecharger le projet

Recupere le dossier `recette-collegue` (zip ou clone git) et ouvre un terminal **dedans**.

### Etape 3 : Installer les dependances

```bash
pip3 install -r requirements.txt
```

### Etape 4 : Creer ta cle API Gemini (gratuit, 2 minutes)

1. Va sur https://aistudio.google.com/app/apikey
2. Connecte-toi avec ton compte Google
3. Clique sur **"Create API Key"**
4. Copie la cle qui s'affiche
5. Dans le dossier du projet, **renomme** `.env.example` en `.env`
6. Ouvre `.env` avec un editeur de texte (Notepad, TextEdit, VS Code...)
7. Remplace `ta_cle_ici` par ta vraie cle. Resultat :

```
GEMINI_API_KEY=AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Etape 5 : Lancer l'app

```bash
streamlit run app.py
```

L'app s'ouvre automatiquement dans ton navigateur sur `http://localhost:8501`.

**C'est tout. T'as plus rien a coder.**

---

## Demo de presentation (a montrer au prof)

Pour que ca claque a l'oral, prepare ces 3 exemples :

| Demo | Aliments a cocher | Style | Effet |
|------|------------------|-------|-------|
| 1. **Couscous express** | Agneau, Carotte, Courgette, Semoule, Ras el hanout | Orientale | Recette IA, image, PDF |
| 2. **Wok asiat** | Poulet, Poivron, Riz, Gingembre, Ail | Asiatique | Recette IA exotique |
| 3. **Pates italiennes** | Tomate, Pates, Basilic, Ail | Europeenne | Vraie recette TheMealDB |

Pour chaque demo, montre le **score nutritionnel** qui evolue en live quand tu coches.

---

## Comment expliquer le projet au prof

**Argumentaire technique :**

> "On a fait un site web en **Python avec Streamlit**, qui combine **une API gratuite de recettes (TheMealDB)** pour les plats europeens classiques et **l'IA Gemini de Google** pour les cuisines plus complexes comme l'orientale ou l'asiatique. L'app genere aussi des images via **Pollinations.ai** et un **export PDF avec fpdf2**. C'est le complement nutrition de l'app sport developpee par le reste du groupe."

**Si le prof demande comment ca marche techniquement :**

- `app.py` : interface Streamlit (le site web)
- `recipe_engine.py` : moteur qui interroge TheMealDB + Gemini
- `image_gen.py` : construit l'URL Pollinations pour l'image du plat
- `pdf_export.py` : genere le PDF avec la lib fpdf2
- Donnees user : pas stockees, tout est en session locale = **respect RGPD**

---

## Deployer en ligne sur Streamlit Cloud (gratuit, URL partageable au prof)

> Note : on n'utilise PAS Vercel pour ce projet. Vercel est concu pour Next.js / serverless. Streamlit a besoin d'un serveur Python persistant — Streamlit Community Cloud est l'option officielle, gratuite et zero-config.

1. Va sur https://share.streamlit.io
2. Connecte-toi avec ton compte GitHub
3. Clique **"New app"** → choisis le repo `nutrirecettes` → branche `main` → main file `app.py`
4. Clique **"Advanced settings"** → **"Secrets"** → colle :
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-api03-..."
   ```
5. **"Deploy"** → l'app est en ligne en 2-3 minutes a une URL type `https://nutrirecettes-xxx.streamlit.app`

Auto-deploy : chaque `git push` sur `main` redeploie automatiquement.

---

## Structure du projet

```
recette-collegue/
├── app.py              # Interface Streamlit (lance avec : streamlit run app.py)
├── recipe_engine.py    # TheMealDB + Gemini IA
├── image_gen.py        # Generation image plat (Pollinations.ai)
├── pdf_export.py       # Export PDF de la recette
├── requirements.txt    # Liste des libs Python a installer
├── .env.example        # Modele pour ta cle API (a renommer en .env)
├── .gitignore          # Fichiers a ignorer si tu utilises git
└── README.md           # Ce fichier
```

---

## En cas de probleme

| Probleme | Solution |
|----------|----------|
| `streamlit: command not found` | Refais `pip3 install -r requirements.txt`, puis essaie `python3 -m streamlit run app.py` |
| `GEMINI_API_KEY non configuree` | Verifie que tu as bien renomme `.env.example` en `.env` et colle ta cle dedans |
| L'image du plat ne s'affiche pas | C'est Pollinations.ai qui rame parfois. Recharge la page. |
| TheMealDB renvoie rien | Normal pour cuisines exotiques, le fallback Gemini prend le relais |
| PDF illisible (caracteres bizarres) | Le PDF utilise latin-1 ; les caracteres tres exotiques sont remplaces auto |

---

## Credits

- **Streamlit** (interface) - https://streamlit.io
- **TheMealDB** (base de recettes, API gratuite) - https://www.themealdb.com
- **Google Gemini** (IA generative) - https://aistudio.google.com
- **Pollinations.ai** (images IA gratuites) - https://pollinations.ai
- **fpdf2** (export PDF) - https://py-pdf.github.io/fpdf2/
