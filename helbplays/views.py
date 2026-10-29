import base64
import requests
from django.shortcuts import render
from django.conf import settings

CHAT_BASE_URL = "https://helbplays2526.alwaysdata.net"
CHAT_TEXT_PATH = "/chat.txt"
CHAT_FRAME_PATH = "/frame.jpg"
CHAT_SEND_PATH = "/chat.php"


"""Role: integre le flux Helbplays dans l app.
    Function: lit le chat distant, affiche l image, envoie un message.
    Context: utilise par la page d accueil de l app Helbplays."""
def helbplays_home(request):
    chat_url = f"{CHAT_BASE_URL}{CHAT_TEXT_PATH}"
    chat_content = requests.get(chat_url).text

    image_url = f"{CHAT_BASE_URL}{CHAT_FRAME_PATH}"

    if request.method == "POST":
        user = request.user.username
        message = request.POST.get("message")
        key = settings.HELBPLAYS_KEY

        username64 = base64.b64encode(user.encode()).decode()
        message64 = base64.b64encode(message.encode()).decode()
        key64 = base64.b64encode(key.encode()).decode()

        send_url = (
            f"{CHAT_BASE_URL}{CHAT_SEND_PATH}"
            f"?username={username64}&message={message64}&key={key64}"
        )

        requests.get(send_url)

    return render(request, "helbplays/home.html", {
        "chat": chat_content.split("\n"),
        "image_url": image_url,
    })
