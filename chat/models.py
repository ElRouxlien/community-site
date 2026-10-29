from django.db import models
from django.contrib.auth.models import User
from agents.models import Agent


"""Role: represente un message echange avec un agent.
    Function: stocke contenu, auteur, agent et horodatage.
    Context: utilise par les vues de chat et les stats."""
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    content = models.TextField()
    is_user = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}"
