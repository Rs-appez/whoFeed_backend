from django.urls import path, include

from rest_framework import routers

from .views import ChampionViewSet, TagViewSet, ParTypeViewSet

router = routers.DefaultRouter()

router.register("champions", ChampionViewSet)
router.register("tags", TagViewSet)
router.register("partypes", ParTypeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
