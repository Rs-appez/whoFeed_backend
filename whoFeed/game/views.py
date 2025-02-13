from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .jwt_utils import decode_jwt

from .models import Champion, Tag, ParType, Player
from .serializers import (
    ChampionSerializer,
    TagSerializer,
    ParTypeSerializer,
    PlayerSerializer,
)


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

    @action(detail=False, permission_classes=[AllowAny])
    def get_champions(self, request):
        if "Authorization" not in request.headers:
            return Response({"error": "No token provided"}, status=401)

        token_type, token = request.headers.get("Authorization").split(" ")
        if token_type != "Bearer":
            return Response({"error": "Invalid token type"}, status=401)

        player = Player.objects.filter(jwttoken=token).first()
        if not player:
            return Response({"error": "Invalid token"}, status=401)

        queryset = Champion.objects.all().order_by("?")[:50]
        serializer = ChampionSerializer(queryset, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ParTypeViewSet(viewsets.ModelViewSet):
    queryset = ParType.objects.all()
    serializer_class = ParTypeSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
