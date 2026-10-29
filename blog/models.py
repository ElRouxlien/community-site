from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

""" Role: represente un article de blog.
    Function: stocke le contenu, la date et l auteur, plus la couleur de jeu.
    Context: utilise par les vues CRUD du blog et les templates."""
class Post(models.Model):
    

    PLAY_COLOR_CHOICES = [
        ('red', 'Rouge'),
        ('blue', 'Bleu'),
        ('green', 'Vert'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    play_color = models.CharField(
        max_length = 20,
        choices = PLAY_COLOR_CHOICES,
        default = 'red'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
