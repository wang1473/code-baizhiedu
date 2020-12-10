from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns = [
    path("login/", obtain_jwt_token),
    path("captcha/", views.CaptchaAPIView.as_view()),
    path("register/", views.UserAPIView.as_view()),
    path("phone/", views.Phone.as_view({'post': 'phone'})),
    path("phone_code/", views.Phonee.as_view({'post': 'phone_code'})),
    path("phone_login/", views.PhoneAPIView.as_view({'post': 'phone_login'})),
    path('message/', views.SendMessageAPIView.as_view()),
]
