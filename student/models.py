from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from home.utils import  get_age
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="studen_user")
    birth_day    =  models.DateField("BirthDay",null=False)
    student_code =  models.CharField(validators=[MinLengthValidator(3)], max_length=40)
    bio          =  models.CharField(max_length=255, blank=True)
    
    def clean(self):
        if get_age(self.birth_day) < 5:
            raise ValidationError("Student should be older than 5 years")
