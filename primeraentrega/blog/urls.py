from django.urls import path
from blog import views
urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('articulos/', views.articulos,name="Articulos"),
    path('categoria/', views.categoria,name="Categoria"),
    path('comentarios/', views.comentarios,name="Comentarios"),
    path('respuesta_buscar/', views.respuestaBuscar,name="RespuestaBuscar"),
    path('buscar/', views.buscar,name="Buscar"),
]

