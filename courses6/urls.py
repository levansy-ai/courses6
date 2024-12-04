from django.urls import path
from .import views

urlpatterns = [
    path('', views.courses_list, name="course_list"),
    path('course6/<int:course_id>/', views.course_detail, name="course_detail")
]
