from rest_framework import serializers, pagination

from .models import Course
from .categories import Category

from applications.teachers.models import Teacher


class CourseSerializer(serializers.ModelSerializer):
    # Get teacher readable name and course category
    teacher = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'image',
            'description',
            'duration',
            'price',
            'language',
            'teacher',
            'category',
            'update_at',
            'average_rating'
        )


class CoursePagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 50
    