# Projet : Premiers pas avec les API de ChatGPT

## **Prérequis : Installer Python** ![Python](img/python_65.png)

- A [Quick Guide for Installing](https://github.com/PackeTsar/Install-Python/blob/master/README.md#install-python-) Python on Common Operating Systems
- Download the latest version of [Python 3.12](https://www.python.org/downloads/)

## Créer un environnement virtuel :

(Windows)
```
python -m venv env
```

(MacOS)
```
python3 -m venv env
```

## Activer l'environnement virtuel :

```
source env/bin/activate
```

## Installation:
(Windows)
```
pip install -r requirements.txt
```

(MacOS)

```
pip3 install -r requirements.txt
```

## [Ajouter une clé API](https://platform.openai.com/account/api-keys)

.env file

OPENAI_API_KEY=sk-brHeh...A39v5iXsM2

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`


## Démarrer le projet :

(Windows)
```
python main.py
```

(MacOS)
```
python3 main.py
```
