from django.db.models import Q
from django.forms.models import model_to_dict

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *
from .models import *


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
    if request.method == 'POST':
        try:
            username = request.data.get('username', '')
            password = request.data.get('password', '')

            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))

            if user.check_password(password):
                try:
                    refresh = RefreshToken.for_user(user)
                    jwt_payload = {
                        'refresh_token': str(refresh),
                        'access_token': str(refresh.access_token)
                    }

                    user_object = model_to_dict(User.objects.filter(pk=user.id).defer('password').first())
                    hikaya_user_object = model_to_dict(HikayaUser.objects.get(user_id=user.id))

                    response_payload = {
                        'token': jwt_payload,
                        'user': user_object,
                        'hikaya_user': hikaya_user_object
                    }

                    return Response(response_payload, status=status.HTTP_200_OK)
                except Exception as e:
                    raise e

        except User.DoesNotExist:
            res = {
                'error': 'User does not exist. Please confirm the details and retry'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)

    error_message = '{} method not allowed'.format(request.method)
    return Response({'error': error_message}, status=status.HTTP_403_FORBIDDEN)


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    Workspace View
    """
    model = Workspace
    serializer_class = WorkspaceSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Workspace.objects.all()
    lookup_field = 'uuid'

    class Meta:
        depth = 1


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

    class Meta:
        depth = 1
