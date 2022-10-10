from django import forms


class articuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    texto = forms.CharField()
    fecha = forms.DateField()
    estado = forms.CharField(max_length=10)


class categoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)


class comentarioFormulario(forms.Form):
    comentario = forms.CharField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    fecha = forms.DateField()
    estado = forms.BooleanField()
