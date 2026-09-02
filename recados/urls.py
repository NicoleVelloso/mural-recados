from django.urls import path

from . import views

urlpatterns = [
    path("", views.mural, name="mural"),
    path("novo/", views.novo_recado, name="novo_recado"),
]
