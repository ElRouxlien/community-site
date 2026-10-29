# Community Site

Plateforme communautaire développée avec **Django** dans le cadre du cours de Web II (HELB).

## Fonctionnalités

- **Blog** : création, modification et suppression d'articles
- **Comptes utilisateurs** : inscription, connexion, profil avec photo
- **Agents IA** : chaque utilisateur crée ses propres agents (prompt système, modèle, délai, avatar, public/privé)
- **Chat avec les agents** : via un modèle local (Ollama, `smollm:135m`) ou une API externe (OpenRouter)
- **Statistiques** : graphiques d'activité des messages
- **Helbplays** : intégration d'un chat et d'un flux d'images distants

## Technologies

Python · Django · Bootstrap 4 (crispy-forms) · SQLite · Ollama / OpenRouter

## Lancer le projet

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Variables d'environnement (voir `.env.example`) :

| Variable | Rôle |
|---|---|
| `DJANGO_SECRET_KEY` | Clé secrète Django |
| `OPENROUTER_API_KEY` | Clé pour les agents « IA externe » |
| `HELBPLAYS_KEY` | Clé d'envoi de messages vers Helbplays |

Pour les agents locaux, [Ollama](https://ollama.com) doit tourner sur `localhost:11434` avec le modèle `smollm:135m`.

## Rapport

Le rapport final du projet est disponible dans [`RapportFinalWebIIJulienBaron.pdf`](RapportFinalWebIIJulienBaron.pdf).
