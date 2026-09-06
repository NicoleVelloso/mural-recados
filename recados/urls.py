from django.urls import path

from . import views

urlpatterns = [
    path("", views.mural, name="mural"),
    path("meus/", views.meus_recados, name="meus_recados"),
    path("novo/", views.novo_recado, name="novo_recado"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("entrar/", views.entrar, name="entrar"),
    path("sair/", views.sair, name="sair"),
]
