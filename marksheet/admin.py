from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'class_name')
    search_fields = ('name', 'roll_no')
    list_filter = ('class_name',)

admin.site.register(Student, StudentAdmin)
