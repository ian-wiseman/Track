from django import forms 
from .models import Recruiter, Placement

class RecruiterCreateForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = "__all__"

class PlacementCreateForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = "__all__"