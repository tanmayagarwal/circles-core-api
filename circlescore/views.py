from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group, User

from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from rest_framework.decorators import (
    api_view, permission_classes,
)
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

# serializers
from .serializers import (
    UserSerializer, AccountSubTypeSerializer, AccountTypeSerializer,
    GroupSerializer, LocationSerializer, HikayaUserSerializer,
    ContactSerializer, WorkspaceSerializer, DocumentSerializer,
    OfficeSerializer, CurrencySerializer, LocationTypeSerializer,
    FundingStatusSerializer, WorkflowStatusSerializer,
    WorkflowLevel1TypeSerializer, WorkflowLevel2TypeSerializer,
    WorkflowLevel1Serializer, WorkflowLevel2Serializer,
)

# models
from .models import (
    HikayaUser, Workspace, AccountType, AccountSubType,
    Location, Contact, Document, Office, Currency, LocationType,
    FundingStatus, WorkflowStatus, WorkflowLevel1Type, WorkflowLevel2Type,
    WorkflowLevel1, WorkflowLevel2,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    Auth User view set (Uses django core User model)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User
    http_method_names = ['put', 'patch', 'post', 'get']

    class Meta:
        depth = 1

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        if self.request.method == 'PUT' or \
                self.request.method == 'PATCH' or\
                self.request.method == 'GET':
            self.permission_classes = (IsAuthenticated,)

        return super(UserViewSet, self).get_permissions()


class GroupViewSet(viewsets.ModelViewSet):
    """
    Group view set
    User django core Group model
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    model = Group
    permission_classes = (IsAuthenticated,)


@api_view(['POST'])
@permission_classes((AllowAny,))
def auth_login(request):
    """
    User login view
    :param request:
    :return: user payload on success and error on fail
    """
    try:
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = User.objects.get(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        )

        if user.check_password(password):
            try:
                refresh = RefreshToken.for_user(user)
                jwt_payload = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }

                user_object = model_to_dict(
                    User.objects.filter(pk=user.id).first()
                )
                # remove password field
                del user_object['password']
                hikaya_user_object = model_to_dict(
                    HikayaUser.objects.get(user_id=user.id))

                response_payload = {
                    'token': jwt_payload,
                    'user': user_object,
                    'hikaya_user': hikaya_user_object
                }

                return Response(
                    response_payload,
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                raise e

    except User.DoesNotExist:
        res = {
            'error': 'User does not exist. '
                     'Please confirm the details and retry'
        }
        return Response(res, status=status.HTTP_403_FORBIDDEN)

    except KeyError:
        res = {
            'error': 'Please provide both username and password'
        }
        return Response(res, status=status.HTTP_403_FORBIDDEN)

    error_message = 'An error occurred. ' \
                    'Please verify details and try again'
    return Response(
        {'error': error_message},
        status=status.HTTP_403_FORBIDDEN
    )


class DocumentViewSet(viewsets.ModelViewSet):
    """
    Document View
    """
    model = Document
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Document.objects.all()
    lookup_field = 'document_uuid'


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    Workspace View
    """
    model = Workspace
    serializer_class = WorkspaceSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Workspace.objects.all()
    lookup_field = 'uuid'


class HikayaUserViewSet(viewsets.ModelViewSet):
    """
    HikayaUser View
    """
    model = HikayaUser
    serializer_class = HikayaUserSerializer
    http_method_names = ('get', 'put', 'patch')
    queryset = HikayaUser.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'hikaya_user_uuid'


class AccountTypeViewSet(viewsets.ModelViewSet):
    """
    AccountType View
    """
    model = AccountType
    serializer_class = AccountTypeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = AccountType.objects.all()
    lookup_field = 'type_uuid'


class AccountSubTypeViewSet(viewsets.ModelViewSet):
    """
    AccountType View
    """
    model = AccountSubType
    serializer_class = AccountSubTypeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = AccountSubType.objects.all()
    lookup_field = 'sub_type_uuid'


class ContactViewSet(viewsets.ModelViewSet):
    """
    Contact View
    """
    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    lookup_field = 'contact_uuid'


class LocationViewSet(viewsets.ModelViewSet):
    """
    Location View
    """
    model = Location
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Location.objects.all()
    lookup_field = 'location_uuid'


class OfficeViewSet(viewsets.ModelViewSet):
    """
    Office ViewSet
    """
    model = Office
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Office.objects.all()
    lookup_field = 'office_uuid'


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    Currency ViewSet
    """
    model = Currency
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    lookup_field = 'currency_uuid'


class LocationTypeViewSet(viewsets.ModelViewSet):
    """
    LocationType ViewSet
    """
    model = LocationType
    serializer_class = LocationTypeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = LocationType.objects.all()
    lookup_field = 'location_type_uuid'


class FundingStatusViewSet(viewsets.ModelViewSet):
    """
    FundingStatus ViewSet
    """
    model = FundingStatus
    serializer_class = FundingStatusSerializer
    permission_classes = (IsAuthenticated,)
    queryset = FundingStatus.objects.all()
    lookup_field = 'funding_status_uuid'


class WorkflowStatusViewSet(viewsets.ModelViewSet):
    """
    WorkflowStatus ViewSet
    """
    model = WorkflowStatus
    serializer_class = WorkflowStatusSerializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkflowStatus.objects.all()
    lookup_field = 'status_uuid'


class WorkflowLevel1TypeViewSet(viewsets.ModelViewSet):
    """
    WorkflowLevel1Type ViewSet
    """
    model = WorkflowLevel1Type
    serializer_class = WorkflowLevel1TypeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkflowLevel1Type.objects.all()
    lookup_field = 'type_uuid'


class WorkflowLevel2TypeViewSet(viewsets.ModelViewSet):
    """
    WorkflowLevel2Type ViewSet
    """
    model = WorkflowLevel2Type
    serializer_class = WorkflowLevel2TypeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkflowLevel2Type.objects.all()
    lookup_field = 'type_uuid'


class WorkflowLevel1ViewSet(viewsets.ModelViewSet):
    """
    WorkflowLevel1 ViewSet
    """
    model = WorkflowLevel1
    serializer_class = WorkflowLevel1Serializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkflowLevel1.objects.all()
    lookup_field = 'workflow_level1_uuid'


class WorkflowLevel2ViewSet(viewsets.ModelViewSet):
    """
    WorkflowLevel2 ViewSet
    """
    model = WorkflowLevel2
    serializer_class = WorkflowLevel2Serializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkflowLevel2.objects.all()
    lookup_field = 'workflow_level2_uuid'
