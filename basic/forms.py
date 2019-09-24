from django import forms
from .models import Obit


class ObitForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-class",
        "placeholder": "Imię"
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-class",
        "placeholder": "Nazwisko"
    }))
    cemetery_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-class",
        "placeholder": "Cmentarz"
    }))
    cemetery_address = forms.CharField(max_length=300, widget=forms.TextInput(attrs={
        "class": "form-class",
        "placeholder": "Adres cmentarza"
    }))
    church_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-class",
        "placeholder": "Kościół"
    }))
    church_address = forms.CharField(max_length=300, widget=forms.TextInput(attrs={
        "class": "form-class",
        "placeholder": "Adres Kościoła"
    }))
    born_date = forms.DateField()
    death_date = forms.DateField()
    description = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={
        "class": "form-class",
        "rows": 20,
        "cols": 120
    }))

    class Meta:
        model = Obit
        fields = [
            'first_name', 'last_name', 'cemetery_name', 'cemetery_address', 'church_name', 'church_address',
            'born_date', 'death_date', 'description'
        ]
