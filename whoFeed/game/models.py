from django.db import models

from shortuuid.django_fields import ShortUUIDField

import bleach
import uuid

from .jwt_utils import make_jwt


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
        self.name = bleach.clean(self.name)
        self.jwttoken = make_jwt({"id": str(self.id), "name": self.name})
        super().save(*args, **kwargs)


class Party(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False,
                        max_length=8, length=8)
    players = models.ManyToManyField("Player", max_length=2)

    def save(self, *args, **kwargs):
        if (
            self._state.adding
        ):  # Check if the object is being created for the first time
            super().save(*args, **kwargs)
            self.id = (self.id[:4] + "-" + self.id[4:]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id

    def add_player(self, player):
        if self.players.count() == 2:
            return False
        self.players.add(player)
        self.save()
        return True
