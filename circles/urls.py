"""
circles URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url, include
from rest_framework_swagger.views import get_swagger_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView,
)

schema_view = get_swagger_view(title='Circles Core API')

urlpatterns = [
    # register admin site
    path('admin/', admin.site.urls),
    # add django rest browsable api urls
    url(r'^api/v1/api-auth/', include('rest_framework.urls')),
    # swagger docs url
    url(r'^api/v1/documentation/$', schema_view),
    # jwt urls
    url(r'^api/v1/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/v1/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]