from django.contrib import admin
from .models import Course, ClasssSection, Enrolled

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass 

@admin.register(ClasssSection)
class ClasssSection(admin.ModelAdmin):
    pass

@admin.register(Enrolled)
class ClassEnrrolled(admin.ModelAdmin):
    pass
