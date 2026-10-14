# Create your models here.
from django.db import models

# Modelo que representa um comentário simples
class Comentario(models.Model):
    # Nome do autor do comentário (campo de texto curto)
    autor = models.CharField(max_length=100)

    # Conteúdo do comentário (texto livre)
    texto = models.TextField() 

    data_criacao = models.DateTimeField(auto_now_add=True) # data/hora de criação preenchida automaticamente
    def __str__(self):
        # Representação legível do objeto: "Autor: texto..." (mostra os primeiros 30 caracteres)
        return f"{self.autor}: {self.texto[:30]}" # [:30] limita a exibição para não mostrar o comentário completo