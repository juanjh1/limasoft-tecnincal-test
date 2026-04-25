from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user             =  models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_user")
    birth_day        =  models.DateField("BirthDay",null=False)
    teacher_code     =  models.CharField(validators=[MinLengthValidator(3)], max_length=40)
    experience_years =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(40)]) 
    bio              =  models.CharField(max_length=255, blank=True)

