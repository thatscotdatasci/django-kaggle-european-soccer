from django.http import HttpResponse
from rest_framework import viewsets

from kaggleeuropeansoccer.teams import models, serializers


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the teams index.")
