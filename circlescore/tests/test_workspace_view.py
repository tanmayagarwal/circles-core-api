from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class WorkspaceViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='username1',
            email='username@test.com',
            is_staff=True,
            password='test1234'
        )

    def test_post_workspace(self):
        self.client.force_authenticate(self.user)
        workspace_data = {
            'name': 'Workspace 1',
            'uuid': 'eghsbsiisoahjs'
        }
        response = self.client.post(
            '/api/v1/workspace/',
            workspace_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

