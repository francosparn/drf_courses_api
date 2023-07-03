from rest_framework import generics, permissions, authentication
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .serializers import TeacherSerializer, TeacherPagination
from .models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    # Get all teachers
    queryset = Teacher.objects.all()
    
    serializer_class = TeacherSerializer
    
    # To access this class it is necessary to be authenticated and have a token
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    pagination_class = TeacherPagination
    
    # Returns the objects that have the same email as the user making the request
    def get_queryset(self):
        return Teacher.objects.filter(email=self.request.user.email)

    # Obtains the student object to be modified and verifies that it has the necessary permissions to perform said action
    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj