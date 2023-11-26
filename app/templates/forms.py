from django impport forms

class Registro (forms.Form):
    name= forms.Charfield(label="Ingesa tu nickname", max length=200)
