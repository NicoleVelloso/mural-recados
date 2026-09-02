from django.db import models


class Recado(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.nome}: {self.mensagem[:30]}"
