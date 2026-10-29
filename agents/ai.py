import os
import requests

LOCAL_CHAT_URL = "http://localhost:11434/api/chat"
EXTERNAL_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
EXTERNAL_MODEL_NAME = "gpt-3.5-turbo"
EXTERNAL_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

""" Role: adapte une requete vers un modele local.
    Function: prepare la charge utile et retourne la reponse texte.
    Context: utilise par le chat quand l agent est configure en local."""
def generate_local_reply(agent, user_message):
    
    data = {
        "model": agent.model_name,
        "messages": [
            {"role": "system", "content": agent.system_prompt},
            {"role": "user", "content": user_message}
        ],
        "stream": False
    }

    response = requests.post(LOCAL_CHAT_URL, json=data)

    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        return "(Erreur IA locale)"

""" Role: envoie une requete vers une API externe.
    Function: construit les en-tetes, poste la requete et renvoie le texte.
    Context: utilise par le chat quand l agent est configure en API."""
def generate_external_reply(agent, user_message):
    
    if not EXTERNAL_API_KEY:
        return "(Erreur : clé API absente)"

    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": EXTERNAL_MODEL_NAME,
        "messages": [
            {"role": "system", "content": agent.system_prompt},
            {"role": "user", "content": user_message}
        ],
    }

    response = requests.post(EXTERNAL_CHAT_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "(Erreur IA externe)"

""" Role: selectionne la strategie de reponse pour un agent.
    Function: route vers le fournisseur local ou externe selon le type.
    Context: point d entree unique utilise par les vues de chat."""
def generate_reply(agent, user_message):
    
    if agent.model_type == "local":
        return generate_local_reply(agent, user_message)
    elif agent.model_type == "api":
        return generate_external_reply(agent, user_message)
    else:
        return "(Aucun modèle IA sélectionné)"
