from django.contrib import admin
from .models import Course, ClassSection, Enrolled

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'state', 'max_capacity')

@admin.register(ClassSection)
class ClassSectionAdmin(admin.ModelAdmin):
    list_display = ('course', 'teacher')

@admin.register(Enrolled)
class ClassEnrrolled(admin.ModelAdmin):
    pass
