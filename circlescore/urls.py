from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)

urlpatterns = router.urls
