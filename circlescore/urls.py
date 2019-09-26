from django.urls import path

from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'document', DocumentViewSet)
router.register(r'workspace', WorkspaceViewSet)
router.register(r'hikayauser', HikayaUserViewSet)
router.register(r'accounttype', AccountTypeViewSet)
router.register(r'accountsubtype', AccountSubTypeViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'location', LocationViewSet)
router.register(r'office', OfficeViewSet)
router.register(r'currency', CurrencyViewSet)
router.register(r'locationtype', LocationTypeViewSet)
router.register(r'fundingstatus', FundingStatusViewSet)
router.register(r'workflowstatus', WorkflowStatusViewSet)
router.register(r'workflowlevel1type', WorkflowLevel1TypeViewSet)
router.register(r'workflowlevel2type', WorkflowLevel2TypeViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('user/auth/login/', auth_login, name='user_login')
]
