from django.contrib import admin
from .models import Student, StudentProfile
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
   list_display = ('student',)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','email','course')
    search_fields=('name','email')
    list_filter=('course',)
