from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import WorkflowStatus


class WorkflowStatusViewSetTestCase(APITestCase):
    """
    WorkflowStatus View Test
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='567389'
        )

    def test_post_workflow_status(self):
        """
        Test WorkflowStatus Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('workflowstatus-list'),
            {'status': 'open'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_workflow_status(self):
        """
        Test WorkflowStatus Retrieve
        """
        self.client.force_authenticate(self.user)

        workflow_status = WorkflowStatus.objects.create(status='new')

        response = self.client.get(
            reverse(
                'workflowstatus-detail',
                kwargs={
                    'status_uuid': workflow_status.status_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'new')

    def test_update_workflow_status(self):
        """
        Test WorkflowStatus Update
        """
        self.client.force_authenticate(self.user)

        workflow_status = WorkflowStatus.objects.create(status='approved')

        response = self.client.put(
            reverse(
                'workflowstatus-detail',
                kwargs={
                    'status_uuid': workflow_status.status_uuid
                }
            ),
            {'status': 'closed'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'closed')

    def test_list_workflow_status(self):
        """
        Test WorkflowStatus List
        """
        self.client.force_authenticate(self.user)

        WorkflowStatus.objects.create(status='accepted')

        response = self.client.get(reverse('workflowstatus-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_workflow_status(self):
        """
        Test WorkflowStatus Delete
        """
        self.client.force_authenticate(self.user)

        workflow_status = WorkflowStatus.objects.create(status='test')

        response = self.client.delete(
            reverse(
                'workflowstatus-detail',
                kwargs={
                    'status_uuid': workflow_status.status_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            WorkflowStatus.DoesNotExist,
            WorkflowStatus.objects.get,
            status_uuid=workflow_status.status_uuid
        )
