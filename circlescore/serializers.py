from django.contrib.auth.models import User, Group

from rest_framework import serializers

# models
from .models import (
    HikayaUser, Workspace, AccountType, AccountSubType,
    Location, Contact, Document, Office, Currency
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Auth User Serializer
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')
        write_only_fields = ('password',)
        read_only_fields = (
            'is_staff', 'is_superuser', 'is_active', 'date_joined',
        )

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


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Document Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='document-detail',
        lookup_field='document_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = Document
        fields = '__all__'
        extra_fields = ('id',)


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
        exclude = (
            'create_date', 'modified_date', 'created_by', 'modified_by'
        )


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
        return UserSerializer(
            User.objects.get(pk=obj.user.id)
        ).data


class AccountTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    AccountType Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='accounttype-detail',
        lookup_field='type_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = AccountType
        fields = '__all__'
        extra_fields = ('id',)


class AccountSubTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    AccountSubType Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='accountsubtype-detail',
        lookup_field='sub_type_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = AccountSubType
        fields = '__all__'
        extra_fields = ('id',)


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    """
    Contact Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='contact-detail',
        lookup_field='contact_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = Contact
        fields = '__all__'
        extra_fields = ('id',)


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Location Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='location-detail',
        lookup_field='location_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = Location
        fields = '__all__'
        extra_fields = ('id',)


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Office Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='office-detail',
        lookup_field='office_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = Office
        fields = '__all__'
        extra_fields = ('id',)


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    """
    Currency Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='currency-detail',
        lookup_field='currency_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = Currency
        fields = '__all__'
        extra_fields = ('id',)
