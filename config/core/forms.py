from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'tu@email.com'}),
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Escribí tu mensaje', 'rows': 5}),
    )
