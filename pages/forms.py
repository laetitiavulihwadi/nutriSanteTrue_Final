from django import forms
from .models import *

class RecetteForm(forms.ModelForm):
    nom = forms.CharField(label="Titre", validators=[validate_name,alphanumeric])
    description = forms.CharField(label="Description", widget=forms.Textarea, validators=[alphanumeric])
    photo = forms.ImageField(label="Photo", required=False)

    class Meta:
        model = Recette
        fields = ['nom', 'description', 'photo']
        
class UserAgentForm(forms.ModelForm):
    nom = forms.CharField(label="Nom")
    code = forms.CharField(label="Code")
    
    class Meta:
        model = UserAgent
        fields = ['nom', 'code']
    