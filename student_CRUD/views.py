from django.shortcuts import render,redirect,get_object_or_404
from .models import StudentDetail
from .forms import Studentform
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
# Create your views here
def homepage(request):
    student_list= StudentDetail.objects.all()
    context ={
        "students":student_list
    }
    return render(request,"homepage1.html",context)

def add_student(request):
    if request.method=="POST" :
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("homepage")
    form=Studentform
    context={
        "form":form
    }
    return render(request,"add_student.html",context)

def details(request,id):
    if request.method=="POST":
        student=get_object_or_404(StudentDetail,pk=id)
        form=Studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect("homepage")
    student=get_object_or_404(StudentDetail,pk=id)
    form=Studentform(instance=student)
    context={
        "form":form
    }
    return render(request,'view_details.html',context)
def delete_student(request,id):
    student=get_object_or_404(StudentDetail,pk=id)
    student.delete()
    return redirect("homepage")

#Api creation
class StudentListCreateAPI(APIView):
    def get(self, request):
        students = StudentDetail.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class StudentRetriveUpdateDestroyAPI(APIView):
    def patch(self,request,pk):
        student=get_object_or_404(StudentDetail,pk=pk)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        student=get_object_or_404(StudentDetail,pk=pk)
        student.delete()
        return Response({"message":"deleted successfully"},status=status.HTTP_200_OK)