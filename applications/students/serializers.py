from rest_framework import serializers, pagination

from .models import Student

from applications.courses.serializers import CourseSerializer


class StudentSerializer(serializers.ModelSerializer):
    # Get course name instead of id
    courses = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Student
        fields = (
            'id',
            'name',
            'lastname',
            'email',
            'gender',
            'courses'
        )

class StudentPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100

