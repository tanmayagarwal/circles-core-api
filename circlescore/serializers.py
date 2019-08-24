from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Auth User Serializer
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Group Serializer
    """
    class Meta:
        model = Group
        fields = '__all__'


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Workspace Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workspace-detail',
        lookup_field='uuid'
    )

    class Meta:
        model = Workspace
        exclude = ('create_date', 'modified_date', 'created_by', 'modified_by')


class HikayaUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    HikayaUser Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid'
    )
    id = serializers.ReadOnlyField()
    user_object = serializers.SerializerMethodField()
    class Meta:
        model = HikayaUser
        fields = '__all__'
        extra_fields = ('id',)

    def get_user_object(self, obj):
        return UserSerializer(User.objects.get(pk=obj.user.id)).data