from django.conf import settings
from django.db import models


class Recado(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recados",
    )
    mensagem = models.TextField()
    # Imagem opcional. Com o storage do Cloudinary configurado no settings,
    # o arquivo enviado para este campo é gravado no Cloudinary
    # automaticamente, e recado.imagem.url devolve a URL da nuvem.
    # blank/null = True -> recados sem imagem continuam válidos.
    imagem = models.ImageField(upload_to="recados/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.autor.username}: {self.mensagem[:30]}"
