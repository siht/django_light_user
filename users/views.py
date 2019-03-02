from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import (
    UserCreationSerializer,
    UserEditionSerializer,
    UserEditPasswordSerializer,
)
from .models import User
__all__ = ('UserViewSet',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return UserEditionSerializer
        return UserCreationSerializer

    @action(detail=True, methods=['patch'])
    def set_password(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserEditPasswordSerializer(
            user, data=request.data, context={'pk': pk}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'password set'})
