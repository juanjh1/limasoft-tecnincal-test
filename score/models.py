from django.db import models

class Score(models.Model):
    score       = models.IntegerField()
    name        = models.CharField(validators=[])
    created_at  = models.IntegerField()
    updated_at  = models.IntegerField()

