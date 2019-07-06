from django.db import models

# Create your models here.
class Empresa(models.Model):

    nome = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=13)
    email = models.EmailField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=200)

def __str__(self):
        return self.nome




