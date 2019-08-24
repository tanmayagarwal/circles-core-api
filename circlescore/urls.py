from django.urls import path

from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'workspace', WorkspaceViewSet)
router.register(r'hikayauser', HikayaUserViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('user/auth/login/', auth_login, name='user_login')
]
