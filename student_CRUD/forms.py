from django import forms
from .models import StudentDetail

class Studentform(forms.ModelForm):
    class Meta:
        model=StudentDetail
        fields=["student_Name","email","course","enrollement_date"]

