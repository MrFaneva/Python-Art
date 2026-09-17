# Python Art 🎨✨

Une collection de scripts de génération artistique algorithmique et mathématique développés en Python à l'aide des modules **Turtle** et **Colorsys**.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-red.svg)](https://github.com/PyCQA/flake8)

---

## 🖼️ Scripts Inclus

1. **`cardioid_shape.py`** : Trace mathématiquement une cardioïde en coordonnées polaires et cartésiennes, avec une mise en couleur dynamique basée sur les dégradés HSV/RGB.
2. **`fiery_sun_burst_desing.py`** : Génère un effet visuel flamboyant de type "explosion solaire" géométrique aux teintes chaleureuses (`#FFE0B2` à `#E65100`).
3. **`Rainbow_spiral.py`** : Trace une spirale multicolore en boucle infinie basée sur un angle magique et une variation dynamique de la palette de couleurs (`colorsys`).

---

## 🛠️ Stack Technique

* **Langage :** Python 3.10+
* **Moteur Graphique :** `turtle` (Intégré à la bibliothèque standard Python, requiert `python3-tk` sur Ubuntu/Linux)
* **Qualité de code & Linting :** Flake8 (normes PEP 8)
* **Typage Statique :** Mypy
* **Automatisation :** Makefile

---

## 🚀 Installation et Utilisation

### 1. Prérequis (Sous Linux/Ubuntu)
Assurez-vous d'avoir le paquet Tkinter installé pour Turtle :
    ```bash
    sudo apt update && sudo apt install python3-tk

---

2. Configurer l'environnement virtuel et installer les outils de linting
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install flake8 mypy

3. Lancer les animations via le Makefile
- Lancer la Cardioïde:
    ```bash
    make run-cardioid
- Lancer l'effet Solaire:
    ```bash
    make run-sun
- Lancer la Spirale Arc-en-ciel:
    ```bash
    make run-spiral

4. Vérifier la qualité du code
    ```bash
    make lint

👤 Auteur:
 - Henintsoa Faneva — Étudiant en double cursus Physique et Application à l'Université d'Antananarivo  & Informatique (IGGLIA / ISPM ).
