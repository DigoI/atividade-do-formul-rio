from django.db import models

# Create your models here.
class aluno(models.Model):
    nome= models.CharField(max_length=200)
    idade=models.IntegerField()
    data_nascimento= models.DateField()
    email=models.EmailField()
    telefone= models.IntegerField()
    curso=models.CharField(max_length=200)

    def __str__(self):
        return self.nome