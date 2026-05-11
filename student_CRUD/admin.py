from django.contrib import admin
from .models import StudentDetail

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_Name","email","course","enrollement_date")
    search_fields=("student_Name","email","course","enrollement_date")
    list_filter=("course",)
admin.site.register(StudentDetail,StudentAdmin)