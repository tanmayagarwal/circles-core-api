from django.contrib.auth.models import User, Group

from rest_framework import serializers

# models
from .models import (
    HikayaUser, Workspace, AccountType, AccountSubType,
    Location, Contact, Document, Office, Currency, LocationType,
    FundingStatus, WorkflowStatus, WorkflowLevel1Type, WorkflowLevel2Type,
    WorkflowLevel1, WorkflowLevel2, WorkflowLevel2Plan, Account,
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
    # """
    url = serializers.HyperlinkedIdentityField(
        view_name='workspace-detail',
        lookup_field='uuid'
    )

    class Meta:
        model = Workspace
        exclude = (
            'create_date', 'modified_date', 'created_by', 'modified_by'
        )
        extra_kwargs = {'url': {'lookup_field': 'uuid'}}


class HikayaUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    HikayaUser Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid'
    )

    workspaces = serializers.HyperlinkedRelatedField(
        view_name='workspace-detail',
        lookup_field='uuid',
        queryset=Workspace.objects.all(),
    )

    workspaces = serializers.HyperlinkedRelatedField(
        view_name='workspace-detail',
        lookup_field='uuid',
        queryset=Workspace.objects.all(),
        many=True,
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

    workspace = serializers.HyperlinkedRelatedField(
        view_name='workspace-detail',
        lookup_field='uuid',
        queryset=Workspace.objects.all(),
        required=False,
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

    workspace = serializers.HyperlinkedRelatedField(
        view_name='workspace-detail',
        lookup_field='uuid',
        queryset=Workspace.objects.all(),
        required=False,
    )

    account_type = serializers.HyperlinkedRelatedField(
        view_name='accounttype-detail',
        lookup_field='type_uuid',
        queryset=AccountType.objects.all(),
        required=False,
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = AccountSubType
        fields = '__all__'
        extra_fields = ('id',)


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    """
    Account Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='account-detail',
        lookup_field='account_uuid'
    )

    account_type = serializers.HyperlinkedRelatedField(
        view_name='accounttype-detail',
        lookup_field='type_uuid',
        queryset=AccountType.objects.all(),
        required=False,
    )

    account_sub_type = serializers.HyperlinkedRelatedField(
        view_name='accountsubtype-detail',
        lookup_field='sub_type_uuid',
        queryset=AccountSubType.objects.all(),
        required=False,
    )

    workspace = serializers.HyperlinkedRelatedField(
        view_name='workspace-detail',
        lookup_field='uuid',
        queryset=Workspace.objects.all(),
        required=False,
    )

    parent_account = serializers.HyperlinkedRelatedField(
        view_name='account-detail',
        lookup_field='account_uuid',
        queryset=Account.objects.all(),
        required=False,
    )

    documentation = serializers.HyperlinkedRelatedField(
        view_name='document-detail',
        lookup_field='document_uuid',
        queryset=Document.objects.all(),
        required=False,
    )

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = Account
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

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
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

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
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


class LocationTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    LocationType Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='locationtype-detail',
        lookup_field='location_type_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = LocationType
        fields = '__all__'
        extra_fields = ('id',)


class FundingStatusSerializer(serializers.HyperlinkedModelSerializer):
    """
    FundingStatus Serializer
    """
    url = serializers.HyperlinkedIdentityField(

        view_name='fundingstatus-detail',
        lookup_field='funding_status_uuid'
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = FundingStatus
        fields = '__all__'
        extra_fields = ('id',)


class WorkflowStatusSerializer(serializers.HyperlinkedModelSerializer):
    """
    WorkflowStatus Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workflowstatus-detail',
        lookup_field='status_uuid'
    )

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkflowStatus
        fields = '__all__'
        extra_fields = ('id',)


class WorkflowLevel1TypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    WorkflowLevel1Type Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workflowlevel1type-detail',
        lookup_field='type_uuid')

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkflowLevel1Type
        fields = '__all__'
        extra_fields = ('id',)


class WorkflowLevel2TypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    WorkflowLevel2Type Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workflowlevel2type-detail',
        lookup_field='type_uuid')

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkflowLevel2Type
        fields = '__all__'
        extra_fields = ('id',)


class WorkflowLevel1Serializer(serializers.HyperlinkedModelSerializer):
    """
    WorkflowLevel1 Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workflowlevel1-detail',
        lookup_field='workflow_level1_uuid')

    workspace = serializers.HyperlinkedRelatedField(
        view_name='workspace-detail',
        lookup_field='uuid',
        queryset=Workspace.objects.all()
    )

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkflowLevel1
        fields = '__all__'
        extra_fields = ('id',)


class WorkflowLevel2Serializer(serializers.HyperlinkedModelSerializer):
    """
    WorkflowLevel2 Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workflowlevel2-detail',
        lookup_field='workflow_level2_uuid'
    )
    workflow_level1 = serializers.HyperlinkedRelatedField(
        view_name='workflowlevel1-detail',
        lookup_field='workflow_level1_uuid',
        queryset=WorkflowLevel1.objects.all()
    )

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkflowLevel2
        fields = '__all__'
        extra_fields = ('id',)


class WorkflowLevel2PlanSerializer(serializers.HyperlinkedModelSerializer):
    """
    WorkflowLevel2Plan Serializer
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='workflowlevel2plan-detail',
        lookup_field='workflow_level2_plan_uuid'
    )

    workflow_level1 = serializers.HyperlinkedRelatedField(
        view_name='workflowlevel1-detail',
        lookup_field='workflow_level1_uuid',
        queryset=WorkflowLevel1.objects.all(),
    )

    workflow_level2 = serializers.HyperlinkedRelatedField(
        view_name='workflowlevel2-detail',
        lookup_field='workflow_level2_uuid',
        queryset=WorkflowLevel2.objects.all(),
    )

    created_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    modified_by = serializers.HyperlinkedRelatedField(
        view_name='hikayauser-detail',
        lookup_field='hikaya_user_uuid',
        read_only=True
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkflowLevel2Plan
        fields = '__all__'
        extra_fields = ('id',)
