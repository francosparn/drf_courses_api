from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, filters

from .serializers import CourseSerializer, CoursePagination
from .models import Course
from .permissions import IsAdminOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    # Get all courses
    queryset = Course.objects.all()
    
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [TokenAuthentication]
    
    # Filter courses by name
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    
    # Filter courses by language or category
    filterset_fields = ['language', 'category']