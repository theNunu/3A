from django import forms

class newCreateClientForm(forms.Form):
    nombre = forms.CharField(label="Ingesa tu nickname", max_length=50)
    correo = forms.EmailField(label="Ingesa tu email", max_length=50)
    telefono = forms.CharField(label="Número celular", max_length=10)

