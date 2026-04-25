from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_student, name="login-student")
]
