from django.urls import path
from student import views

urlpatterns = [
    path("student/add", views.StudentCreateView.as_view(), name="student-create"),
    path("student/list", views.StudentListView.as_view(),name="list"),
    path("student/index", views.IndexView.as_view(), name="home"),
    path("student/<int:id>", views.StudentDetailView.as_view(), name="detail-student"),
    path("student/<int:id>/remove", views.StudentDelete.as_view(), name="remove"),

]
