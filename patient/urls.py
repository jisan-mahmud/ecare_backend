from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('profile/', views.PatientViewset.as_view()),
    path('register/', views.PatientRegisterAPIView.as_view(), name='register'),
    path('activate/<uid>/<token>/', views.active, name='activate'),
    path('login/', views.UserLoginAPIView.as_view(), name= 'user_login'),
    path('logout/', views.LogoutAPIView.as_view(), name= 'user_logout')
]
