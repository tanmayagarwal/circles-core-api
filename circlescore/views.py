from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    Auth User view set
    Uses django core user model
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


