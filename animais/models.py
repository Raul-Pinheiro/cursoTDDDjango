from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Animais(models.Model):
    nome_animal = models.CharField(max_length=20)
    predador = models.CharField(max_length=400, blank=True, null=True)
    venenoso = models.CharField(max_length=40, blank=True, null= True)
    domestico = models.CharField(max_length=40, blank=True, null= True)

    def __str__(self):
        return self.nome_animal