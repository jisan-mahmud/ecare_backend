from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AppointmentAPIView.as_view(), name='appointment'),
]
