from django import forms
from projects.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "bio", "profession", "tech_stack", "profile_photo", 
        ]

        widgets = {
            "profession": forms.CheckboxSelectMultiple,
            "tech_stack": forms.CheckboxSelectMultiple,
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=[
            "name", "description","technology_used", "pro_image","demo_link", "github_link",
        ]
        widgets = {
            "technology_used": forms.CheckboxSelectMultiple,
        }
        