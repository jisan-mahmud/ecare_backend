from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorViewset,
    DesignationViewset,
    SpecializationViewset,
    AvailableTimeViewset,
    ReviewViewset
)

router = DefaultRouter()
router.register(r'list', DoctorViewset)
router.register(r'designation', DesignationViewset)
router.register(r'specialization', SpecializationViewset)
router.register(r'availabletime', AvailableTimeViewset)
router.register(r'review', ReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]
