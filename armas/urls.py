from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('arma/crear/', views.añadir_arma, name='añadir_arma'),
    path('arma/<int:pk>/editar/', views.editar_arma, name='editar_arma'),
    path('arma/<int:pk>/eliminar/', views.eliminar_arma, name='eliminar_arma'),
]