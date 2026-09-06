from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from .models import Recado


def mural(request):
    recados = Recado.objects.all()
    return render(request, "recados/mural.html", {"recados": recados})


@login_required
def meus_recados(request):
    recados = Recado.objects.filter(autor=request.user)
    return render(request, "recados/meus_recados.html", {"recados": recados})


@login_required
def novo_recado(request):
    if request.method == "POST":
        mensagem = request.POST.get("mensagem", "").strip()

        if mensagem:
            Recado.objects.create(autor=request.user, mensagem=mensagem)
            return redirect("mural")

        contexto = {
            "erro": "Escreva uma mensagem para publicar o recado.",
            "mensagem": mensagem,
        }
        return render(request, "recados/novo_recado.html", contexto)

    return render(request, "recados/novo_recado.html")


def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("mural")
    else:
        form = UserCreationForm()

    return render(request, "recados/cadastro.html", {"form": form})


def entrar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("mural")
    else:
        form = AuthenticationForm()

    return render(request, "recados/login.html", {"form": form})


def sair(request):
    logout(request)
    return redirect("mural")
