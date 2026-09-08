# Lab 1 — Pipeline de données en couches

Ce lab met en œuvre un pipeline de données simple selon l'architecture **Bronze → Silver → Gold**, à partir du jeu de données public `tips` de Seaborn.

## Prérequis

- Python 3.10 ou plus récent
- Une connexion Internet lors de la première extraction

## Installation

Depuis le dossier `de-section1-lab` :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Sous macOS ou Linux, activez l'environnement avec `source .venv/bin/activate`.

## Exécution

```powershell
python lab1.py
```

Le script effectue les étapes suivantes :

1. télécharge le CSV source vers `data/bronze/tips_raw.csv` ;
2. nettoie et enrichit les données dans `data/silver/tips_clean.parquet` ;
3. valide le jeu Silver avec Pandera ;
4. crée les agrégats dans `data/gold/tips_summary.parquet` ;
5. exécute deux requêtes SQL DuckDB directement sur les fichiers Parquet.

## Structure

```text
.
├── lab1.py                 # point d'entrée du pipeline
├── pipeline/
│   ├── extract.py           # ingestion Bronze
│   ├── transform.py         # transformation Silver
│   ├── validate.py          # contrôles qualité
│   ├── aggregate.py         # agrégation Gold
│   └── query.py             # exemples SQL DuckDB
└── data/
    ├── bronze/
    ├── silver/
    └── gold/
```

## Dépendances

- `pandas` : lecture, transformation et agrégation des données ;
- `pyarrow` : écriture et lecture du format Parquet ;
- `pandera` : validation du schéma Silver ;
- `duckdb` : requêtes SQL sur Parquet.
