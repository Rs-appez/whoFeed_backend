from django.db import models

from cryptography.hazmat.primitives import serialization
import jwt
import uuid
from django.conf import settings


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


class Player(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    jwttoken = models.CharField(max_length=100, editable=False)
    last_game = models.DateTimeField(auto_now=True)

    champion = models.ForeignKey(
        "Champion", on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.make_jwt()
        super().save(*args, **kwargs)

    def make_jwt(self):
        private_key = serialization.load_ssh_private_key(
            settings.SECRET_JWT_KEY.encode(), password=b""
        )
        self.jwttoken = jwt.encode(
            {"id": str(self.id), "name": self.name},
            private_key,
            algorithm="RS256",
        )
