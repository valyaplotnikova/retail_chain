from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Пользователь. """

    class Meta:
        model = User
        fields = ['email', 'is_active',]
