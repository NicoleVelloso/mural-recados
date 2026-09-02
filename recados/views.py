from django.shortcuts import render, redirect

from .models import Recado


def mural(request):
    recados = Recado.objects.all()
    return render(request, "recados/mural.html", {"recados": recados})


def novo_recado(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        mensagem = request.POST.get("mensagem", "").strip()

        if nome and mensagem:
            Recado.objects.create(nome=nome, mensagem=mensagem)
            return redirect("mural")

        contexto = {
            "erro": "Preencha nome e mensagem para publicar o recado.",
            "nome": nome,
            "mensagem": mensagem,
        }
        return render(request, "recados/novo_recado.html", contexto)

    return render(request, "recados/novo_recado.html")
