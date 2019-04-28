from django.http import HttpResponse
from rest_framework import viewsets, serializers

from kaggleeuropeansoccer.teams import models


class Test(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.models


def index(request):
    return HttpResponse("Hello, world. You're at the teams index.")
