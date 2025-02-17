from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .jwt_utils import decode_jwt

from .models import Champion, Tag, ParType, Player, Party
from .serializers import (
    ChampionSerializer,
    TagSerializer,
    ParTypeSerializer,
    PlayerSerializer,
    PartySerializer,
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
    permission_classes_by_action = {"create": [AllowAny]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class PartyViewSet(viewsets.ViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    @action(detail=False, methods=["POST"], permission_classes=[AllowAny])
    def create_party(self, request):
        if "Authorization" not in request.headers:
            return Response({"error": "No token provided"}, status=401)

        token_type, token = request.headers.get("Authorization").split(" ")
        if token_type != "Bearer":
            return Response({"error": "Invalid token type"}, status=401)

        player = Player.objects.filter(jwttoken=token).first()
        if not player:
            return Response({"error": "Invalid token"}, status=401)

        party = Party.objects.create()
        party.players.add(player)
        serializer = PartySerializer(party)
        return Response(serializer.data)

    @action(detail=False, methods=["POST"], permission_classes=[AllowAny])
    def join_party(self, request):
        if "Authorization" not in request.headers:
            return Response({"error": "No token provided"}, status=401)

        token_type, token = request.headers.get("Authorization").split(" ")
        if token_type != "Bearer":
            return Response({"error": "Invalid token type"}, status=401)

        player = Player.objects.filter(jwttoken=token).first()
        if not player:
            return Response({"error": "Invalid token"}, status=401)

        party_id = request.data.get("party_id")
        party = Party.objects.filter(id=party_id).first()
        if not party:
            return Response({"error": "Invalid party id"}, status=400)

        if not party.add_player(player):
            return Response({"error": "Party is full"}, status=400)

        serializer = PartySerializer(party)
        return Response(serializer.data)
