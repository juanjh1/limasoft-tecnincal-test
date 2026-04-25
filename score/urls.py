from django.urls import path 
from . import views
urlpatterns = [
    path("scoreboard/<int:id>", views.show_scores, name="show_score"),
    path("add/", views.add_score, name="add_score"),
    path("bulk-update/", views.bulk_update_scores, name="bulk_update_scores"),
]
