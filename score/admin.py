from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('enrolled', 'value', 'updated_at')
    list_editable = ('value',)
