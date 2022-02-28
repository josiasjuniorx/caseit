from django.db import models

class Racas(models.Model):
    id = models.CharField(max_length=256, primary_key=True)
    nome = models.CharField(max_length=256)
    origem = models.CharField(max_length=256)
    temperamento = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)

    def __str__(self):
        return self.id

class BreedUrls(models.Model):
    breedid = models.CharField(max_length=256, primary_key=True)
    url0 = models.JSONField(max_length=256)
    url1 = models.URLField(max_length=256)
    url2 = models.URLField(max_length=256)

class CategoryUrls(models.Model):
    categoryid = models.CharField(max_length=256, primary_key=True)
    categoryname = models.CharField(max_length=256)
    url0 = models.URLField(max_length=256)
    url1 = models.URLField(max_length=256)
    url2 = models.URLField(max_length=256)
