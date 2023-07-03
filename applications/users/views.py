from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserSerializer, AuthTokenSerializer
from .models import User

from applications.students.permissions import IsOwnerOrReadOnly
from applications.teachers.permissions import IsOwnerOrReadOnly


# Create users
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

# Update user
class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_object(self):
        return self.request.user # Busca el objeto con el PK indicado
    

# Create authentication token
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    
    

