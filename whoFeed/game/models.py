from django.db import models


class Champion(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    fr_name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    sprite = models.CharField(max_length=100)
    lore = models.TextField()
    fr_lore = models.TextField()
    tags = models.ManyToManyField("Tag")
    par_types = models.ManyToManyField("ParType")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    fr_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ParType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    fr_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
