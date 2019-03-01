from rest_framework import serializers
from .models import User
__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('last_login', 'date_joined')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
