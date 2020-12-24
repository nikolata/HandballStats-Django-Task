from django.db import models

# Create your models here.
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=60)
    wins = models.IntegerField()
    opponents = models.TextField(max_length=256, null=True, blank=True)
    last_match = models.DateTimeField(auto_now=True)
    last_win = models.DateTimeField(auto_now=False, null=True, blank=True)
    added = models.DateTimeField(auto_now=False)
    def __str__(self):
        return self.name
