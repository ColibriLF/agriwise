from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Parcela(models.Model):
    nome = models.CharField(max_length=100)
    area = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parcelas')

    def __str__(self):
        return f'{self.nome}'


class Registo(models.Model):
    data = models.DateField(auto_now_add=True)
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE, related_name='parcelas')
    produto = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.data} {self.parcela} {self.produto} {self.dose}'