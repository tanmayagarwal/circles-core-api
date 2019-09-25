from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from circlescore.models import Workspace


class WorkspaceViewTest(APITestCase):
    """
    Workspace View set tests
    """
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
        workspace_data = {'name': 'Workspace 1'}
        response = self.client.post(
            '/api/v1/workspace/',
            workspace_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_workspace(self):
        self.client.force_authenticate(self.user)
        workspace_data = {'name': 'Workspace 1'}
        workspace = Workspace.objects.create(**workspace_data)
        response = self.client.put(
            reverse('workspace-detail', kwargs={'uuid': workspace.uuid}),
            {'name': 'Workspace 2'}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Workspace 2')

    def test_list_workspaces(self):
        self.client.force_authenticate(self.user)
        workspace_data = {'name': 'Workspace 1'}
        Workspace.objects.create(**workspace_data)
        response = self.client.get(reverse('workspace-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_workspace(self):
        self.client.force_authenticate(self.user)
        workspace_data = {'name': 'Workspace 1'}
        workspace =Workspace.objects.create(**workspace_data)

        response = self.client.delete(
            reverse(
                'workspace-detail',
                kwargs={'uuid': workspace.uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # getting the deleted item should throw DoesNotExist Exception
        self.assertRaises(
            Workspace.DoesNotExist,
            Workspace.objects.get,
            uuid=workspace.uuid
        )
        # or checking if the deleted item exists should be false
        self.assertFalse(Workspace.objects.filter(
            uuid=workspace.uuid).exists())

    def test_get_workspace_details(self):
        self.client.force_authenticate(self.user)
        workspace_data = {'name': 'Workspace 1'}
        workspace = Workspace.objects.create(**workspace_data)

        response = self.client.get(
            reverse('workspace-detail', kwargs={'uuid': workspace.uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Workspace 1')
