from rest_framework import viewsets

from .models import Champion, Tag, ParType
from .serializers import ChampionSerializer, TagSerializer, ParTypeSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ParTypeViewSet(viewsets.ModelViewSet):
    queryset = ParType.objects.all()
    serializer_class = ParTypeSerializer
