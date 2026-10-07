from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
        labels = {'autor': 'Tu nombre', 'texto': 'Tu comentario'}
        widgets = {'texto': forms.Textarea(attrs={'rows': 4})}