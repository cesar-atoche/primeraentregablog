from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from blog.forms import articuloFormulario, categoriaFormulario, comentarioFormulario
from blog.models import Articulo, Categoria, Comentario

# inicio
def inicio(request):
    urls = {"Categoria", "Articulos", "Comentarios"}
    titulo = "Formularios"
    contenido = {"urls": urls, "titulo": titulo}
    return render(request, "index.html", contenido)


def categoria(request):
    titulo = "Categoria"
    if request.method != "POST":
        formulario = categoriaFormulario()
    else:
        formulario = categoriaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            articulo = Categoria(nombre=informacion["nombre"])
            articulo.save()
            return render(request, "respuesta.html", {"titulo": titulo})
    contenido = {"formulario": formulario, "titulo": titulo}
    return render(request, "categoria.html", contenido)


def articulos(request):
    titulo = "Articulos"
    if request.method != "POST":
        formulario = articuloFormulario()
    else:
        formulario = articuloFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            articulo = Articulo(
                titulo=informacion["titulo"],
                texto=informacion["texto"],
                fecha=informacion["fecha"],
                estado=informacion["estado"],
            )
            articulo.save()
            return render(request, "respuesta.html", {"titulo": titulo})
    contenido = {"formulario": formulario, "titulo": titulo}
    return render(request, "articulos.html", contenido)


def comentarios(request):
    titulo = "Comentarios"
    if request.method != "POST":
        formulario = comentarioFormulario()
    else:
        formulario = comentarioFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            articulo = Comentario(
                comentario=informacion["comentario"],
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                fecha=informacion["fecha"],
                estado=informacion["estado"],
            )
            articulo.save()
            return render(request, "respuesta.html", {"titulo": titulo})
    contenido = {"formulario": formulario, "titulo": titulo}
    return render(request, "comentarios.html", contenido)


def buscar(request):
    titulo = "Buscar"
    return render(request, "buscar.html", {"titulo": titulo})


def respuestaBuscar(request):
    titulo = "Resultado de Busqueda"
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        filtro = Comentario.objects.filter(nombre__icontains=nombre)
        contenido = {"filtro": filtro, "titulo": titulo, "buscando": nombre}
        return render(request, "respuesta_busqueda.html", contenido)
    else:
        respuesta = "No enviaste datos"
        return render(
            request,
            "respuesta_busqueda.html",
            {"respuesta": respuesta, "titulo": titulo},
        )
