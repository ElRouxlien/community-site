from django import forms
from .models import Agent

"""Role: expose un formulaire pour editer un agent IA.
    Function: mappe les champs principaux de l agent.
    Context: utilise par les vues de creation et modification d agent."""
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            'name',
            'description',
            'system_prompt',
            'model_type',
            'model_name',
            'cooldown',
            'avatar',
        ]
