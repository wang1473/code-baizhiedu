from django.urls import path

from course import views

urlpatterns = [
    path("category/", views.CourseCategoryAPIView.as_view()),
    path("courses/", views.CourseAPIView.as_view()),
    path("lession/<int:pk>/", views.LessionAPIView.as_view()),
]