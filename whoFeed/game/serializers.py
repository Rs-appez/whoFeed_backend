from rest_framework import serializers

from .models import Champion, Tag, ParType


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ParTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParType
        fields = "__all__"
