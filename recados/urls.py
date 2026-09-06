from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mural/", views.mural, name="mural"),
    path("recados/<int:id>/", views.detalhes_recado, name="detalhes_recado"),
    path("meus/", views.meus_recados, name="meus_recados"),
    path("novo/", views.novo_recado, name="novo_recado"),
    path("editar/<int:id>/", views.editar_recado, name="editar_recado"),
    path("excluir/<int:id>/", views.excluir_recado, name="excluir_recado"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("entrar/", views.entrar, name="entrar"),
    path("sair/", views.sair, name="sair"),
]
