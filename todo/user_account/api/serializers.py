from rest_framework import serializers
from ..models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
