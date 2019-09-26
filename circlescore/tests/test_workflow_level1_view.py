from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import (WorkflowLevel1, Workspace)


class WorkflowLevel1ViewSetTestCase(APITestCase):
    """
    WorkflowLevel1 ViewSet
    """
    def setUp(self):
        self.client = APIClient()
        self.workspace = Workspace.objects.create(name='My Workspace')
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='1234dfg'
        )

    def test_post_workflow_level1(self):
        """
        Test WorkflowLevel1 Post
        """
        self.client.force_authenticate(self.user)
        print('Workspace', )
        workspace = reverse(
                    'workspace-detail',
                    kwargs={'uuid': self.workspace.uuid}
                )
        response = self.client.post(
            reverse('workflowlevel1-list'),
            {
                'name': 'test program',
                'workspace': '{}'.format(workspace)
            },
            format='json'
        )

        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'test program')

    def test_update_workflow_level1(self):
        """
        Test WorkflowLevel1 Update
        """
        self.client.force_authenticate(self.user)

        workflow_level1 = WorkflowLevel1.objects.create(
            name='Test',
            workspace=self.workspace
        )

        response = self.client.put(
            reverse(
                'workflowlevel1-detail',
                kwargs={
                    'workflow_level1_uuid': workflow_level1.workflow_level1_uuid
                }
            ),
            {
                'name': 'Another program',
                'workspace': reverse(
                    'workspace-detail', kwargs={'uuid': self.workspace.uuid}
                )
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Another program')

    def test_retrieve_workflow_level1(self):
        """
        Test WorkflowLevel1 Retrieve
        """
        self.client.force_authenticate(self.user)
        workflow_level1 = WorkflowLevel1.objects.create(
            name='Test 2',
            workspace=self.workspace
        )

        response = self.client.get(
            reverse(
                'workflowlevel1-detail',
                kwargs={
                    'workflow_level1_uuid': workflow_level1.workflow_level1_uuid
                }
            ),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test 2')

    def test_list_workflow_level1(self):
        """
        Test WorkflowLevel1 List
        """
        self.client.force_authenticate(self.user)
        WorkflowLevel1.objects.create(
            name='Test 3',
            workspace=self.workspace
        )

        response = self.client.get(reverse('workflowlevel1-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_workflow_level1(self):
        """
        Test WorkflowLevel1 Delete
        """
        self.client.force_authenticate(self.user)

        workflow_level1 = WorkflowLevel1.objects.create(
            name='Test 2',
            workspace=self.workspace
        )

        response = self.client.delete(
            reverse(
                'workflowlevel1-detail',
                kwargs={
                    'workflow_level1_uuid': workflow_level1.workflow_level1_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            WorkflowLevel1.DoesNotExist,
            WorkflowLevel1.objects.get,
            workflow_level1_uuid=workflow_level1.workflow_level1_uuid
        )
