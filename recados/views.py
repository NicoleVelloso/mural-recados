from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect

from .models import Recado


def home(request):
    ultimos = Recado.objects.all()[:5]
    return render(request, "recados/home.html", {"ultimos": ultimos})


def mural(request):
    busca = request.GET.get("busca", "").strip()

    recados = Recado.objects.all()
    if busca:
        from django.db.models import Q
        recados = recados.filter(
            Q(mensagem__icontains=busca) | Q(autor__username__icontains=busca)
        )

    contexto = {"recados": recados, "busca": busca}
    return render(request, "recados/mural.html", contexto)


def detalhes_recado(request, id):
    recado = get_object_or_404(Recado, id=id)
    return render(request, "recados/detalhes_recado.html", {"recado": recado})


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
            return redirect("meus_recados")

        contexto = {
            "erro": "Escreva uma mensagem para publicar o recado.",
            "mensagem": mensagem,
        }
        return render(request, "recados/novo_recado.html", contexto)

    return render(request, "recados/novo_recado.html")


@login_required
def editar_recado(request, id):
    recado = get_object_or_404(Recado, id=id, autor=request.user)

    if request.method == "POST":
        mensagem = request.POST.get("mensagem", "").strip()

        if mensagem:
            recado.mensagem = mensagem
            recado.save()
            return redirect("meus_recados")

        contexto = {
            "erro": "Escreva uma mensagem para salvar o recado.",
            "recado": recado,
            "mensagem": mensagem,
        }
        return render(request, "recados/editar_recado.html", contexto)

    return render(request, "recados/editar_recado.html", {"recado": recado})


@login_required
def excluir_recado(request, id):
    recado = get_object_or_404(Recado, id=id, autor=request.user)

    if request.method == "POST":
        recado.delete()
        return redirect("meus_recados")

    return render(request, "recados/excluir_recado.html", {"recado": recado})


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
