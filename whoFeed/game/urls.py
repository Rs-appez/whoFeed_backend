from django.urls import path, include

from rest_framework import routers

from .views import (
    ChampionViewSet,
    TagViewSet,
    ParTypeViewSet,
    PlayerViewSet,
    PartyViewSet,
)

router = routers.DefaultRouter()

router.register("champions", ChampionViewSet)
router.register("tags", TagViewSet)
router.register("partypes", ParTypeViewSet)
router.register("players", PlayerViewSet)
router.register("parties", PartyViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
