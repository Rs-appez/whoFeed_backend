from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Champion, Tag, ParType
from .serializers import ChampionSerializer, TagSerializer, ParTypeSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

    @action(detail=False)
    def get_champions(self, request):
        queryset = Champion.objects.all().order_by("?")[:50]
        serializer = ChampionSerializer(queryset, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ParTypeViewSet(viewsets.ModelViewSet):
    queryset = ParType.objects.all()
    serializer_class = ParTypeSerializer
