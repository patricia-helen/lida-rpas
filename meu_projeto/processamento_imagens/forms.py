# processamento_imagens/forms.py
from django import forms
from .models import GeospatialImage  # Modelo associado ao formulário

# Formulário para upload de imagens, com campos adicionais para flexibilidade
class UploadForm(forms.ModelForm):
    additional_info = forms.CharField(
        required=False,
        label='Informações Adicionais',  # Alteração para português
        widget=forms.Textarea,
    )

    class Meta:
        model = GeospatialImage  # Associe o ModelForm ao modelo
        fields = ['image', 'description', 'additional_info']  # Campos do formulário
