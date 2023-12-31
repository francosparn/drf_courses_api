from django.urls import path, include
from rest_framework import routers

from .views import TeacherViewSet


router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
 