from django.db import models
from django.contrib.auth.models import User
from PIL import Image

PROFILE_IMAGE_DEFAULT = "default.jpg"
PROFILE_IMAGE_MAX_SIZE = 300


"""Role: represente le profil utilisateur et son image.
    Function: stocke l image et gere le redimensionnement.
    Context: utilise par les formulaires de profil et les templates."""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=PROFILE_IMAGE_DEFAULT, upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > PROFILE_IMAGE_MAX_SIZE or img.width > PROFILE_IMAGE_MAX_SIZE:
            output_size = (PROFILE_IMAGE_MAX_SIZE, PROFILE_IMAGE_MAX_SIZE)
            img.thumbnail(output_size)
            img.save(self.image.path)
