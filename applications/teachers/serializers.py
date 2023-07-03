from rest_framework import serializers, pagination

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Teacher
        fields = (
            'id',
            'name',
            'lastname',
            'email',
            'gender'
        )


class TeacherPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 50