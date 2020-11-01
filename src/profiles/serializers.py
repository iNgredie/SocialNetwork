from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """ Вывод инфо о user
    """
    class Meta:
        model = UserNet
        exclude = (
            'password', 'last_login', 'is_active', 'is_stuff', 'is_superuser'
         )