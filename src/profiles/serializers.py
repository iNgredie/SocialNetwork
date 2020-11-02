from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """ Вывод инфо о user
    """
    class Meta:
        model = UserNet
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_stuff',
            'is_superuser',
            'groups',
            'user_permissions'
         )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной инфы о user
    """
    class Meta:
        model = UserNet
        exclude = (
            'email',
            'password',
            'phone'
            'last_login',
            'is_active',
            'is_stuff',
            'is_superuser',
            'groups',
            'user_permissions'
         )
