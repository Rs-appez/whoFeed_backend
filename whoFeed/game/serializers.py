from rest_framework import serializers

from .models import Champion, Tag, ParType, Player


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ParTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParType
        fields = "__all__"


class ChampionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    par_type = ParTypeSerializer()

    class Meta:
        model = Champion
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
