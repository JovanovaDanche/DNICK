from django import forms

from suplementApp.models import Supplement


class SupplementForm(forms.ModelForm):
    class Meta:
        model = Supplement
        fields = '__all__'