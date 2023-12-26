from django.db import models

# Create your models here.
class Word(models.Model):
    word1 = models.CharField(max_length=100)
    word2 = models.CharField(max_length=100)
