# 🚖 Projet NYC Taxi – Snowflake & DBT Core

Bienvenue dans le repository du projet **NYC Taxi** !  
Ce projet montre comment **charger, transformer et analyser des données de taxis new-yorkais** en utilisant **Snowflake** et **DBT Core**.  
Il sert aussi de **guide / aide-mémoire** pour les futurs projets similaires.

---

## 📂 Contenu du repository

### 📝 Fichiers principaux
- **`Brief Taxi New York.odt`**  
  Étapes détaillées suivies lors de la réalisation du brief. Une vraie bible pour les débutants Snowflake et DBT.
- **`STRUCTURE DE LA TABLE YELLOW_TAXI_TRIPS.ods`**  
  Résultats de requêtes pour jauger la qualité des données source.

### 📝 Chargement des fichiers sur le blob Azure
- **`requirements.txt`** : dépendances Python nécessaires.
- **`nyc-venv`** : environnement virtuel Python. 


### 📸 Captures d’écran
- Dossier regroupant toutes les captures d’écran de la **création de l’architecture dans Snowflake**.

### 💻 DBT Core
La partie du projet codée entièrement en **lignes de commande depuis VSCode**.  
Contenu du dossier :

- **`dbt-venv`** : environnement virtuel Python pour DBT Core.  
- **`logs/`** : fichiers de logs pour suivre les exécutions.  
- **`requirements.txt`** : dépendances Python nécessaires.  
- **`WW_Address_Data/`** : projet principal avec la logique de création des tables et transformations DBT.

### ⚙️ Scripts utiles
- **`csv_load.py`** : lancer le chargement des fichiers sur Azure.  
- **`run_dbt.py`** : lancer le debug pour vérifier la configuration du projet.  
- **`build_dbt.py`** : compiler le projet DBT.

### 🔒 Variables & sécurité
- Les variables de connexion sont dans **`.env`** (non inclus dans le repo pour protéger les informations sensibles).  
- **`.gitignore`** : pour éviter de versionner les données sensibles.

---

## 🎯 Objectifs de la partie DBT Core

1. **Récupérer des données** depuis une bibliothèque gratuite du **Marketplace de Snowflake**.  
2. **Créer des tables NYC Taxi** avec les adresses de 3 pays :  
   - **États-Unis** : chargement classique.  
   - **Autres pays** : génération automatique via **Jinja**, en bouclant sur une liste de pays définie dans les variables du projet.

---

## 🚀 Bonus

- Le projet est entièrement **scriptable** depuis VSCode et DBT Core.  
- Prêt à être utilisé comme **template pour de futurs projets data** sur Snowflake.  
- Les bonnes pratiques **sécurité et modularité** sont appliquées (variables sensibles, structure de dossiers, environnement virtuel, lineage actif).
- Il est orchestré par github actions.

---

> _Pro-tip_: Pense à **activer ton `dbt-venv`** avant d’exécuter les scripts pour éviter tout conflit de dépendances.
