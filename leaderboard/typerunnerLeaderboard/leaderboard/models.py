from django.db import models

# Create your models here.

class Scoreboard(models.model):
    username = models.CharField(max_length=10)
    score    = models.BigIntegerField(
        verbose_name="score"
    )
