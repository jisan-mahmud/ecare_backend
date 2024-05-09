from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'list', views.PatientViewset, basename= 'patent_list')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.PatientRegisterAPIView.as_view(), name='register'),
    path('activate/<uid>/<token>/', views.active, name='activate')
]
