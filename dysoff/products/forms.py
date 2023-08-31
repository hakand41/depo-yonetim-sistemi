from django import forms
from . import models

class ResimForm(forms.ModelForm):
    class Meta:
        model = models.Resim
        fields = ["resim", "title"]

class UrunForm(forms.ModelForm):
    class Meta:
        model = models.Urun
        fields = ["urun_adi", "urun_adedi", "resim"]

class FaturaForm(forms.ModelForm):
    class Meta:
        model = models.Fatura
        fields = ["urun", "fiyat"]