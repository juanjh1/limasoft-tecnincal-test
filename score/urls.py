from django.urls import path 
from . import views
urlpatterns = [
    path("scoreboard/<int:id>", views.show_scores, name="show_score")
]
