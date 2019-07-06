from django import forms
from app.models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nome',
            'cnpj',
            'email',
            'telefone',
            'endereco',
        ]



