from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
# Create your models here.


class Course(models.Model):
    class Status(models.TextChoices):
        DRAFT    = "DF", "DRAFT"
        ACTIVE   = "AC", "ACTIVE"
        INACTIVE = "IN", "INACTIVE"

    name         = models.CharField(max)
    max_capacity = models.IntegerField(validators=[MinValueValidator(1)]) 
    code         = models.CharField()
    state        = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)


