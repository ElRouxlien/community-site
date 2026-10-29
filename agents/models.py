from django.db import models
from django.contrib.auth.models import User

MODEL_TYPE_LOCAL = "local"
MODEL_TYPE_API = "api"
DEFAULT_COOLDOWN_SECONDS = 5

"""Role: represente un agent IA configurable par un utilisateur.
    Function: stocke les parametres de generation et la visibilite publique.
    Context: utilise par les vues agents et le module de chat pour choisir un agent."""
class Agent(models.Model):

    MODEL_CHOICES = [
        (MODEL_TYPE_LOCAL, 'IA locale (smollm:135m)'),
        (MODEL_TYPE_API, 'IA externe (API)'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agents")
    name = models.CharField(max_length=50)
    description = models.TextField()
    system_prompt = models.CharField(max_length=255)
    model_type = models.CharField(
        max_length=10,
        choices=MODEL_CHOICES,
        default=MODEL_TYPE_LOCAL
    )
    model_name = models.CharField(max_length=100)
    cooldown = models.IntegerField(default=DEFAULT_COOLDOWN_SECONDS)
    avatar = models.ImageField(upload_to="agent_avatars/", null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
