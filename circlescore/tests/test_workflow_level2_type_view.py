from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import WorkflowLevel2Type


class WorkflowLevel2TypeViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='tyei709q'
        )

    def test_post_workflow_level2_type(self):
        """
        Test WorkflowLevel2Type Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('workflowlevel2type-list'),
            {'type': 'type1'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['type'], 'type1')

    def test_retrieve_workflow_level2_type(self):
        """
        Test WorkflowLevel2Type Retrieve
        """
        self.client.force_authenticate(self.user)
        worflow_level2_type = WorkflowLevel2Type.objects.create(type='type2')

        response = self.client.get(
            reverse(
                'workflowlevel2type-detail',
                kwargs={'type_uuid': worflow_level2_type.type_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'type2')

    def test_update_workflow_level2_type(self):
        """
        Test WorkflowLevel2Type Update
        """
        self.client.force_authenticate(self.user)
        workflow_level2_type = WorkflowLevel2Type.objects.create(type='type3')

        response = self.client.put(
            reverse(
                'workflowlevel2type-detail',
                kwargs={'type_uuid': workflow_level2_type.type_uuid}
            ),
            {'type': 'type3 update'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'type3 update')

    def test_list_workflow_level2_type(self):
        """
        Test WorkflowLevel2Type List
        """
        self.client.force_authenticate(self.user)

        WorkflowLevel2Type.objects.create(type='type4')

        response = self.client.get(reverse('workflowlevel2type-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_workflow_level2_type(self):
        """
        Test WorkflowLevel2Type delete
        """
        self.client.force_authenticate(self.user)
        workflow_level2_type = WorkflowLevel2Type.objects.create(type='type5')

        response = self.client.delete(
            reverse(
                'workflowlevel2type-detail',
                kwargs={'type_uuid': workflow_level2_type.type_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            WorkflowLevel2Type.DoesNotExist,
            WorkflowLevel2Type.objects.get,
            type_uuid=workflow_level2_type.type_uuid
        )
