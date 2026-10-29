from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'play_color']
        widgets = {
            'play_color': forms.RadioSelect
        }
