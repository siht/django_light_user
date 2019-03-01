from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
__all__ = ('UserViewSet',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
