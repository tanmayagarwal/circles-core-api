from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import (
    Workspace, WorkflowLevel1, WorkflowLevel2, WorkflowLevel2Plan,
)


class WorkflowLevel2PlanViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='5wyhucwer'
        )

        workspace = Workspace.objects.create(name='test')
        self.wfl1 = WorkflowLevel1.objects.create(name='Test 2', workspace=workspace)
        self.wfl2 = WorkflowLevel2.objects.create(
            name='Test Project',
            workflow_level1=self.wfl1
        )

    def test_post_workflow_level2_plan(self):
        """
        Test WorkflowLevel2Plan Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('workflowlevel2plan-list'),
            {
                'name': 'Test Plan',
                'workflow_level1': reverse(
                    'workflowlevel1-detail',
                    kwargs={
                        'workflow_level1_uuid': self.wfl1.workflow_level1_uuid
                    }
                ),
                'workflow_level2': reverse(
                    'workflowlevel2-detail',
                    kwargs={
                        'workflow_level2_uuid': self.wfl2.workflow_level2_uuid
                    }
                )
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test Plan')

    def test_retrieve_workflow_level2_plan(self):
        """
        Test WorkflowLevel2Plan Retrieve
        """
        self.client.force_authenticate(self.user)
        workflow_level2_plan = WorkflowLevel2Plan.objects.create(
            name='Another Plan',
            workflow_level1=self.wfl1,
            workflow_level2=self.wfl2
        )

        response = self.client.get(
            reverse(
                'workflowlevel2plan-detail',
                kwargs={
                    'workflow_level2_plan_uuid':
                        workflow_level2_plan.workflow_level2_plan_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Another Plan')

    def test_update_workflow_level2_plan(self):
        """
        Test WorkflowLevel2Plan Update
        """
        self.client.force_authenticate(self.user)
        workflow_level2_plan = WorkflowLevel2Plan.objects.create(
            name='Another Plan',
            workflow_level1=self.wfl1,
            workflow_level2=self.wfl2
        )

        response = self.client.put(
            reverse(
                'workflowlevel2plan-detail',
                kwargs={
                    'workflow_level2_plan_uuid': workflow_level2_plan.workflow_level2_plan_uuid
                }
            ),
            {
                'name': 'Plan2',
                'workflow_level1': reverse(
                    'workflowlevel1-detail',
                    kwargs={
                        'workflow_level1_uuid': self.wfl1.workflow_level1_uuid
                    }
                ),
                'workflow_level2': reverse(
                    'workflowlevel2-detail',
                    kwargs={
                        'workflow_level2_uuid': self.wfl2.workflow_level2_uuid
                    }
                )
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Plan2')

    def test_list_workflow_level2_plan(self):
        """
        Test WorkflowLevel2Plan List
        """
        self.client.force_authenticate(self.user)
        WorkflowLevel2Plan.objects.create(
            name='Plan 3',
            workflow_level1=self.wfl1,
            workflow_level2=self.wfl2
        )

        response = self.client.get(reverse('workflowlevel2plan-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_workflow_level2_plan(self):
        """
        Test WorkflowLevel2Plan Delete
        """
        self.client.force_authenticate(self.user)

        workflow_level2_plan = WorkflowLevel2Plan.objects.create(
            name='Another Plan',
            workflow_level1=self.wfl1,
            workflow_level2=self.wfl2
        )

        response = self.client.delete(
            reverse(
                'workflowlevel2plan-detail',
                kwargs={
                    'workflow_level2_plan_uuid': workflow_level2_plan.workflow_level2_plan_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            WorkflowLevel2Plan.DoesNotExist,
            WorkflowLevel2Plan.objects.get,
            workflow_level2_plan_uuid=workflow_level2_plan.workflow_level2_plan_uuid
        )
