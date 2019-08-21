from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Auth User Serializer
    """
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

