import uuid

from django.db import models


class Country(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=30)
    founded_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
