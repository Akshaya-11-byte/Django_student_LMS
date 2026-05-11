from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    student_Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique=True)
    course=models.CharField(max_length=70)
    enrollement_date=models.DateField()

    def  __str__(self):
        return self.student_Name