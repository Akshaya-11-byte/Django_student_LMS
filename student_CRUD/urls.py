from django.urls import path

from student_CRUD import views


urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("stu/",views.add_student,name="add_student"),
    path("details/<int:id>/",views.details,name="details"),
    path("delete_student/<int:id>/",views.delete_student,name="delete_student"),
    path("api/students/",views.StudentListCreateAPI.as_view(),name="Student-list-create-API"),
    path("api/students/<int:pk>/",views.StudentRetriveUpdateDestroyAPI.as_view(),name="StudentRetriveUpdateDestroyAPI")
]

    
