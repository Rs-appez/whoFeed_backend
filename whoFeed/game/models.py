from django.db import models


class Champion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    fr_name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    sprite = models.CharField(max_length=100)
    lore = models.TextField()
    fr_lore = models.TextField()
    title = models.CharField(max_length=100)
    fr_title = models.CharField(max_length=100)
    tags = models.ManyToManyField("Tag")
    par_type = models.ForeignKey("ParType", on_delete=models.CASCADE)

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
