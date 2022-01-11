from django.db import models

class Paises(models.Model):
    nome_ingles = models.CharField("nome_ingles", max_length=50)
    nome_portugues = models.CharField("nome_portugues", max_length=50)
    bandeira_url = models.CharField("bandeira_url", max_length=40)
