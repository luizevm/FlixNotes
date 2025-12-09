from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gênero")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


class Plataforma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Plataforma de streaming")
    site = models.CharField(max_length=150, verbose_name="Site da plataforma", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"


class Obra(models.Model):
    TIPOS = (
        ("FILME", "Filme"),
        ("SERIE", "Série"),
    )

    STATUS = (
        ("ASSISTIDO", "Assistido"),
        ("VER", "Quero ver"),
    )

    titulo = models.CharField(max_length=150, verbose_name="Título")
    tipo = models.CharField(max_length=10, choices=TIPOS, verbose_name="Tipo")
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, verbose_name="Gênero")
    plataforma = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True, verbose_name="Plataforma")
    status = models.CharField(max_length=10, choices=STATUS, verbose_name="Status")
    nota = models.IntegerField(null=True, blank=True, verbose_name="Nota (0–10)")
    comentario = models.TextField(blank=True, verbose_name="Comentário")
    data_registro = models.DateField(auto_now_add=True, verbose_name="Data de registro")
    data_atualizacao = models.DateField(auto_now=True, verbose_name="Última atualização")

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
        ordering = ["titulo"]
