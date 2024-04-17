from django.db import models
from datetime import date

# Create your models here.  

class Pessoa(models.Model):
    """ class Pessoa
    -
    Fields
    - `nome` = String
    - `email` = String
    - `data` = Date
    - `pais` = String
    """
    
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    data = models.DateField(default=date.today)
    pais = models.CharField(default="",max_length=50)