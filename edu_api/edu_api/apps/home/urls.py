from django.urls import path
from home import views

urlpatterns = [
    path('banners/', views.BannerAPIView.as_view()),
    path('navs/', views.NavAPIView.as_view()),
    path('navss/', views.NavvAPIView.as_view()),
]
