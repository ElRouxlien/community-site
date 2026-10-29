from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

"""Role: formulaire d inscription utilisateur.
    Function: ajoute l email aux champs de creation.
    Context: utilise par la vue d inscription."""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

"""Role: formulaire de mise a jour du compte.
    Function: permet de modifier nom d utilisateur et email.
    Context: utilise par la page profil."""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

"""Role: formulaire de mise a jour du profil.
    Function: permet de changer l image de profil.
    Context: utilise par la page profil."""
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
