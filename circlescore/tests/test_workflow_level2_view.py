from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import (Workspace, WorkflowLevel1, WorkflowLevel2)


class WorkflowLevel2ViewSetTestCase(APITestCase):
    """
    WorkflowLevel2 ViewSet
    """
    def setUp(self):
        self.client = APIClient()
        workspace = Workspace.objects.create(name='My Workspace')
        self.workflow_level1 = WorkflowLevel1.objects.create(
            name='Test 1',
            workspace=workspace
        )
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='1234dfg'
        )

    def test_post_workflow_level2(self):
        """
        Test WorkflowLevel2 Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('workflowlevel2-list'),
            {
                'name': 'test Project',
                'workflow_level1': reverse(
                    'workflowlevel1-detail',
                    kwargs={
                        'workflow_level1_uuid':
                            self.workflow_level1.workflow_level1_uuid
                    }
                )
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'test Project')

    def test_update_workflow_level2(self):
        """
        Test WorkflowLevel2 Update
        """
        self.client.force_authenticate(self.user)

        workflow_level2 = WorkflowLevel2.objects.create(
            name='Test',
            workflow_level1=self.workflow_level1
        )

        response = self.client.put(
            reverse(
                'workflowlevel2-detail',
                kwargs={
                    'workflow_level2_uuid': workflow_level2.workflow_level2_uuid
                }
            ),
            {
                'name': 'Another project',
                'workflow_level1': reverse(
                    'workflowlevel1-detail',
                    kwargs={
                        'workflow_level1_uuid':
                            self.workflow_level1.workflow_level1_uuid
                    }
                )
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Another project')

    def test_retrieve_workflow_level2(self):
        """
        Test WorkflowLevel2 Retrieve
        """
        self.client.force_authenticate(self.user)
        workflow_level2 = WorkflowLevel2.objects.create(
            name='Test 2',
            workflow_level1=self.workflow_level1
        )

        response = self.client.get(
            reverse(
                'workflowlevel2-detail',
                kwargs={
                    'workflow_level2_uuid': workflow_level2.workflow_level2_uuid
                }
            ),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test 2')

    def test_list_workflow_level2(self):
        """
        Test WorkflowLevel2 List
        """
        self.client.force_authenticate(self.user)
        WorkflowLevel2.objects.create(
            name='Test 3',
            workflow_level1=self.workflow_level1
        )

        response = self.client.get(reverse('workflowlevel2-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_workflow_level2(self):
        """
        Test WorkflowLevel2 Delete
        """
        self.client.force_authenticate(self.user)

        workflow_level2 = WorkflowLevel2.objects.create(
            name='Test 2',
            workflow_level1=self.workflow_level1
        )

        response = self.client.delete(
            reverse(
                'workflowlevel2-detail',
                kwargs={
                    'workflow_level2_uuid': workflow_level2.workflow_level2_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            WorkflowLevel2.DoesNotExist,
            WorkflowLevel2.objects.get,
            workflow_level2_uuid=workflow_level2.workflow_level2_uuid
        )
