from django.urls import path, include
from rest_framework.routers import SimpleRouter

from kaggleeuropeansoccer.teams import views

router = SimpleRouter()
router.register('team', views.TeamViewSet)
router.register('country', views.CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index', views.index)
]
